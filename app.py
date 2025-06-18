from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return 'Welcome to the secure login page!'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'admin123':
        app.logger.info(f"Successful login: {username}")
        return {'message': 'Login successful'}
    else:
        app.logger.warning(f"Failed login: {username}")
        return {'message': 'Login failed'}, 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

