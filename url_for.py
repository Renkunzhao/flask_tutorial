from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return url_for('index') + 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

# @app.route(url_for('static', filename='style.css'))
# def static():
#     return "static"
    

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))