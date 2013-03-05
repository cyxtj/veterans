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
    sizheninfoList = []
    sizheninfoList.append({})
    sizheninfoList.append({})
    
    data = models.ChineseDisease.data()
    for (i, sizheninfo) in enumerate(data):
        print i, sizheninfo
        sizheninfoList[i]["patientID"] = sizheninfo.code
        print sizheninfoList[i]["patientID"]
        sizheninfoList[i]["patientName"] = sizheninfo.name
        sizheninfoList[i]["connectedState"] = True
        sizheninfoList[i]["connectedAddinfoID"] = None
        print sizheninfoList[i]
    return json.dumps(sizheninfoList)
