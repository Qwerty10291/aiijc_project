from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def image_handler():
    print(len(request.files))
    return jsonify([{'status': 'OK', 'result': 'тут будет тестовый результат', 'name': name, 'filename': file.filename} for name, file in request.files.items()])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('localhost', port=5000)