from flask import Flask, request, jsonify
import requests
import json
import hashlib
from datetime import datetime

app = Flask(__name__)

PLAYFAB_TITLE_ID = "1806A1"
PLAYFAB_SECRET_KEY = "IIHUI47SDEQOH67IRFG3M7UFE7XTQRUJFPYI97UO577ENO18Z3"
OCULUS_ID = "9735667116454066"

webhookUrl = ""
webhookUrl2 = ""

titleData = {}

def loadTitleDataFromFile():
    try:
        with open('titleData.json', 'r') as file:
            return json.load(file)
    except:
        return {}

def saveTitleDataToFile(data):
    with open('titleData.json', 'w') as file:
        json.dump(data, file, indent=2)

def md5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()

@app.route('/', methods=['GET'])
def get_title_data():
    return jsonify(titleData)

@app.route('/api/TitleData', methods=['POST'])
def get_title_dat():
    return jsonify(titleData)

@app.route('/', methods=['POST'])
def update_title_data():
    global titleData
    receivedData = request.json.get('data')
    titleData = receivedData
    saveTitleDataToFile(titleData)
    return jsonify({"message": "Data updated successfully"})

@app.route('/api/post/photon', methods=['POST'])
def photon_api():
    data = request.json
    if not data:
        return jsonify({"Error": "Missing JSON payload"}), 400

    user_id = data.get('Ticket', '').split('-')[0]
    data["UserId"] = user_id
    nonce = data.get("Nonce", "EMPTY")

    return jsonify({
        "ResultCode": 1,
        "StatusCode": 200,
        "Message": '',
        "result": 0,
        "UserId": user_id,
        "AppId": "live1.1.112",
        "Ticket": data['Ticket'],
        "Token": data['Token'],
        "Nonce": nonce
    })

@app.route('/api/PlayfabAuthenticate', methods=['POST'])
def playfabauth():
    data = request.json
    send_to_discord_webhook(data)
    if 'UserId' in data and 'Platform' in data:
        return jsonify({
            "ResultCode": 1,
            "UserId": data['UserId'],
            "Platform": data['Platform']
        })
    else:
        ban_info = {
            "BanReason": "dawg",
            "BanDuration": "0",
            "Timestamp": datetime.utcnow().isoformat()
        }
        return jsonify({"Error": "Forbidden", "Message": "Invalid data received", "BanInfo": ban_info}), 403

@app.route('/api/CachePlayFabId', methods=['POST'])
def cache_playfab_id():
    data = request.json
    send_to_discord_webhook(data)
    required_fields = ['Platform', 'SessionTicket', 'PlayFabId']
    if all(field in data for field in required_fields):
        return jsonify({"Message": "PlayFabId Cached Successfully"}), 200
    else:
        missing_fields = [field for field in required_fields if field not in data]
        return jsonify({"Error": "Missing Data", "MissingFields": missing_fields}), 400

def send_to_discord_webhook(log_data):
    if webhookUrl:
        content = f"Auth Post Data: \n```json\n{json.dumps(log_data, indent=2)}\n```"
        requests.post(webhookUrl, json={"content": content})

def send_to_discord_webhook2(nonce):
    if webhookUrl2:
        content = f"Nonce Is: \n```json\n{json.dumps(nonce, indent=2)}\n```"
        requests.post(webhookUrl2, json={"content": content})

# Don't run the server manually — expose it for Vercel
handler = app
