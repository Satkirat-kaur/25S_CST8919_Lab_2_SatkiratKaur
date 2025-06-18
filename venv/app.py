from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='login.log', level=logging.INFO)

@app.route('/')
def index():
    return 'Welcome to the secure login page!'

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'admin123':
        logging.info(f"Successful login: {username}")
        return {'message': 'Login successful'}
    else:
        logging.warning(f"Failed login: {username}")
        return {'message': 'Login failed'}, 401

if __name__ == '__main__':
    app.run()
