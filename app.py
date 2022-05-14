#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template,request,redirect,url_for
import api,os
import pandas as pd
DEVELOPMENT_ENV  = True

app = Flask(__name__)

app_data = {
    "name":         "OMS Tasarım BlockChain Uygulaması",
    "description":  "Açıkhack",
    "author":       "Mehmet Önder",
    "html_title":   "Açıkhack2022",
    "project_name": "Açıkhack2022",
    "keywords":     "Blockchain "
}

@app.route('/')
def index():
    return render_template('index.html',app_data=app_data)

@app.route('/checkandsaveimage',methods=["POST"])
def checkandsaveimage():
    result=""
    if request.method=="POST":
        image=request.files.get("file")
        path=os.path.join("templates","static","images",image.filename)
        image.save(path)
        
        result=api.getimgFeatureVector(path)
    return render_template('imgvector.html',imgvec=result,app_data=app_data)



@app.route('/hakkimizda')
def hakkimizda():
    return render_template('contact.html',app_data=app_data)
if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)