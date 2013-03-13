#coding=utf8
from model import models
#can't understand from what app??
from app import app
from flask import render_template
import json


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/sizheninfo')
def sizheninfo(): 
    return models.drug.get_all()
