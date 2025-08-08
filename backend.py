import json
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
import uuid
from flask import Flask, request, jsonify, make_response
from supabase import create_client

# black
ProdZipFile = "https://github.com/FreakyUnity/moddedanimalcompany/raw/refs/heads/main/game-data-prod.zip"
DILDOPENIS = "https://github.com/FreakyUnity/moddedanimalcompany/raw/refs/heads/main/game-data-prod/econ_gameplay_items"
HalloweenPhotonAppId = "c8e2df68-0b36-4e3a-9811-54e44b4dd51a"
HalloweenPhotonVoiceAppId = "9e1343a4-a530-40ce-b1eb-b91833a3231d"
WinterPhotonAppId1 = "c8e2df68-0b36-4e3a-9811-54e44b4dd51a"
WinterPhotonVoiceAppId1 = "9e1343a4-a530-40ce-b1eb-b91833a3231d"
DATABASE_PASSWORDNOTREQUIRED = "MOONCOMPANYAPI69"
fuckalex = ["alexshorts", "alex_shorts1", "alex_shorts2", "Kelponline", "sxhadow"]
Supaurl = "https://tsppljulusbducdxczxa.supabase.co"
Supatable = "Storage"
Supatable2 = "userprof"
Supakey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzcHBsanVsdXNiZHVjZHhjenhhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMxODYwNzEsImV4cCI6MjA2ODc2MjA3MX0.J0wXrSIQffjo8TTFvwKH2VIRzR7QO7IzmAMTvQJI7uQ"
dihhcord = "https://discord.com/api/webhooks/1399808123757264926/Loz-e795u3V3uzgIS0YLZa4JwV4adBI1OFSVRvTS909QRSWl5jgIAScB4aCBWGfGZ4Zp"
supabase = create_client(Supaurl, Supakey)
dih = r"C:\Users\konys\AppData\Local\CapCut\Videos\beriumprivate-main\cooliostuff"
dih2 = r"C:\Users\konys\AppData\Local\CapCut\Videos\beriumprivate-main\cavedata"
REAL_BACKEND_URL = "https://your.real.meta.backend.url/v2/rpc/clientBootstrap"
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI4ZGQ5NmM5Yi0yNGVkLTRmZTEtOGRkOC1hNDM4MWIwMzI2MWEiLCJ1aWQiOiI5ZDNiY2FhZS1jMjA2LTQ3OTktYWVjMi0xNDZhY2ZiM2I2NjIiLCJ1c24iOiJleHBsb2RpbmdfY2FyIiwidnJzIjp7ImF1dGhJRCI6IjI1YTY0MDU4YzRhMzQ4YTA4MjFmNWVlZWY5MjUzNzVkIiwiY2xpZW50VXNlckFnZW50IjoiTWV0YVF1ZXN0IDEuMzQuMS4xNTUzX2VjZjE4MDZjIiwiZGV2aWNlSUQiOiI0ZWNhMzI4YWUzN2FkMWY0ZmQ2YTYyMjM0Y2RkZDZkYiIsImxvZ2luVHlwZSI6Im1ldGFfcXVlc3QifSwiZXhwIjoxNzU0NjU3MzAwLCJpYXQiOjE3NTQ2NTM3MDB9.fp4WiFGHNtZEJPm0M3k2xK9rkFvrsq2PtpmlwNR0qlE"
app = Flask(__name__)

GITHUB_ZIP_URL = "https://github.com/FreakyUnity/moddedanimalcompany/raw/refs/heads/main/zombies/game-data-prod/game-data-prod.zip"

def log_to_discord(message: str):
    try:
        requests.post(dihhcord, json={"content": message})
    except Exception as e:
        print(f"[Webhook Error] {e}")

@app.before_request
def log_every_request():
    try:
        headers = dict(request.headers)
        path = request.path
        body = request.get_json(silent=True)
        if body is None and request.form:
            body = request.form.to_dict()
        if body is None:
            body = request.data.decode(errors='ignore') or "(empty)"
        else:
            body = json.dumps(body, indent=2)

        log_to_discord(
            f"📨 **{request.method} {path}**\n"
            f"📍 Path: `{path}`\n"
            f"🧾 Headers: ```json\n{json.dumps(headers, indent=2)}\n```\n"
            f"📦 Body: ```json\n{body}\n```"
        )
    except Exception as e:
        print(f"[Request Log Error] {e}")

# Helper functions

localuserid = secrets.token_hex(16)

def generate_random_username():
    return 'Xera+' + ''.join(random.choices(string.ascii_uppercase, k=6))

def b64encode_json(obj):
    return base64.urlsafe_b64encode(json.dumps(obj).encode()).decode().rstrip('=')

def racism():
    secrets.token_hex(16)

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

Usernamez = ""
# Minimal user data for storage responses
sexoffending = {
    'objects': [
        {
            'collection': 'user_avatar',
            'key': '0',
            'user_id': localuserid,
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

newgenresponse1 = {
    'user': {
        'id': localuserid,
        'username': "OWNER",
        "display_name": "<color=red>OWNER</color>",
        'lang_tag': 'en',
        'metadata': {'isDeveloper': True},
        'edge_count': 4,
        'create_time': '2024-08-24T07:30:12Z',
        'update_time': '2025-04-05T21:00:27Z'
    },
    'wallet': {
        "stashCols": 4,
        "stashRows": 2,
        "hardCurrency": 999999999999,
        "softCurrency": 100000,
        "researchPoints": 999999999999
    },
    'custom_id': localuserid
}

def newgenresponse():
    return {
        'user': {
            'id': localuserid,
            'username': "player",
            "display_name": "player",
            'lang_tag': 'en',
            'metadata': {'isDeveloper': True},
            'edge_count': 4,
            'create_time': '2024-08-24T07:30:12Z',
            'update_time': '2025-04-05T21:00:27Z'
        },
        'wallet': {
            "stashCols": 4,
            "stashRows": 2,
            "hardCurrency": 999999999999,
            "softCurrency": 1000000000,
            "researchPoints": 999999999999
        },
        'custom_id': localuserid
    }

dihhatabase = 'db.json' 

if not os.path.exists(dihhatabase):
    with open(dihhatabase, 'w') as f:
        json.dump({"usernames": []}, f)

@app.route('/validateOculus', methods=['GET', 'POST'])
def validate_oculus():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        with open(dihhatabase, 'r') as f:
            db = json.load(f)
    except Exception as e:
        return jsonify({"error": f"Failed to read database: {str(e)}"}), 500

    if "usernames" not in db:
        db["usernames"] = []

    if username not in db["usernames"]:
        db["usernames"].append(username)
        try:
            with open(dihhatabase, 'w') as f:
                json.dump(db, f, indent=2)
        except Exception as e:
            return jsonify({"error": f"Failed to write database: {str(e)}"}), 500

    return jsonify({
        "message": "Thanks for participating in the early access, your oculus account has access now!!!!"
    })



def websitehtml():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>Moon Company Tools</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet"/>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: 'Inter', sans-serif;
            }

            body {
                background-color: #0e0e0e;
                color: white;
                padding: 2rem;
                text-align: center;
            }

            h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }

            nav {
                display: flex;
                justify-content: center;
                gap: 1rem;
                margin-bottom: 2rem;
            }

            .tab-button {
                padding: 10px 20px;
                background: #1a1a1a;
                border: 1px solid #333;
                border-radius: 8px;
                cursor: pointer;
                color: white;
                font-weight: 600;
                transition: background 0.3s;
            }

            .tab-button:hover {
                background: #2b2b2b;
            }

            .tab-content {
                display: none;
                margin-top: 2rem;
                max-width: 700px;
                margin-left: auto;
                margin-right: auto;
                text-align: left;
            }

            .tab-content.active {
                display: block;
            }

            .card {
                background: #1a1a1a;
                border-radius: 10px;
                padding: 1.5rem 2rem;
                box-shadow: 0 0 10px rgba(0,0,0,0.5);
            }

            .status-row {
                display: flex;
                justify-content: space-between;
                margin: 0.8rem 0;
            }

            .green-dot {
                width: 10px;
                height: 10px;
                background-color: #00e676;
                border-radius: 50%;
                display: inline-block;
                margin-right: 6px;
            }

            input[type="text"] {
                width: 100%;
                padding: 12px;
                background: #1a1a1a;
                border: 1px solid #333;
                border-radius: 8px;
                color: #fff;
                margin-bottom: 16px;
            }

            button {
                background: #222;
                border: 1px solid #444;
                color: #fff;
                padding: 12px 24px;
                border-radius: 8px;
                cursor: pointer;
                transition: background 0.3s;
                font-size: 1rem;
                font-weight: 600;
            }

            button:hover {
                background: #333;
            }

            .footer {
                font-size: 0.95rem;
                color: #aaa;
                margin-top: 1.5rem;
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
                word-wrap: break-word;
            }

            .footer span {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                flex-wrap: wrap;
                text-align: center;
            }

            a {
                color: #00e676;
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }

            .warning {
                color: #ff5252;
                font-weight: bold;
                margin-bottom: 10px;
            }

            #zombie-msg {
                margin-top: 10px;
                color: #aaa;
            }
        </style>
    </head>
    <body>
        <h1>Moon Company Tools</h1>
        <nav>
            <button class="tab-button" onclick="showTab('status')">Status</button>
            <button class="tab-button" onclick="showTab('zombie')">Zombie Beta</button>
        </nav>

        <!-- Status Tab -->
        <div class="tab-content active" id="status">
            <div class="card">
                <div class="status-row">
                    <strong>General Status</strong>
                    <span><span class="green-dot"></span>Online</span>
                </div>
                <hr style="border: 0; border-top: 1px solid #333;">
                <div class="status-row"><span>Version</span><span>1.1</span></div>
                <div class="status-row"><span>Last Updated</span><span>August 5, 2025</span></div>
                <div class="status-row"><span>API Status</span><span><span class="green-dot"></span>Online</span></div>
                <div class="footer">
                    <span>50k+ users</span>
                    <span>App Lab: <a href="https://www.meta.com/en-gb/experiences/h4k-tag/9887286787972745/" target="_blank">Meta Page</a></span>
                    <span>Discord: <a href="https://discord.gg/svEc5bBefJ" target="_blank">Join Here</a></span>
                </div>
            </div>
        </div>

        <!-- Zombie Beta Tab -->
        <div class="tab-content" id="zombie">
            <h2>ZOMBIE BETA</h2>
            <div class="warning">CASE SENSITIVE</div>
            <input type="text" id="zombieUsername" placeholder="Enter your Oculus username"/>
            <button onclick="validateZombie()">Submit</button>
            <div id="zombie-msg"></div>
        </div>

        <script>
            function showTab(tabId) {
                document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
                document.getElementById(tabId).classList.add('active');
            }

            async function validateZombie() {
                const username = document.getElementById("zombieUsername").value;
                const msg = document.getElementById("zombie-msg");

                if (!username.trim()) {
                    msg.textContent = "Please enter a username.";
                    return;
                }

                msg.textContent = "Validating...";

                try {
                    const res = await fetch(`/validateOculus?username=${encodeURIComponent(username)}`);
                    const data = await res.json();
                    msg.textContent = data.message || data.error || "Unknown response.";
                } catch (err) {
                    console.error(err);
                    msg.textContent = "An error occurred while validating.";
                }
            }
        </script>
    </body>
    </html>
    """




@app.route("/", methods=["GET", "POST"])
def nodeathythreaties():
    return websitehtml()


tspmo = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI3OGU0NDBiOS00NWZjLTRhODYtOTllMy02ZGM5Y2RjN2M1N2UiLCJ1aWQiOiJmM2E1NjE4YS1hMzNmLTQyMDAtYThiYS1lYjM3YzdiZmJmOWMiLCJ1c24iOiJ4ZW5pdHl5dCIsInZycyI6eyJhdXRoSUQiOiJkYTEzZjU4YzJiMjU0ZTgwYTM5YzA3YzRlNzkyNjlmOSIsImNsaWVudFVzZXJBZ2VudCI6Ik1ldGFRdWVzdCAxLjE2LjMuMTEzOF81ZWRjYmQ5OCIsImRldmljZUlEIjoiMTcyZjZjMmU3MWE5NGMwMTBjMWY2Mjk5OWJjM2QzMjEiLCJsb2dpblR5cGUiOiJtZXRhX3F1ZXN0In0sImV4cCI6MTc0NDA2MzQwNiwiaWF0IjoxNzQzOTk0MzE4fQ.nRJLbep6nCGeBTwruOunyNjDUiLxfcvpAJHl7E6n3m8'

STATIC_AUTH_TOKENS = {
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI3OGU0NDBiOS00NWZjLTRhODYtOTllMy02ZGM5Y2RjN2M1N2UiLCJ1aWQiOiJmM2E1NjE4YS1hMzNmLTQyMDAtYThiYS1lYjM3YzdiZmJmOWMiLCJ1c24iOiJ4ZW5pdHl5dCIsInZycyI6eyJhdXRoSUQiOiJkYTEzZjU4YzJiMjU0ZTgwYTM5YzA3YzRlNzkyNjlmOSIsImNsaWVudFVzZXJBZ2VudCI6Ik1ldGFRdWVzdCAxLjE2LjMuMTEzOF81ZWRjYmQ5OCIsImRldmljZUlEIjoiMTcyZjZjMmU3MWE5NGMwMTBjMWY2Mjk5OWJjM2QzMjEiLCJsb2dpblR5cGUiOiJtZXRhX3F1ZXN0In0sImV4cCI6MTc0NDA2MzQwNiwiaWF0IjoxNzQzOTk0MzE4fQ.nRJLbep6nCGeBTwruOunyNjDUiLxfcvpAJHl7E6n3m8',
    'refresh_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI3OGU0NDBiOS00NWZjLTRhODYtOTllMy02ZGM5Y2RjN2M1N2UiLCJ1aWQiOiJmM2E1NjE4YS1hMzNmLTQyMDAtYThiYS1lYjM3YzdiZmJmOWMiLCJ1c24iOiJ4ZW5pdHl5dCIsInZycyI6eyJhdXRoSUQiOiJkYTEzZjU4YzJiMjU0ZTgwYTM5YzA3YzRlNzkyNjlmOSIsImNsaWVudFVzZXJBZ2VudCI6Ik1ldGFRdWVzdCAxLjE2LjMuMTEzOF81ZWRjYmQ5OCIsImRldmljZUlEIjoiMTcyZjZjMmU3MWE5NGMwMTBjMWY2Mjk5OWJjM2QzMjEiLCJsb2dpblR5cGUiOiJtZXRhX3F1ZXN0In0sImV4cCI6MTc0NDE0NjIwNiwiaWF0IjoxNzQzOTk0MzE4fQ.f7nTHNnPrJW6oYYo54RDks1iDvntTP2yiBfpHdH-ygQ'
}

SupporterClientBootstrap = {
    'payload': json.dumps({
        "updateType": "Optional",
        "attestResult": "Valid",
        "attestTokenExpiresAt": 1820877961,
        "photonAppID": WinterPhotonAppId1,
        "photonVoiceAppID": WinterPhotonVoiceAppId1,   
        "termsAcceptanceNeeded": [],
        "dailyMissionDateKey": [],
        "dailyMissions": None,
        "dailyMissionResetTime": 0,
        "serverTimeUnix": 1720877961,
        "gameDataUrl": ProdZipFile
    })
}

WinterClientBootstrap2 = {
    'payload': json.dumps({
        "updateType": "Optional",
        "attestResult": "Valid",
        "attestTokenExpiresAt": 1820877961,
        "photonAppID": WinterPhotonAppId1,
        "photonVoiceAppID": WinterPhotonVoiceAppId1,   
        "termsAcceptanceNeeded": [],
        "dailyMissionDateKey": [],
        "dailyMissions": None,
        "dailyMissionResetTime": 0,
        "serverTimeUnix": 1720877961,
        "gameDataUrl": ProdZipFile
    })
}

SupporterClientBootstrap1 = {
    'payload': json.dumps({
        "updateType": "Optional",
        "attestResult": "Valid",
        "attestTokenExpiresAt": 1820877961,
        "photonAppID": WinterPhotonAppId1,
        "photonVoiceAppID": WinterPhotonVoiceAppId1,   
        "termsAcceptanceNeeded": [],
        "dailyMissionDateKey": [],
        "dailyMissions": None,
        "dailyMissionResetTime": 0,
        "serverTimeUnix": 1720877961,
        "gameDataUrl": ProdZipFile
    })
}

HalloweenClientBootstrap = {
    'payload': json.dumps({
        "updateType": "Optional",
        "attestResult": "Valid",
        "attestTokenExpiresAt": 1820877961,
        "photonAppID": HalloweenPhotonAppId,
        "photonVoiceAppID": HalloweenPhotonVoiceAppId, 
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
Supportlist = ["lix.810419", "parrot0870", "blockac", "robozeke5", "kewl.vr.2024", "italianbrainrotisstupid", "alex_shorts", "Xrenobys"]
Auth156 = "Basic NlVSdVRTbERLS2ZZYnVEVzo="

af1f = ""
# sex =         data = request.get_data()

Usernamez2 = ""
woah = "<color=red>you've been banned for:</color> being a dickhead and a whore and a bitch and a dirty ass cunt suck my dick if you're alex lmaoaoamaomaoa"
woah2 = ""

# CAVE LETS GOOOOOO

@app.route("/ssss/nakamacloud.c/v2/account/authenticate/custom", methods=["POST"])
def CaveDataauth2():
    b = request.get_data()
    userid1 = b['id'] 
    return jsonify(generate_jwt_token(userid1))

myoculus = ["exploding_car", "iKDO.19", "Hodded"]

@app.route("/nakamacloud.c/v2/account/authenticate/custom", methods=["POST", "GET"])
def CaveDataauth():
    global ussssssssssername
    us1sername = request.args.get("username")
    ussssssssssername = us1sername

    if us1sername in myoculus:
        return jsonify({
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI0YWMzN2YxOS1lMjA1LTQwOTYtYTZjMi04MjZlYjhhZTA3ZGYiLCJ1aWQiOiIzNTYwZmUyZS0wMTVjLTRkMmItYjJhNi02ZWI5ZjhkNmEyMzYiLCJ1c24iOiJza2lyZWZyIiwidnJzIjp7ImF1dGhJRCI6ImQyYzJlOTkyMTM2OTRkMzE4ZTUyM2Q2OWQ5YmUyOWZkIiwiY2xpZW50VXNlckFnZW50IjoiTWV0YVF1ZXN0IDEuMzIuMS4xNTE2Xzk2ZDZiOGI3IiwibG9naW5UeXBlIjoibWV0YV9xdWVzdCJ9LCJleHAiOjE3NTM1OTQ3ODAsImlhdCI6MTc1MzU5MTE4MH0.WdErpQIzAAlfnT-lnn0Ik49MQi47iuZn-zx6NJKqnxA"
        }), 200
    else:
        return jsonify("fetch account failed"), 403

# return {

@app.route("/sss/nakamacloud.c/v2/account/authenticate/custom", methods=["POST"])
def CaveDataauth1():
    global UUUsername
    username = request.args.get('username')
    UUUsername = username
    if not username:
        return jsonify({"error": "Username is required"}), 400

    try:
        with open(dihhatabase, 'r') as f:
            db = json.load(f)
    except Exception as e:
        return jsonify({"error": f"Failed to read database: {str(e)}"}), 500

    if "usernames" not in db:
        db["usernames"] = []

    if username not in db["usernames"]:
        db["usernames"].append(username)
        try:
            with open(dihhatabase, 'w') as f:
                json.dump(db, f, indent=2)
        except Exception as e:
            return jsonify({"error": f"Failed to write database: {str(e)}"}), 500
        return jsonify(generate_jwt_token(localuserid))
    

@app.route("/nakamacloud.c/v2/account/session/refresh", methods=["POST"])
def CaveDatarefresh():
    return {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI0YWMzN2YxOS1lMjA1LTQwOTYtYTZjMi04MjZlYjhhZTA3ZGYiLCJ1aWQiOiIzNTYwZmUyZS0wMTVjLTRkMmItYjJhNi02ZWI5ZjhkNmEyMzYiLCJ1c24iOiJza2lyZWZyIiwidnJzIjp7ImF1dGhJRCI6ImQyYzJlOTkyMTM2OTRkMzE4ZTUyM2Q2OWQ5YmUyOWZkIiwiY2xpZW50VXNlckFnZW50IjoiTWV0YVF1ZXN0IDEuMzIuMS4xNTE2Xzk2ZDZiOGI3IiwibG9naW5UeXBlIjoibWV0YV9xdWVzdCJ9LCJleHAiOjE3NTM1OTQ3ODAsImlhdCI6MTc1MzU5MTE4MH0.WdErpQIzAAlfnT-lnn0Ik49MQi47iuZn-zx6NJKqnxA",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI0YWMzN2YxOS1lMjA1LTQwOTYtYTZjMi04MjZlYjhhZTA3ZGYiLCJ1aWQiOiIzNTYwZmUyZS0wMTVjLTRkMmItYjJhNi02ZWI5ZjhkNmEyMzYiLCJ1c24iOiJza2lyZWZyIiwidnJzIjp7ImF1dGhJRCI6ImQyYzJlOTkyMTM2OTRkMzE4ZTUyM2Q2OWQ5YmUyOWZkIiwiY2xpZW50VXNlckFnZW50IjoiTWV0YVF1ZXN0IDEuMzIuMS4xNTE2Xzk2ZDZiOGI3IiwibG9naW5UeXBlIjoibWV0YV9xdWVzdCJ9LCJleHAiOjE3NTM1OTQ3ODAsImlhdCI6MTc1MzU5MTE4MH0.WdErpQIzAAlfnT-lnn0Ik49MQi47iuZn-zx6NJKqnxA",
}

@app.route("/nakamacloud.c/v2/rpc/user.getActiveSanctions", methods=["GET", "POST", "PUT"])
def cavedatasanctions():
    return {
        "payload": []
    }

@app.route("/nakamacloud.c/v2/account", methods=["GET", "POST", "PUT"])
def CaveDataaccount():
    return {
        "user": {
            "id": localuserid,
            "username": ussssssssssername,
            "display_name": ussssssssssername,
            "lang_tag": "en",
            "metadata": {'isDeveloper': True},
            "edge_count": 199,
            "create_time": "2024-08-24T04:20:56Z",
            "update_time": "2025-07-25T18:41:17Z"
        },
        "wallet": {'stashCols': 16, 'stashRows': 16, 'hardCurrency': 10000, 'softCurrency': 10000, 'researchPoints': 10000},
        "custom_id": secrets.token_hex(4)
    }

@app.route("/nakamacloud.c/v2/storage", methods=["GET", "POST", "PUT"])
def CaveDatastorage():
    b = json.loads(request.get_data().decode('utf-8', errors='replace'))
    for objecta in b["object_ids"]:
        if objecta["collection"] == 'user_avatar' and objecta["key"] == '0':
            return {
                "objects": [
                    {
                        "collection": "user_avatar",
                        "key": "0",
                        "user_id": "00000000-0000-0000-0000-000000000000",
                        "value": {'butt': 'bp_butt_bigbutt_galaxy', 'head': 'bp_head_cat', 'tail': 'bp_tail_cat', 'torso': "bp_torso_gorilla", 'armLeft': 'bp_arm_l_skeletongorilla', 'eyeLeft': 'bp_eye_polarbear', 'armRight': 'bp_arm_r_skeletongorilla', 'eyeRight': 'bp_eye_polarbear', 'accessories': ['acc_fit_early_bird_tshirt', 'acc_head_mop', 'bp_eye_lenseyes'], 'primaryColor': '000000'},
                        "version": "0a9e8f4c4b6b166a1a7650033d5f11c7",
                        "permission_read": 2,
                        "create_time": "2024-09-20T21:26:18Z",
                        "update_time": "2025-07-24T20:03:16Z"
                    }
                ]
            }
    return {}

app.route('/nakamacloud.c/v2/account/link/device', methods=['POST'])
def CaveDatalinkdevice():
    return jsonify({
        'id': secrets.token_hex(16),
        'user_id': localuserid,
        'linked': True,
        'create_time': '2025-01-15T18:08:45Z'
    })

@app.route("/nakamacloud.c/ws", methods=['GET', 'POST'])
def cavews():
    return "validated", 200

@app.route("/nakamacloud.c/v2/storage/econ_avatar_items", methods=["GET", "POST", "PUT"])
def CaveDataeconavataritems():
    ballsjr = os.path.join(dih2, "econ_avatar_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_avatar_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route('/nakamacloud.c/v2/rpc/attest.start', methods=['POST'])
def CaveDataatteststart():
    return jsonify({
        'payload': json.dumps({
            'status': 'success',
            'attestResult': 'Valid',
            'message': 'Attestation validated'
        })
    })

@app.route("/nakamacloud.c/v2/storage/econ_gameplay_items", methods=["GET", "POST", "PUT"])
def CaveDatagameplayitems():
    ballsjr = os.path.join(dih2, "econ_gameplay_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_gameplay_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/nakamacloud.c/v2/storage/econ_research_nodes", methods=["GET", "POST", "PUT"])
def CaveDataresearchnodes():
    ballsjr = os.path.join(dih2, "econ_research_nodes.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_research_nodes",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/nakamacloud.c/v2/storage/econ_products", methods=["GET", "POST", "PUT"])
def CaveDataeconproducts():
    ballsjr = os.path.join(dih2, "econ_products.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_products",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/nakamacloud.c/v2/storage/econ_stash_upgrades", methods=["GET", "POST", "PUT"])
def CaveDataeconstashupgrades():
    ballsjr = os.path.join(dih2, "econ_stash_upgrades.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_stash_upgrades",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

app.route("/nakamacloud.c/v2/storage/econ_loot_table_bindings", methods=["GET", "POST", "PUT"])
def CaveDataeconloottablebindings():
    ballsjr = os.path.join(dih2, "econ_loot_table_bindings.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_loot_table_bindings",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

app.route("/nakamacloud.c/v2/storage/econ_loot_table", methods=["GET", "POST", "PUT"])
def CaveDataeconloottable():
    ballsjr = os.path.join(dih2, "econ_loot_table.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_loot_table",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

app.route("/nakamacloud.c/v2/storage/econ_crafting_materials", methods=["GET", "POST", "PUT"])
def CaveDataeconcraftingmaterials():
    ballsjr = os.path.join(dih2, "econ_crafting_materials.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_crafting_materials",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

PhotonAppId1 = "84e5c139-ca02-495a-9031-2e76684b6271"
PhotonVoiceAppId1 = "52688ea6-5ea9-41e9-86f5-f9c53d723970"

PhotonAppId5 = "fd9600e2-f257-4cf7-96cf-058b2576fbae"
PhotonVoiceAppId5 = "f336a849-f518-46e1-aa34-add0e4289b38"

@app.route('/v2/rpc/clientBootstrap', methods=['POST'])
def proxy_bootstrap():
    body = request.get_json()

    # Forward the request to the real backend
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        resp = requests.post(REAL_BACKEND_URL, headers=headers, json=body)
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to contact real backend", "details": str(e)}), 502


@app.route('/nakamacloud.c/v2/rpc/mining.balance', methods=['GET'])
def CaveDataminingbalance():
    response_body = {
        'payload': json.dumps({
            'hardCurrency': 20000000,
            'researchPoints': 999999
        })
    }
    return jsonify(response_body), 200

@app.route('/nakamacloud.c/v2/rpc/purchase.list', methods=['GET'])
def CaveDatapurchaselist():
    response_body = {
        'payload': json.dumps({
            'purchases': [
                {
                    'user_id': localuserid,
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

# SUPPORTERSSSSS

@app.route("/ac/SSuuporter/v2/account/authenticate/custom", methods=["POST"])
def supporterauth():
    return jsonify(generate_jwt_token(localuserid))
    

@app.route("/ac/SSuuporter/v2/account/session/refresh", methods=["POST"])
def Suuporterrefresh():
    return {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI0YWMzN2YxOS1lMjA1LTQwOTYtYTZjMi04MjZlYjhhZTA3ZGYiLCJ1aWQiOiIzNTYwZmUyZS0wMTVjLTRkMmItYjJhNi02ZWI5ZjhkNmEyMzYiLCJ1c24iOiJza2lyZWZyIiwidnJzIjp7ImF1dGhJRCI6ImQyYzJlOTkyMTM2OTRkMzE4ZTUyM2Q2OWQ5YmUyOWZkIiwiY2xpZW50VXNlckFnZW50IjoiTWV0YVF1ZXN0IDEuMzIuMS4xNTE2Xzk2ZDZiOGI3IiwibG9naW5UeXBlIjoibWV0YV9xdWVzdCJ9LCJleHAiOjE3NTM1OTQ3ODAsImlhdCI6MTc1MzU5MTE4MH0.WdErpQIzAAlfnT-lnn0Ik49MQi47iuZn-zx6NJKqnxA",
        "refresh_token": generate_jwt_token(localuserid) }

@app.route("/ac/SSuuporter/v2/account", methods=["GET"])
def Suuporteraccount():
    diddy = request.get_json(silent=True)
    af1f = diddy.get("Username")
    return {
        "user": {
            "id": localuserid,
            "username": af1f,
            "display_name": af1f,
            "lang_tag": "en",
            "metadata": "{\"isDeveloper\": True}",
            "edge_count": 199,
            "create_time": "2024-08-24T04:20:56Z",
            "update_time": "2025-07-25T18:41:17Z"
        },
        "wallet": "{\"stashCols\": 8, \"stashRows\": 8, \"hardCurrency\": 1000000, \"softCurrency\": 1000000000, \"researchPoints\": 100000}",
        "custom_id": "26412155295098886"
    }

@app.route("/ac/SSuuporter/v2/storage", methods=["GET", "POST", "PUT"])
def Suuporterstorage():
    b = json.loads(request.get_data().decode('utf-8', errors='replace'))
    for objecta in b["object_ids"]:
        if objecta["collection"] == 'user_avatar' and objecta["key"] == '0':
            return {
                "objects": [
                    {
                        "collection": "user_avatar",
                        "key": "0",
                        "user_id": localuserid,
                        "value": "{\"butt\": \"bp_butt_bigbutt_galaxy\", \"head\": \"bp_head_cat\", \"tail\": \"bp_tail_cat\", \"torso\": \"\", \"armLeft\": \"bp_arm_l_skeletongorilla\", \"eyeLeft\": \"bp_eye_polarbear\", \"armRight\": \"bp_arm_r_skeletongorilla\", \"eyeRight\": \"bp_eye_polarbear\", \"accessories\": [\"acc_fit_early_bird_tshirt\", \"acc_head_mop\", \"bp_eye_lenseyes\"], \"primaryColor\": \"000000\"}",
                        "version": "0a9e8f4c4b6b166a1a7650033d5f11c7",
                        "permission_read": 2,
                        "create_time": "2024-09-20T21:26:18Z",
                        "update_time": "2025-07-24T20:03:16Z"
                    }
                ]
            }
    return {}

app.route('/ac/SSuuporter/v2/account/link/device', methods=['POST'])
def Suuporterlinkdevice():
    return jsonify({
        'id': secrets.token_hex(16),
        'user_id': localuserid,
        'linked': True,
        'create_time': '2025-01-15T18:08:45Z'
    })

@app.route("/ac/SSuuporter/v2/storage/econ_avatar_items", methods=["GET", "POST", "PUT"])
def Suuportereconavataritems():
    ballsjr = os.path.join(dih, "econ_avatar_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_avatar_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/ac/SSuuporter/v2/storage/econ_gameplay_items", methods=["GET", "POST", "PUT"])
def Suuportergameplayitems():
    ballsjr = os.path.join(dih, "econ_gameplay_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_gameplay_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/ac/SSuuporter/v2/storage/econ_research_nodes", methods=["GET", "POST", "PUT"])
def Suuporterresearchnodes():
    ballsjr = os.path.join(dih, "econ_research_nodes.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_research_nodes",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/ac/SSuuporter/v2/storage/econ_products", methods=["GET", "POST", "PUT"])
def Suuportereconproducts():
    ballsjr = os.path.join(dih, "econ_products.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_products",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route('/ac/SSuuporter/v2/rpc/clientBootstrap', methods=['GET', 'POST'])
def Suuporterbootstrap():
    return jsonify(SupporterClientBootstrap)

@app.route('/ac/SSuuporter/v2/rpc/mining.balance', methods=['GET'])
def Suuportermining_balance():
    response_body = {
        'payload': json.dumps({
            'hardCurrency': 20000000,
            'researchPoints': 999999
        })
    }
    return jsonify(response_body), 200

@app.route('/ac/SSuuporter/v2/rpc/purchase.list', methods=['GET'])
def Suuporterpurchase_list():
    response_body = {
        'payload': json.dumps({
            'purchases': [
                {
                    'user_id': localuserid,
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

@app.route("/Halloween/authenticate/Redo/Sigma", methods=['GET', 'POST'])
def test():
    usersexid = uuid.uuid4().hex
    sessionsexid = secrets.token_hex(16)
    return jsonify({
        "ResultCode": 1,
        "UserId": localuserid,
        "SessionId": sessionsexid,
        "Message": "Authenticated successfully"
    })

# winter thin

@app.route("/v2/account/session/refresh", methods=["POST"])
def refresh12():
    return {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0aWQiOiI0YWMzN2YxOS1lMjA1LTQwOTYtYTZjMi04MjZlYjhhZTA3ZGYiLCJ1aWQiOiIzNTYwZmUyZS0wMTVjLTRkMmItYjJhNi02ZWI5ZjhkNmEyMzYiLCJ1c24iOiJza2lyZWZyIiwidnJzIjp7ImF1dGhJRCI6ImQyYzJlOTkyMTM2OTRkMzE4ZTUyM2Q2OWQ5YmUyOWZkIiwiY2xpZW50VXNlckFnZW50IjoiTWV0YVF1ZXN0IDEuMzIuMS4xNTE2Xzk2ZDZiOGI3IiwibG9naW5UeXBlIjoibWV0YV9xdWVzdCJ9LCJleHAiOjE3NTM1OTQ3ODAsImlhdCI6MTc1MzU5MTE4MH0.WdErpQIzAAlfnT-lnn0Ik49MQi47iuZn-zx6NJKqnxA",
        "refresh_token": generate_jwt_token(localuserid)
    }

@app.route("/ws", methods=['GET', 'POST'])
def winterws():
    return "validated", 200

@app.route("/Halloween/ws", methods=['GET', 'POST'])
def halloweenws():
    return "validated", 200

@app.route("/ac/SSuuporter/ws", methods=['GET', 'POST'])
def Suuporterws():
    return "validated", 200


app.route('/v2/account/link/device', methods=['POST'])
def link_device12():
    return jsonify({
        'id': secrets.token_hex(16),
        'user_id': localuserid,
        'linked': True,
        'create_time': '2025-01-15T18:08:45Z'
    })

@app.route('/v2/rpc/clientBootstrap', methods=['GET', 'POST'])
def client_bootstrap21():
    return jsonify(HalloweenClientBootstrap)

@app.route('/v2/account', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def account244():
    Authorization = request.headers.get("Authorization", "")

    if request.method == 'GET':
        if Usernamez in fuckalex:
            return jsonify({"error": woah}), 403

        if "Bearer ey" in Authorization:
            return jsonify(newgenresponse()), 200
        else:
            return jsonify({"error": "No valid auth token"}), 403
    else:
        return jsonify(newgenresponse()), 200

# huge credits to skire / x6
@app.route("/v2/storage", methods=["GET", "POST", "PUT"])
def fake_storag12e():
    b = json.loads(request.get_data().decode('utf-8', errors='replace'))
    for objecta in b["object_ids"]:
        if objecta["collection"] == 'user_avatar' and objecta["key"] == '0':
            return {
                "objects": [
                    {
                        "collection": "user_avatar",
                        "key": "0",
                        "user_id": "00000000-0000-0000-0000-000000000000",
                        "value": "{\"butt\": \"bp_butt_bigbutt_galaxy\", \"head\": \"bp_head_cat\", \"tail\": \"bp_tail_cat\", \"torso\": \"\", \"armLeft\": \"bp_arm_l_skeletongorilla\", \"eyeLeft\": \"bp_eye_polarbear\", \"armRight\": \"bp_arm_r_skeletongorilla\", \"eyeRight\": \"bp_eye_polarbear\", \"accessories\": [\"acc_fit_early_bird_tshirt\", \"acc_head_mop\", \"bp_eye_lenseyes\"], \"primaryColor\": \"000000\"}",
                        "version": "0a9e8f4c4b6b166a1a7650033d5f11c7",
                        "permission_read": 2,
                        "create_time": "2024-09-20T21:26:18Z",
                        "update_time": "2025-07-24T20:03:16Z"
                    }
                ]
            }
    return jsonify("validated"), 200


@app.route('/v2/account/authenticate/custom', methods=['POST', 'GET'])
def authenticate_custom12():
    Usernamez = request.args.get("Username")
    return jsonify(generate_auth_tokens())

@app.route('/v2/user', methods=['GET', 'POST', 'PUT'])
def user21():
    return jsonify(newgenresponse)


@app.route('/v2/account1', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def account12():
    return jsonify(DEFAULT_USER_RESPONSE)

@app.route('/v2/rpc/avatar.update', methods=['POST'])
def update_avatar1():
    return jsonify(sexoffending), 200

@app.route('/v2/rpc/purchase.gameplayItems', methods=['POST'])
def purchase_gameplay_items1():
    return jsonify({'payload': ''})

@app.route('/v2/rpc/purchase.avatarItems', methods=['POST', 'GET'])
def penis68941():
    data = request.get_json()
    b = json.loads(data)
    if isinstance(b, dict):
        b['true'] = True
        b['none'] = False


@app.route('/v2/rpc/mining.balance', methods=['GET'])
def mining_balance():
    response_body = {
        'payload': json.dumps({
            'hardCurrency': 20000000,
            'researchPoints': 999999
        })
    }
    return jsonify(response_body), 200

@app.route("/v2/storage/econ_avatar_items", methods=["GET", "POST", "PUT"])
def neconavataritems():
    ballsjr = os.path.join(dih, "econ_avatar_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_avatar_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/v2/storage/econ_gameplay_items", methods=["GET", "POST", "PUT"])
def gameplayitems():
    ballsjr = os.path.join(dih, "econ_gameplay_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_gameplay_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/v2/storage/econ_research_nodes", methods=["GET", "POST", "PUT"])
def researchnodes():
    ballsjr = os.path.join(dih, "econ_research_nodes.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_research_nodes",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/v2/storage/econ_products", methods=["GET", "POST", "PUT"])
def econproducts():
    ballsjr = os.path.join(dih, "econ_products.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_products",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)


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

# halloween thin

@app.route('/Halloween/v2/account/link/device', methods=['POST'])
def Halloweenlink_device():
    return jsonify({
        'id': secrets.token_hex(16),
        'user_id': localuserid,
        'linked': True,
        'create_time': '2025-01-15T18:08:45Z'
    })

@app.route('/Halloween/v2/rpc/clientBootstrap', methods=['GET', 'POST'])
def Halloweenclient_bootstrap():
    return jsonify(HalloweenClientBootstrap)

@app.route('/Halloween/v2/account', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def Halloweenaccount24():
    Authorization = request.headers.get("Authorization", "")
    if request.method == 'GET':
        if Usernamez in fuckalex:
            return jsonify({"error": woah}), 403

        if "Bearer ey" in Authorization:
            return jsonify(newgenresponse()), 200
        else:
            return jsonify({"error": "No valid auth token"}), 403
    else:
        return jsonify(newgenresponse()), 200

def offendtheminorsbymakingthemangry():
    return ''.join(random.choices('0123456789ABCDEF', k=6))

@app.route("/Halloween/v2/storage", methods=["GET", "POST", "PUT"])
def halloweenstorage():
    b = json.loads(request.get_data().decode('utf-8', errors='replace'))
    for objecta in b.get("object_ids", []):
        if objecta.get("collection") == 'user_avatar' and objecta.get("key") == '0':
            randomcolor = offendtheminorsbymakingthemangry()
            return {
                "objects": [
                    {
                        "collection": "user_avatar",
                        "key": "0",
                        "user_id": localuserid,
                        "value": json.dumps(objecta),
                        "version": "0a9e8f4c4b6b166a1a7650033d5f11c7",
                        "permission_read": 2,
                        "create_time": "2024-09-20T21:26:18Z",
                        "update_time": "2025-07-24T20:03:16Z"
                    }
                ]
            }
    return {}

@app.route('/Halloween/v2/account/authenticate/custom', methods=['POST', 'GET'])
def Halloweenauthenticate_custom():
    return jsonify(generate_auth_tokens())

@app.route('/Halloween/v2/user', methods=['GET', 'POST', 'PUT'])
def Halloweenuser():
    return jsonify(newgenresponse())


@app.route('/Halloween/v2/account1', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def Halloweenaccount1():
    return jsonify(DEFAULT_USER_RESPONSE)

@app.route('/Halloween/v2/rpc/avatar.update', methods=['POST'])
def Halloweenupdate_avatar():
    return jsonify(sexoffending), 200

@app.route('/Halloween/v2/rpc/purchase.gameplayItems', methods=['POST'])
def Halloweenpurchase_gameplay_items():
    return jsonify({'payload': ''})

@app.route('/Halloween/v2/rpc/purchase.avatarItems', methods=['POST', 'GET'])
def Halloweenpenis6894():
    data = request.get_json()
    b = json.loads(data)
    if isinstance(b, dict):
        b['true'] = True
        b['none'] = False
@app.route("/Halloween/v2/storage/econ_avatar_items", methods=["GET", "POST", "PUT"])
def Halloweeneconavataritems():
    ballsjr = os.path.join(dih, "econ_avatar_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_avatar_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/Halloween/v2/storage/econ_gameplay_items", methods=["GET", "POST", "PUT"])
def Halloweengameplayitems():
    ballsjr = os.path.join(dih, "econ_gameplay_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_gameplay_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/Halloween/v2/storage/econ_research_nodes", methods=["GET", "POST", "PUT"])
def Halloweenresearchnodes():
    ballsjr = os.path.join(dih, "econ_research_nodes.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_research_nodes",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route('/Halloween/v2/rpc/mining.balance', methods=['GET'])
def Halloweenmining_balance():
    response_body = {
        'payload': json.dumps({
            'hardCurrency': 20000000,
            'researchPoints': 999999
        })
    }
    return jsonify(response_body), 200

@app.route("/Halloween/v2/storage/econ_products", methods=["GET", "POST", "PUT"])
def Halloweeneconproducts():
    ballsjr = os.path.join(dih, "econ_products.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_products",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route('/Halloween/v2/rpc/purchase.list', methods=['GET'])
def Halloweenpurchase_list():
    response_body = {
        'payload': json.dumps({
            'purchases': [
                {
                    'user_id': localuserid,
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

# halloween thin

@app.route('/HHalloween/v2/account/link/device', methods=['POST'])
def HHalloweenlink_device():
    return jsonify({
        'id': secrets.token_hex(16),
        'user_id': localuserid,
        'linked': True,
        'create_time': '2025-01-15T18:08:45Z'
    })

@app.route('/HHalloween/v2/rpc/clientBootstrap', methods=['GET', 'POST'])
def HHalloweenclient_bootstrap():
    return jsonify(HalloweenClientBootstrap)

@app.route('/HHalloween/v2/account', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def HHalloweenaccount24():
    Authorization = request.headers.get("Authorization", "")

    if request.method == 'GET':
        if Usernamez in fuckalex:
            return jsonify({"error": woah}), 403

        if "Bearer ey" in Authorization:
            return jsonify(newgenresponse1), 200
        else:
            return jsonify({"error": "No valid auth token"}), 403
    else:
        return jsonify(newgenresponse1), 200

@app.route("/HHalloween/v2/storage", methods=["GET", "POST", "PUT"])
def HHalloweenstorage():
    b = json.loads(request.get_data().decode('utf-8', errors='replace'))
    for objecta in b.get("object_ids", []):
        if objecta.get("collection") == 'user_avatar' and objecta.get("key") == '0':
            randomcolor = offendtheminorsbymakingthemangry()
            return {
                "objects": [
                    {
                        "collection": "user_avatar",
                        "key": "0",
                        "user_id": localuserid,
                        "value": f"""{{"butt": "bp_butt_bigbutt_galaxy", "head": "bp_head_gorilla", "torso": "bp_torso_gorilla", "armLeft": "bp_arm_l_skeletongorilla", "eyeLeft": "bp_eye_gorilla", "armRight": "bp_arm_r_skeletongorilla", "eyeRight": "bp_eye_gorilla", "accessories": "acc_head_mop", "primaryColor": "{randomcolor}"}}""",
                        "version": "0a9e8f4c4b6b166a1a7650033d5f11c7",
                        "permission_read": 2,
                        "create_time": "2024-09-20T21:26:18Z",
                        "update_time": "2025-07-24T20:03:16Z"
                    }
                ]
            }
    return {}

@app.route('/HHalloween/v2/account/authenticate/custom', methods=['POST', 'GET'])
def HHalloweenauthenticate_custom():
    return jsonify(generate_auth_tokens())

@app.route('/HHalloween/v2/user', methods=['GET', 'POST', 'PUT'])
def HHalloweenuser():
    return jsonify(newgenresponse1)


@app.route('/HHalloween/v2/account1', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def HHalloweenaccount1():
    return jsonify(DEFAULT_USER_RESPONSE)

@app.route('/HHalloween/v2/rpc/avatar.update', methods=['POST'])
def HHalloweenupdate_avatar():
    return jsonify(sexoffending), 200

@app.route('/HHalloween/v2/rpc/purchase.gameplayItems', methods=['POST'])
def HHalloweenpurchase_gameplay_items():
    return jsonify({'payload': ''})

@app.route('/HHalloween/v2/rpc/purchase.avatarItems', methods=['POST', 'GET'])
def HHalloweenpenis6894():
    data = request.get_json()
    b = json.loads(data)
    if isinstance(b, dict):
        b['true'] = True
        b['none'] = False
@app.route("/HHalloween/v2/storage/econ_avatar_items", methods=["GET", "POST", "PUT"])
def HHalloweeneconavataritems():
    ballsjr = os.path.join(dih, "econ_avatar_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_avatar_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route("/HHalloween/v2/storage/econ_gameplay_items", methods=["GET", "POST", "PUT"])
def HHalloweengameplayitems():
    ballsjr = os.path.join(dih, "econ_gameplay_items.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_gameplay_items",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route('/HHalloween/v2/rpc/mining.balance', methods=['GET'])
def HHalloweenmining_balance():
    response_body = {
        'payload': json.dumps({
            'hardCurrency': 20000000,
            'researchPoints': 999999
        })
    }
    return jsonify(response_body), 200

@app.route("/HHalloween/v2/storage/econ_products", methods=["GET", "POST", "PUT"])
def HHalloweeneconproducts():
    ballsjr = os.path.join(dih, "econ_products.json")
    with open(ballsjr, 'r', encoding='utf-8') as f:
        data = json.load(f) or []
    newdata = {"objects": []}
    for e in data:
        newdata["objects"].append({
            "collection": "econ_products",
            "key": e["id"],
            "user_id": "00000000-0000-0000-0000-000000000000",
            "value": json.dumps(e),
            "version": "5c8518bd84cdb43a4e057cb62ca8d5b1",
            "permission_read": 2,
            "create_time": "2025-05-28T16:03:59Z",
            "update_time": "2025-06-11T16:16:56Z"
        })

    return jsonify(newdata)

@app.route('/HHalloween/v2/rpc/purchase.list', methods=['GET'])
def HHalloweenpurchase_list():
    response_body = {
        'payload': json.dumps({
            'purchases': [
                {
                    'user_id': localuserid,
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
