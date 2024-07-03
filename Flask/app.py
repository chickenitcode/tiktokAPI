from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    tiktok_username = request.form['username']
    # Thêm logic để gọi API của TikTok ở đây
    # Ví dụ: response = requests.get(f'https://api.tiktok.com/{tiktok_username}')
    # Dữ liệu giả lập
    response = {'user': tiktok_username, 'followers': 1000}
    return render_template('index.html', data=response)

if __name__ == '__main__':
    app.run(debug=True)
