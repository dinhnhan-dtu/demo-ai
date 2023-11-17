from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI GPT-3 API key
openai.api_key = 'YOUR_API_KEY'

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    user_question = data['question']

    # GPT-3 API call to generate a response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_question,
        temperature=0.7,
        max_tokens=150
    )

    # Extract the generated answer from GPT-3 response
    model_answer = response['choices'][0]['text'].strip()

    return jsonify({'answer': model_answer})

if __name__ == '__main__':
    app.run(port=5000)