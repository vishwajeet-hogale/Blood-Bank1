import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
from PIL import Image
from io import StringIO
import base64
import requests
import random

app = Flask(__name__)
CORS(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "Dbadbakbkcb232e3jasbkabs7cabjbc"

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/org_lander')
def org_lander():
    return render_template('orglander.html')

if __name__ == "__main__":
    app.run(debug=True)