import json
import requests
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

TARGET_BASE = "https://animalcompany.us-east1.nakamacloud.io"
SPOOFED_VERSION = "1.29.1.1463"
SPOOFED_CODE = "1463"

def patch_json_bytes(data_bytes: bytes) -> bytes:
    try:
        obj = json.loads(data_bytes)
        if isinstance(obj, dict):
            obj["AppVersion"] = SPOOFED_VERSION
            obj["AppVersionCode"] = SPOOFED_CODE
            return json.dumps(obj).encode("utf-8")
    except Exception as e:
        app.logger.error(f"JSON patching error: {e}")
    return data_bytes

def forward_request(method: str, path: str):
    url = TARGET_BASE + path
    headers = dict(request.headers)
    headers["Host"] = "animalcompany.us-east1.nakamacloud.io"
    headers["User-Agent"] = f"MetaQuestClient/{SPOOFED_VERSION}"

    # Read raw data once
    raw_data = request.get_data()
    app.logger.debug(f"Incoming raw data: {raw_data}")

    # Patch JSON if Content-Type is JSON and method is POST
    content_type = headers.get("Content-Type", "")
    if method == "POST" and content_type.startswith("application/json"):
        patched_data = patch_json_bytes(raw_data)
        app.logger.debug(f"Patched JSON data: {patched_data}")
    else:
        patched_data = raw_data

    try:
        resp = requests.request(method, url, headers=headers, data=patched_data, timeout=10)
    except requests.RequestException as e:
        app.logger.error(f"Upstream request failed: {e}")
        return jsonify({"error": str(e)}), 502

    excluded_headers = ['content-encoding', 'transfer-encoding', 'content-length', 'connection']
    resp_headers = [(k, v) for k, v in resp.raw.headers.items() if k.lower() not in excluded_headers]

    app.logger.debug(f"Upstream response status: {resp.status_code}")
    app.logger.debug(f"Upstream response headers: {resp_headers}")

    return Response(resp.content, resp.status_code, resp_headers)

@app.route("/v2/account", methods=["GET"])
def v2_account():
    return forward_request("GET", "/v2/account")

@app.route("/v2/storage", methods=["POST"])
def v2_storage():
    return forward_request("POST", "/v2/storage")

@app.route("/v2/account/link/device", methods=["POST"])
def v2_link_device():
    return forward_request("POST", "/v2/account/link/device")

@app.route("/v2/rpc/clientBootstrap", methods=["POST"])
def v2_rpc_bootstrap():
    return forward_request("POST", "/v2/rpc/clientBootstrap")

@app.route("/v2/account/authenticate/custom", methods=["POST"])
def v2_auth_custom():
    return forward_request("POST", "/v2/account/authenticate/custom")

@app.route("/")
def index():
    return "<h2>✅ Proxy Running</h2>"

if __name__ == "__main__":
    # To see debug logs, run with: FLASK_ENV=development python yourscript.py
    app.run(host="0.0.0.0", port=3002, debug=True)
