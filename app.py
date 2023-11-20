from flask import Flask, request, jsonify
import openai  # Fix import statement

client = openai.OpenAI(api_key='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')

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    user_question = data['question']

    # GPT-3 API call to generate a response
    response = client.Completion.create(  # Fix method name
        engine="text-davinci-003",
        prompt=user_question,
        temperature=0.7,
        max_tokens=150
    )

    # Extract the generated answer from GPT-3 response
    model_answer = response['choices'][0]['text'].strip()

    return jsonify({'answer': model_answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)