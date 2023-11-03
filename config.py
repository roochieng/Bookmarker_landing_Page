import os
from flask import Flask, request



app = Flask(__name__, '/static')

app.secret_key = os.urandom(24)
