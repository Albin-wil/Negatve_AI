from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = 'sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # Replace with your key

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_reply = response.choices[0].message['content']
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": "⚠️ Error: " + str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
