import json
import requests
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

TARGET_BASE = "https://animalcompany.us-east1.nakamacloud.io"
SPOOFED_VERSION = "1.29.1.1463"
SPOOFED_CODE = "1463"

def patch_json_from_bytes(data_bytes: bytes) -> bytes:
    try:
        obj = json.loads(data_bytes)
        if isinstance(obj, dict):
            obj["AppVersion"] = SPOOFED_VERSION
            obj["AppVersionCode"] = SPOOFED_CODE
            return json.dumps(obj).encode("utf-8")
    except Exception as e:
        app.logger.warning(f"patch_json_from_bytes error: {e}")
    return data_bytes

def forward_request(method: str, path: str):
    url = TARGET_BASE + path
    headers = dict(request.headers)
    headers["Host"] = "animalcompany.us-east1.nakamacloud.io"
    headers["User-Agent"] = f"MetaQuestClient/{SPOOFED_VERSION}"

    body = request.data
    content_type = headers.get("Content-Type", "")
    if method == "POST" and content_type.startswith("application/json"):
        body = patch_json_from_bytes(body)

    try:
        resp = requests.request(method, url, headers=headers, data=body, timeout=10)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 502

    excluded = ['content-encoding', 'transfer-encoding', 'content-length', 'connection']
    resp_headers = [(k, v) for k, v in resp.raw.headers.items() if k.lower() not in excluded]

    return Response(resp.content, resp.status_code, resp_headers)

@app.route("/v2/account", methods=["GET"])
def account_get():
    return forward_request("GET", "/v2/account")

@app.route("/v2/storage", methods=["POST"])
def storage_post():
    return forward_request("POST", "/v2/storage")

@app.route("/v2/account/link/device", methods=["POST"])
def link_device_post():
    return forward_request("POST", "/v2/account/link/device")

@app.route("/v2/rpc/clientBootstrap", methods=["POST"])
def rpc_bootstrap_post():
    return forward_request("POST", "/v2/rpc/clientBootstrap")

@app.route("/v2/account/authenticate/custom", methods=["POST"])
def authenticate_custom_post():
    return forward_request("POST", "/v2/account/authenticate/custom")

@app.route("/")
def home():
    return "<h2>✅ Proxy Running</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002, debug=True)
