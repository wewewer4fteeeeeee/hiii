import json
import os
from flask import Flask, request, Response
import urllib3

app = Flask(__name__)
http = urllib3.PoolManager()

TARGET_BASE = "https://animalcompany.us-east1.nakamacloud.io"
VERSION_STRING = "1.29.1.1463"
VERSION_CODE = "1463"
USERDATA_FILE = "user_account_data.json"

def save_user_account_data(username, data):
    if not os.path.exists(USERDATA_FILE):
        user_db = {}
    else:
        with open(USERDATA_FILE, "r") as f:
            try:
                user_db = json.load(f)
            except json.JSONDecodeError:
                user_db = {}

    user_db[username] = data

    with open(USERDATA_FILE, "w") as f:
        json.dump(user_db, f, indent=2)

def forward_raw_and_save_response(path, method):
    url = f"{TARGET_BASE}{path}"
    body = request.get_data()

    headers = {k: v for k, v in request.headers.items() if k.lower() != "host"}
    headers["X-Unity-Version"] = VERSION_STRING
    headers["User-Agent"] = VERSION_STRING
    headers["VersionCode"] = VERSION_CODE
    headers = {str(k): str(v) for k, v in headers.items()}

    resp = http.request(
        method=method,
        url=url,
        body=body,
        headers=headers,
        redirect=False,
        preload_content=False
    )

    response_body = resp.read()
    resp.release_conn()

    # Attempt to get username from request headers or default
    username = request.headers.get("Username", "UnknownUser")

    # Try to parse response body as JSON to save (optional)
    try:
        json_data = json.loads(response_body.decode('utf-8'))
    except Exception:
        json_data = response_body.decode('utf-8', errors='ignore')

    # Save response data keyed by username
    save_user_account_data(username, json_data)

    return Response(response_body, status=resp.status, headers=resp.headers)


@app.route("/v2/account", methods=["GET"])
def route_account_get():
    return forward_raw_and_save_response("/v2/account", "GET")


# Other routes just do normal raw forwarding without saving

def forward_raw(path, method):
    url = f"{TARGET_BASE}{path}"
    body = request.get_data()
    headers = {k: v for k, v in request.headers.items() if k.lower() != "host"}
    headers["X-Unity-Version"] = VERSION_STRING
    headers["User-Agent"] = VERSION_STRING
    headers["VersionCode"] = VERSION_CODE
    headers = {str(k): str(v) for k, v in headers.items()}

    resp = http.request(
        method=method,
        url=url,
        body=body,
        headers=headers,
        redirect=False,
        preload_content=False
    )
    response_body = resp.read()
    resp.release_conn()
    return Response(response_body, status=resp.status, headers=resp.headers)


@app.route("/v2/storage", methods=["POST"])
def route_storage_post():
    return forward_raw("/v2/storage", "POST")

@app.route("/v2/account/link/device", methods=["POST"])
def route_link_device_post():
    return forward_raw("/v2/account/link/device", "POST")

@app.route("/v2/rpc/clientBootstrap", methods=["POST"])
def route_client_bootstrap_post():
    return forward_raw("/v2/rpc/clientBootstrap", "POST")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
