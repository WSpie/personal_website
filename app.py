from flask import Flask, request, jsonify, send_from_directory, redirect, url_for, render_template
from flask_cors import CORS
from argparse import ArgumentParser
from time import time

import utils
from utils.logger import Logger
from utils.gpt_init import login

import warnings
warnings.filterwarnings('ignore')

parser = ArgumentParser()
parser.add_argument('--username', default=f'user_{int(time())}')
opt = parser.parse_args()

logger = Logger(opt.username)

app = Flask(opt.username, template_folder='apps/templates', static_folder='apps/static')
CORS(app)

@app.route('/') #https://wspie.github.io/personal_website/
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            username = request.form['username']
            token = request.form['token']
            # You can handle the token and username here as needed
            return redirect(f'/gpt_api_play?username={username}')
        else:
            return render_template('login.html')
    except Exception as e:
        print(e)

@app.route('/gpt_api_play')
def gpt_api_play():
    username = request.args.get('username')
    return render_template('gpt_api_play.html', username=username)

@app.route('/test')
def test_route():
    return 'This is a test route'


if __name__ == '__main__':
    app.run(debug=True)