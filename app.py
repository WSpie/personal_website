from flask import Flask, request, jsonify
from flask_cors import CORS

import utils
from utils.logger import Logger

import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app)

