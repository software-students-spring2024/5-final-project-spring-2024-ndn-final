from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import base64
import requests
from dotenv import load_dotenv
import os
import pymongo


app = Flask(__name__)
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
connectionn = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
dbn = os.getenv("MONGO_DB", "pictures")
connection = pymongo.MongoClient(connectionn)
db = connection[dbn]

@app.route("/")
def hello_world():
    return render_template("index.html")


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        print("decoding")
        return base64.b64encode(image_file.read()).decode("utf-8")


@app.route("/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    image_data = file.read()
    base64_image = base64.b64encode(image_data).decode('utf-8')
    result = db.pics.insert_one({"image": base64_image})
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {openai_api_key}"}
    payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image?"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                ],
            }
        ],
        "max_tokens": 300,
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response_json = response.json()
    db.pics.update_one({"image": base64_image}, {"$set": {"response": response_json['choices'][0]['message']['content']}})
    return response.json(), 200


if __name__ == "__main__":
    app.run(debug=False)
