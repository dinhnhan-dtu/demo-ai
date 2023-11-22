from flask import Flask, request, jsonify
from decouple import config
from openai import OpenAI

# Lấy API key từ biến môi trường
# export OPENAI_API_KEY='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'
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

    # Kiểm tra xem 'choices' có tồn tại trong response hay không
    if 'choices' in response:
        # Kiểm tra xem danh sách 'choices' có ít nhất một phần tử hay không
        if len(response['choices']) > 0:
            # Lấy giá trị 'text' từ phần tử đầu tiên của danh sách
            model_answer = response['choices'][0].get('text', '').strip()
            # Làm bất kỳ xử lý nào khác bạn cần với 'model_answer'
        else:
            model_answer = "No choices available in the response"
    else:
        model_answer = "No 'choices' field in the response"

    return jsonify({'answer': model_answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)