from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)

TARGET_BASE = "https://animalcompany.us-east1.nakamacloud.io"
SPOOFED_VERSION = "1.29.1.1463"
SPOOFED_CODE = "1463"

def patch_json_body(raw_body):
    try:
        obj = json.loads(raw_body)
        if isinstance(obj, dict):
            obj["AppVersion"] = SPOOFED_VERSION
            obj["AppVersionCode"] = SPOOFED_CODE
            return json.dumps(obj).encode("utf-8")
    except Exception as e:
        app.logger.error(f"Failed to patch JSON body: {e}")
    return raw_body

def forward_request(path):
    url = TARGET_BASE + path
    headers = dict(request.headers)
    headers["Host"] = "animalcompany.us-east1.nakamacloud.io"
    headers.pop("Content-Length", None)

    body = request.data
    if request.method == "POST" and headers.get("Content-Type", "").startswith("application/json"):
        body = patch_json_body(body)

    resp = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=body
    )

    excluded_headers = ['content-encoding', 'transfer-encoding', 'content-length', 'connection']
    response_headers = [(k, v) for k, v in resp.headers.items() if k.lower() not in excluded_headers]

    return Response(resp.content, status=resp.status_code, headers=dict(response_headers))

# Explicitly route your needed endpoints
@app.route("/v2/account", methods=["GET"])
def route_account():
    return forward_request("/v2/account")

@app.route("/v2/storage", methods=["POST"])
def route_storage():
    return forward_request("/v2/storage")

@app.route("/v2/account/link/device", methods=["POST"])
def route_link_device():
    return forward_request("/v2/account/link/device")

@app.route("/v2/rpc/clientBootstrap", methods=["POST"])
def route_client_bootstrap():
    return forward_request("/v2/rpc/clientBootstrap")

@app.route("/v2/account/authenticate/custom", methods=["POST"])
def route_auth_custom():
    return forward_request("/v2/account/authenticate/custom")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002, debug=True)
