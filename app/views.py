#coding=utf8
import json
import flask.ext.restless
from flask import render_template
from model import models
from app import app


@app.route('/')
def index():
    return render_template("index.html")


manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=models.db)

preprocessor = {'GET_SINGLE':[models.drug.d_get_by_id],'GET_MANY':[models.drug.d_get_all]}

manager.create_api(models.drug, methods=['GET','POST','DELETE'], postprocessors = preprocessor)
manager.create_api(models.ChineseDisease, methods=['GET','POST','DELETE'])
manager.create_api(models.dCase, methods=['GET','POST','DELETE'])
manager.create_api(models.dMethod, methods=['GET','POST','DELETE'])
manager.create_api(models.dTemplate, methods=['GET','POST','DELETE'])
manager.create_api(models.fixedrecipe, methods=['GET','POST','DELETE'])
manager.create_api(models.semiotic, methods=['GET','POST','DELETE'])
manager.create_api(models.symptom, methods=['GET','POST','DELETE'])
manager.create_api(models.WesternDisease, methods=['GET','POST','DELETE'])
