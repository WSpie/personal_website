from flask import Flask, request, jsonify
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
app = Flask(opt.username)
CORS(app)

@app.route('https://wspie.github.io/personal_website/')
def index():
    return "Welcome to Lipai Huang's API!"

@app.route('/profile', methods=['GET'])
def profile():
    # Your code to handle profile request
    return jsonify({'message': 'Profile information'})

@app.route('/gpt-api-play', methods=['POST'])
def gpt_api_play():
    data = request.json
    # Your code to handle GPT API play request
    return jsonify({'result': 'GPT API result'})

if __name__ == '__main__':
    app.run(debug=True)