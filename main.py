from flask import Flask, request, jsonify

app = Flask(__name__)

# DEMO DATABASE
db = {
    "123456789": "9781566283",
    "987654321": "9123456789"
}

@app.route("/")
def home():
    return "TG TO NUM API RUNNING"

@app.route("/api/tg")
def tg():

    chat_id = request.args.get("chat_id")

    number = db.get(chat_id)

    if number:
        return jsonify({
            "status": True,
            "chat_id": chat_id,
            "number": number
        })

    return jsonify({
        "status": False,
        "message": "NOT FOUND"
    })

app = app