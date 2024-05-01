from flask import Flask, request, jsonify, render_template
import base64
import requests
from dotenv import load_dotenv
import os
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client.get_database("Recipe")
    collection = db.get_collection("images")

    @app.route("/")
    def hello_world():
        return render_template("index.html")

    @app.route("/upload", methods=["POST"])
    def upload_image():
        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files["file"]
        image_data = file.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {openai_api_key}"}
        payload = {
            "model": "gpt-4-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Based on the ingredients in the image, can you suggest a recipe?"},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
                    ],
                }
            ],
            "max_tokens": 300,
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response_json = response.json()
        choices = response_json.get('choices')
        if choices is not None:
             collection.insert_one({"image": base64_image, "recipe": response_json['choices'][0]['message']['content']})
        else:
            collection.insert_one({"image": base64_image, "recipe": "No recipe found"})
        return jsonify({"response": response_json['choices'][0]['message']}), 200
    

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)  

