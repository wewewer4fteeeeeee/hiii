import json
import requests
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

TARGET_BASE = "https://animalcompany.us-east1.nakamacloud.io"
SPOOFED_VERSION = "1.29.1.1463"
SPOOFED_CODE = "1463"

def is_json(headers):
    content_type = headers.get("Content-Type", "")
    return content_type.startswith("application/json")

def patch_json(data: bytes) -> bytes:
    try:
        body = json.loads(data)
        if isinstance(body, dict):
            body["AppVersion"] = SPOOFED_VERSION
            body["AppVersionCode"] = SPOOFED_CODE
            return json.dumps(body).encode("utf-8")
    except Exception as e:
        app.logger.warning(f"Failed to patch JSON body: {e}")
    return data

def forward(method, path):
    url = f"{TARGET_BASE}{path}"
    headers = dict(request.headers)
    headers["Host"] = "animalcompany.us-east1.nakamacloud.io"
    headers["User-Agent"] = f"MetaQuestClient/{SPOOFED_VERSION}"

    body = request.get_data()
    if is_json(headers):
        body = patch_json(body)

    app.logger.info(f"Forwarding {method} {path} to {url}")

    try:
        resp = requests.request(
            method=method,
            url=url,
            headers=headers,
            data=body,
            timeout=10,
        )
    except requests.exceptions.Timeout:
        return jsonify({"error": "Upstream request timed out"}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Failed to connect to upstream server"}), 502
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    response_headers = [(k, v) for k, v in resp.raw.headers.items() if k.lower() not in excluded_headers]

    return Response(resp.content, resp.status_code, response_headers)

@app.route("/v2/account", methods=["GET"])
def v2_account():
    return forward("GET", "/v2/account")

@app.route("/v2/storage", methods=["POST"])
def v2_storage():
    return forward("POST", "/v2/storage")

@app.route("/v2/account/link/device", methods=["POST"])
def v2_link_device():
    return forward("POST", "/v2/account/link/device")

@app.route("/v2/rpc/clientBootstrap", methods=["POST"])
def v2_rpc_bootstrap():
    return forward("POST", "/v2/rpc/clientBootstrap")

@app.route("/v2/account/authenticate/custom", methods=["POST"])
def v2_auth_custom():
    return forward("POST", "/v2/account/authenticate/custom")

@app.route("/")
def index():
    return "<h2>✅ Flask Proxy Running</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002, debug=True)
