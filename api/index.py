from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)

TARGET_URL = "https://animalcompany.us-east1.nakamacloud.io/v2/account/authenticate/custom"
SPOOFED_VERSION = "1.29.1.1463"
SPOOFED_CODE = "1463"

@app.route("/v2/account/authenticate/custom", methods=["POST"])
def mirror_and_patch():
    try:
        raw_body = request.data
        payload = json.loads(raw_body)

        # Patch or add version fields
        payload["AppVersion"] = SPOOFED_VERSION
        payload["AppVersionCode"] = SPOOFED_CODE

        # Re-encode JSON to bytes
        patched_body = json.dumps(payload).encode("utf-8")

        # Copy headers and remove Content-Length to let requests lib set it properly
        headers = dict(request.headers)
        headers["Host"] = "animalcompany.us-east1.nakamacloud.io"
        headers.pop("Content-Length", None)

        # Forward patched request to upstream
        resp = requests.post(
            TARGET_URL,
            data=patched_body,
            headers=headers,
            timeout=10
        )

        # Filter response headers for Flask response
        excluded = ['content-encoding', 'transfer-encoding', 'content-length', 'connection']
        response_headers = [(k, v) for k, v in resp.headers.items() if k.lower() not in excluded]

        return Response(resp.content, status=resp.status_code, headers=dict(response_headers))

    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500, mimetype="application/json")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443)
