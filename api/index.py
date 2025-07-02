from fastapi import FastAPI, Request, Response, WebSocket
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests, json, logging, os, re, urllib.parse
from datetime import datetime
from websockets.client import connect as ws_connect

app = FastAPI()

TARGET_BASE = 'https://animalcompany.us-east1.nakamacloud.io'
WEBHOOK_URL = 'webhookgohere'
LOG_DIR = "request_logs"
os.makedirs(LOG_DIR, exist_ok=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def spoof_headers(headers: dict):
    spoofed = {
        k: v for k, v in headers.items()
        if not k.lower().startswith("x-replit-") and k.lower() not in ['host', 'content-length', 'transfer-encoding']
    }
    spoofed.update({
        "X-Unity-Version": "1.29.1.1463",
        "User-Agent": "1.29.1.1463",
        "App-Version": "1.29.1.1463",
        "Oculus-SDK-Version": "1463",
        "Device-Model": "Quest2",
        "Platform": "Android",
        "Device-ID": "00:00:00:00:00:00",
        "X-Platform-Version": "1.29.1.1463"
    })
    return spoofed

def spoof_body(body: str):
    body = re.sub(r'(\"?client[_-]?version\"?\s*[:=]\s*[\"\']?)[^"\']+', r'\g<1>1.29.1.1463', body)
    body = re.sub(r'(\"?version[_-]?code\"?\s*[:=]\s*)\d+', r'\g<1>1463', body)
    body = re.sub(r'(\"?oculus[_-]?sdk[_-]?version\"?\s*[:=]\s*)[\"\']?[^"\']+', r'\g<1>1463', body)
    body = re.sub(r'(\"?platform\"?\s*[:=]\s*)[\"\']?[^"\']+', r'\g<1>Android', body)
    body = re.sub(r'(\"?device[_-]?model\"?\s*[:=]\s*)[\"\']?[^"\']+', r'\g<1>Quest2', body)
    body = re.sub(r'(\"?buildNumber\"?\s*[:=]\s*)\d+', r'\g<1>1463', body)
    body = re.sub(r'(\"?metaQuestStoreVersion\"?\s*[:=]\s*)\d+', r'\g<1>1463', body)
    body = re.sub(r'(\"?min_supported_version\"?\s*[:=]\s*)[\"\']?[^"\']+', r'\g<1>1.0.0', body)
    return body

async def forward_request(path: str, request: Request):
    method = request.method
    target_url = f"{TARGET_BASE}/{path.lstrip('/')}"
    headers = spoof_headers(dict(request.headers))
    raw_data = await request.body()
    body_str = spoof_body(raw_data.decode('utf-8', errors='ignore'))

    if path.endswith("clientBootstrap"):
        try:
            json_request = json.loads(body_str)
            if isinstance(json_request, dict):
                json_request["clientVersion"] = "1.29.1.1463"
                json_request["oculus_sdk_version"] = "1463"
                json_request["deviceModel"] = "Quest2"
                json_request["platform"] = "Android"
                json_request["buildNumber"] = "1463"
                json_request["metaQuestStoreVersion"] = "1463"
                json_request["min_supported_version"] = "1.0.0"
                body_str = json.dumps(json_request)
        except:
            pass

    try:
        forwarded_response = requests.request(
            method=method,
            url=target_url,
            headers=headers,
            data=body_str.encode(),
            allow_redirects=False
        )

        content_type = forwarded_response.headers.get("Content-Type", "")
        modified_content = forwarded_response.content

        if 'application/json' in content_type:
            try:
                json_response = forwarded_response.json()

                if 'wallet' in json_response:
                    wallet = json.loads(json_response['wallet']) if isinstance(json_response['wallet'], str) else json_response['wallet']
                    wallet = {"hardCurrency": 2000000, "companyCoins": 2000000}
                    json_response['wallet'] = json.dumps(wallet)

                if 'user' in json_response and 'username' in json_response['user']:
                    json_response['user']['username'] = "ModHub User"

                json_response = {k: v for k, v in json_response.items() if k not in ['forceUpdate', 'unsupportedVersion']}
                json_response.update({
                    "forceUpdate": False,
                    "min_supported_version": "1.0.0",
                    "recommended_version": "1.29.1.1463",
                })

                modified_content = json.dumps(json_response).encode()
            except:
                pass

        filtered_headers = {
            k: v for k, v in forwarded_response.headers.items()
            if k.lower() not in ['content-encoding', 'transfer-encoding', 'connection']
        }

        return Response(
            content=modified_content,
            status_code=forwarded_response.status_code,
            headers=filtered_headers,
            media_type=content_type
        )

    except Exception as e:
        return JSONResponse(content={"error": "Proxy Error", "details": str(e)}, status_code=502)

@app.middleware("http")
async def log_request_route(request: Request, call_next):
    print(f"[ROUTE] {request.method} {request.url.path}")
    return await call_next(request)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=1008)
        return
    try:
        token = urllib.parse.quote(token)
        url = f"wss://animalcompany.us-east1.nakamacloud.io/ws?lang=en&status=True&token={token}"
        async with ws_connect(url) as ws:
            result = await ws.recv()
            await websocket.send_text(result)
    except Exception as e:
        await websocket.send_text(f"Error: {e}")
        await websocket.close()

@app.api_route('/v2/{path:path}', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
async def handle_all_v2(path: str, request: Request):
    return await forward_request(f"v2/{path}", request)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
