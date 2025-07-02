from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)

# Update target base to your PythonAnywhere backend
TARGET_BASE = "https://bytecompany-0x11avaite.pythonanywhere.com"
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

    excluded_headers = {"content-length", "transfer-encoding", "connection", "host"}
    headers = {
        k: v for k, v in request.headers.items() if k.lower() not in excluded_headers
    }
    headers["Host"] = url.split("//")[1].split("/")[0]  # Host based on TARGET_BASE
    headers["User-Agent"] = f"MetaQuestClient/{SPOOFED_VERSION}"

    body = request.data
    if request.method == "POST" and headers.get("Content-Type", "").startswith("application/json"):
        body = patch_json_body(body)

    resp = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=body,
        allow_redirects=False,
    )

    excluded_resp_headers = {
        "content-encoding",
        "transfer-encoding",
        "content-length",
        "connection",
        "keep-alive",
        "proxy-authenticate",
        "proxy-authorization",
        "te",
        "trailers",
        "upgrade",
    }
    response_headers = [
        (name, value) for name, value in resp.headers.items()
        if name.lower() not in excluded_resp_headers
    ]

    return Response(resp.content, status=resp.status_code, headers=dict(response_headers))

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
def route_authenticate_custom():
    return forward_request("/v2/account/authenticate/custom")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002, debug=True)
