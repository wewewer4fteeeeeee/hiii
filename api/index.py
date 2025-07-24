import json
import re
import secrets
import base64
import time
import sqlite3
import random
import os
import string
import ipaddress
import requests
import supabase
from flask import Flask, request, jsonify, make_response
from supabase import create_client

# black
ProdZipFile = "https://raw.githubusercontent.com/wewewer4fteeeeeee/fuv/main/game-data-prod.zip"
DILDOPENIS = "https://raw.githubusercontent.com/wewewer4fteeeeeee/fuv/main/game-data-prod/econ_gameplay_items"
PhotonAppId = "4a3b27ff-1e95-4e94-a05f-9da825e96a3d"
PhotonVoiceAppId = "0808b51b-92f6-4514-8f97-8039d0953338"
DATABASE_PASSWORDNOTREQUIRED = "MOONCOMPANYAPI69"
SUPABASE_URL = "https://ektoydwsqbbwobqgboos.supabase.co"
WHITELIST_USERS = ["camdrippy31", "Sxhadow", "exploding_car"]
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVrdG95ZHdzcWJid29icWdib29zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMzODk2NjMsImV4cCI6MjA2ODk2NTY2M30.dc-aQsMJ-qIPfouDI7Ekbl8xN26ZNJdtfA36dzmVB38"
dihhcord = "https://discord.com/api/webhooks/1388254061811335199/Q_u4im3xkpdbXtSL7-JPAfPmFIcVQBMBY-Gd_tB18bTtAq0i435Kh7B3v4si0_0TQA0O"
app = Flask(__name__)
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

GITHUB_ZIP_URL = "https://raw.githubusercontent.com/wewewer4fteeeeeee/fuv/main/game-data-prod.zip"

def log_to_discord(message: str):
    try:
        requests.post(dihhcord, json={"content": message})
    except Exception as e:
        print(f"[Webhook Error] {e}")

@app.before_request
def log_every_request():
    try:
        path = request.path
        method = request.method
        headers = dict(request.headers)

        # Try all possible body formats
        body = request.get_json(silent=True)
        if body is None and request.form:
            body = request.form.to_dict()
        if body is None:
            raw_body = request.data.decode(errors='ignore') or ""
            body_str = raw_body
            # Extract username from raw string using regex
            match = re.search(r"username=([a-zA-Z0-9_+-]+)", raw_body)
            username = match.group(1) if match else ""
        else:
            body_str = json.dumps(body, indent=2)
            username = body.get("username", "").strip()

        # Logging to Discord
        log_to_discord(
            f"📨 **{method} {path}**\n"
            f"📍 Path: `{path}`\n"
            f"🧾 Headers: ```json\n{json.dumps(headers, indent=2)}\n```\n"
            f"📦 Body: ```json\n{body_str}\n```"
        )

        # Check whitelist
        if username not in WHITELIST_USERS:
            log_to_discord(f"❌ Blocked `{username}` — not whitelisted.")
            return jsonify({"error": "You are not whitelisted BAHAHAHHA FAGGOT."}), 403

    except Exception as e:
        print(f"[Request Log Error] {e}")

# Helper functions

def generate_random_username():
    return 'Xera+' + ''.join(random.choices(string.ascii_uppercase, k=6))

def generate_custom_id():
    return ''.join(random.choices(string.digits, k=17))

def b64encode_json(obj):
    return base64.urlsafe_b64encode(json.dumps(obj).encode()).decode().rstrip('=')

def generate_jwt_token(user_id):
    header = {'alg': 'HS256', 'typ': 'JWT'}
    now = int(time.time())
    payload = {
        'tid': secrets.token_hex(16),
        'uid': user_id,
        'usn': secrets.token_hex(5),
        'vrs': {
            'authID': secrets.token_hex(20),
            'clientUserAgent': 'MetaQuest 1.2.0_731_54fb75be9',
            'deviceID': secrets.token_hex(20),
            'loginType': 'meta_quest'
        },
        'exp': now + 72000,
        'iat': now
    }
    signature = secrets.token_urlsafe(32)
    return f"{b64encode_json(header)}.{b64encode_json(payload)}.{signature}"

def generate_auth_tokens():
    user_id = secrets.token_hex(16)
    return {
        'token': generate_jwt_token(user_id),
        'refresh_token': generate_jwt_token(user_id)
    }


# Minimal user data for storage responses
USER_DATA_RESPONSE = {
    'objects': [
        {
            'collection': 'user_avatar',
            'key': '0',
            'user_id': '2e8aace0-282d-4c3d-b9d4-6a3b3ba2c2a6',
            'value': json.dumps({
                "butt": "bp_butt_gorilla",
                "head": "bp_head_gorilla",
                "tail": "",
                "torso": "bp_torso_gorilla",
                "armLeft": "bp_arm_l_gorilla",
                "eyeLeft": "bp_eye_gorilla",
                "armRight": "bp_arm_r_gorilla",
                "eyeRight": "bp_eye_gorilla",
                "accessories": ["acc_fit_varsityjacket"],
                "primaryColor": "604170"
            }),
            'version': '7a326a2a4d0639a5f08e3116bb99a3bf',
            'permission_read': 2,
            'create_time': '2024-10-29T00:22:08Z',
            'update_time': '2025-04-04T03:55:19Z'
        }
    ]
}

DEFAULT_USER_RESPONSE = {
    'user': {
        'id': '2e8aace0-282d-4c3d-b9d4-6a3b3ba2c2a6',
        'username': 'ERROR',
        'lang_tag': 'en',
        'metadata': '{}',
        'edge_count': 4,
        'create_time': '2024-08-24T07:30:12Z',
        'update_time': '2025-04-05T21:00:27Z'
    },
    'wallet': json.dumps({
        "stashCols": 4,
        "stashRows": 2,
        "hardCurrency": 999999999999,
        "softCurrency": 999999999999,
        "researchPoints": 999999999999
    }),
    'custom_id': '26344644298513663'
}

STATIC_AUTH_TOKENS = {
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI3OGU0NDBiOS00NWZjLTRhODYtOTllMy02ZGM5Y2RjN2M1N2UiLCJ1aWQiOiJmM2E1NjE4YS1hMzNmLTQyMDAtYThiYS1lYjM3YzdiZmJmOWMiLCJ1c24iOiJ4ZW5pdHl5dCIsInZycyI6eyJhdXRoSUQiOiJkYTEzZjU4YzJiMjU0ZTgwYTM5YzA3YzRlNzkyNjlmOSIsImNsaWVudFVzZXJBZ2VudCI6Ik1ldGFRdWVzdCAxLjE2LjMuMTEzOF81ZWRjYmQ5OCIsImRldmljZUlEIjoiMTcyZjZjMmU3MWE5NGMwMTBjMWY2Mjk5OWJjM2QzMjEiLCJsb2dpblR5cGUiOiJtZXRhX3F1ZXN0In0sImV4cCI6MTc0NDA2MzQwNiwiaWF0IjoxNzQzOTk0MzE4fQ.nRJLbep6nCGeBTwruOunyNjDUiLxfcvpAJHl7E6n3m8',
    'refresh_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI3OGU0NDBiOS00NWZjLTRhODYtOTllMy02ZGM5Y2RjN2M1N2UiLCJ1aWQiOiJmM2E1NjE4YS1hMzNmLTQyMDAtYThiYS1lYjM3YzdiZmJmOWMiLCJ1c24iOiJ4ZW5pdHl5dCIsInZycyI6eyJhdXRoSUQiOiJkYTEzZjU4YzJiMjU0ZTgwYTM5YzA3YzRlNzkyNjlmOSIsImNsaWVudFVzZXJBZ2VudCI6Ik1ldGFRdWVzdCAxLjE2LjMuMTEzOF81ZWRjYmQ5OCIsImRldmljZUlEIjoiMTcyZjZjMmU3MWE5NGMwMTBjMWY2Mjk5OWJjM2QzMjEiLCJsb2dpblR5cGUiOiJtZXRhX3F1ZXN0In0sImV4cCI6MTc0NDE0NjIwNiwiaWF0IjoxNzQzOTk0MzE4fQ.f7nTHNnPrJW6oYYo54RDks1iDvntTP2yiBfpHdH-ygQ'
}

CLIENT_BOOTSTRAP_RESPONSE = {
    'payload': json.dumps({
        "updateType": "Optional",
        "attestResult": "Valid",
        "attestTokenExpiresAt": 1820877961,
        "photonAppID": PhotonAppId,
        "photonVoiceAppID": PhotonVoiceAppId,   # <-- COMMA HERE
        "termsAcceptanceNeeded": [],
        "dailyMissionDateKey": [],
        "dailyMissions": None,
        "dailyMissionResetTime": 0,
        "serverTimeUnix": 1720877961,
        "gameDataUrl": ProdZipFile
    })
}
# https://backend.xmodding.org/Auth
# MetaQuest 1.1.0.755_cc43b478
Auth69 = ""
USERIDFORME = "28367912736155594"
USERNAMEFORME = "<color=red>MOON COMPANY USER</color>"
username5 = "<size=0.5><color=red>MC</color></size>: "
usersystem = ""
owners = "iKDO.19"
ContentCreator = "GxlxcticVR"
Auth156 = "Basic NlVSdVRTbERLS2ZZYnVEVzo="
# sex =         data = request.get_data()


@app.route('/v2/account/link/device', methods=['POST'])
def link_device():
    data = request.get_json()
    Authorization = data.get("Authorization")
    return jsonify({
        'id': secrets.token_hex(16),
        'user_id': '13b8dce4-2c8e-4945-90b6-19af0c2b0ad7',
        'linked': True,
        'create_time': '2025-01-15T18:08:45Z'
    })

# Routes
@app.route('/v2/rpc/clientBootstrap', methods=['GET', 'POST'])
def client_bootstrap():
    return jsonify(CLIENT_BOOTSTRAP_RESPONSE)

@app.route('/game-data-prod.zip')
def serve_game_data():
    r = requests.get(GITHUB_ZIP_URL)
    if r.status_code == 200:
        return Response(
            r.content,
            mimetype='application/zip',
            headers={'Content-Disposition': 'attachment; filename=game-data-prod.zip'}
        )
    return {'error': 'File not found'}, 404

@app.route('/v2/account', methods=['GET', 'POST', 'PUT'])
def account():
    return jsonify({
        'user': {
             'id': secrets.token_hex(16),
             'username': username5 + secrets.token_hex(5),
             'lang_tag': 'en',
             'metadata': json.dumps({'isDeveloper': True}),
             'edge_count': 4,
             'create_time': '2024-08-24T07:30:12Z',
             'update_time': '2025-04-05T21:00:27Z'
         },
         'wallet': {
             "stashCols": 16, "stashRows": 8,
             "hardCurrency": 0,
             "softCurrency": 20000000,
             "researchPoints": 69420
         },
         'custom_id': generate_custom_id()
     })



@app.route('/v2/storage', methods=['GET', 'POST'])
def storage():
    if request.method == 'POST':
        data = request.get_json(force=True)
        Authorization = data.get("Authorization")
        user_objects = data.get('objects', [])
        return jsonify(user_objects), 200

@app.route('/v2/account/authenticate/custom', methods=['POST', 'GET'])
def authenticate_custom():
    return jsonify(generate_auth_tokens())



@app.route('/v2/account1', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def account1():
    return jsonify(DEFAULT_USER_RESPONSE)

@app.route('/v2/rpc/purchase.avatarItems', methods=['POST'])
def purchase_avatar_items():
    return jsonify({'payload': ''})

@app.route('/v2/rpc/avatar.update', methods=['POST'])
def update_avatar():
    return jsonify({'payload': ''})

@app.route('/v2/rpc/purchase.gameplayItems', methods=['POST'])
def purchase_gameplay_items():
    return jsonify({'payload': ''})



@app.route("/v2/storage/econ_gameplay_items", methods=["GET", "POST"])
def gameplayitems():
    github_url = "https://raw.githubusercontent.com/wewewer4fteeeeeee/fuv/main/modded/econ_gameplay_items.json"

    try:
        response = requests.get(github_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return jsonify({"objects": data})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch from GitHub: {str(e)}"}), 500



@app.route("/econ/items", methods=["GET"])
def get_econ_items():
    """Fetch econ_gameplay_items.json from GitHub"""
    github_url = "https://raw.githubusercontent.com/wewewer4fteeeeeee/fuv/main/modded/econ_gameplay_items.json"

    try:
        response = requests.get(github_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch from GitHub: {str(e)}"}), 500


@app.route('/v2/rpc/mining.balance', methods=['GET'])
def mining_balance():
    response_body = {
        'payload': json.dumps({
            'hardCurrency': 20000000,
            'researchPoints': 999999
        })
    }
    return jsonify(response_body), 200

@app.route('/v2/rpc/purchase.list', methods=['GET'])
def purchase_list():
    response_body = {
        'payload': json.dumps({
            'purchases': [
                {
                    'user_id': '13b8dce4-2c8e-4945-90b6-19af0c2b0ad7',
                    'purchase_time': {'seconds': 1741450711},
                    'create_time': {'seconds': 1741450837, 'nanos': 694669000},
                    'update_time': {'seconds': 1741450837, 'nanos': 694669000},
                    'metadata': '{}',
                    'id': 'dcbde23c-63cc-4c2a-bbc7-dc89ab5b63e6',
                    'purchase_id': 'p12345',
                    'purchase_source': 'meta_quest',
                    'payment_status': 'PAID',
                    'transaction_id': 'txn_001',
                    'product_id': 'prod_001',
                    'amount': 200,
                    'currency_code': 'USD',
                    'revenue': 200,
                    'app_store': 'Oculus'
                }
            ]
        })
    }
    return jsonify(response_body)


