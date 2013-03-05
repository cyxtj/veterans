#coding=utf8

from flask import Flask

app = Flask(__name__)

#from app folder import views.py
from app import views


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8008, debug=True)
