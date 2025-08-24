# file: modded_backend.py
from flask import Flask, jsonify, request

app = Flask(__name__)

LOCAL_USER_ID = "12345678-ABCD-4321-EFGH-87654321"

@app.route("/v2/account", methods=["GET", "POST"])
def account():
    # Return OWNER JSON
    return jsonify({
        "user": {
            "id": LOCAL_USER_ID,
            "username": "OWNER",
            "display_name": "<color=red>OWNER</color>",
            "lang_tag": "en",
            "metadata": {"isDeveloper": True},
            "edge_count": 4,
            "create_time": "2024-08-24T07:30:12Z",
            "update_time": "2025-04-05T21:00:27Z"
        },
        "wallet": {
            "stashCols": 4,
            "stashRows": 2,
            "hardCurrency": 999999999999,
            "softCurrency": 100000,
            "researchPoints": 999999999999
        },
        "custom_id": LOCAL_USER_ID
    })

@app.route("/<path:path>", methods=["GET", "POST"])
def proxy_all(path):
    # Forward everything else to the real NakamaCloud server
    import requests
    real_url = f"https://animalcompany.us-east1.nakamacloud.io/{path}"
    if request.method == "POST":
        resp = requests.post(real_url, json=request.get_json(), headers=request.headers)
    else:
        resp = requests.get(real_url, headers=request.headers)
    return (resp.content, resp.status_code, resp.headers.items())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4049, ssl_context="adhoc")  # HTTPS
