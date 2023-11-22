from flask import Flask, request, jsonify
from decouple import config
from openai import OpenAI

# Lấy API key từ biến môi trường
api_key = config('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    user_question = data['question']

    # GPT-3 API call to generate a response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": user_question},
        ]
    )

    # Extract the generated answer from GPT-3 response
    model_answer = response['choices'][0]['text'].strip()

    return jsonify({'answer': model_answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)