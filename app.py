#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template,request,redirect,url_for
import api,os
import pandas as pd
from blockchain import BlockChain
from imagesimilarity import ImageFeatureExtractor,ImageComparator
DEVELOPMENT_ENV  = True

app = Flask(__name__)
app._static_folder=os.path.join("templates","static")
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
@app.route('/listblocks')
def listblocks():
    blocksdata= [ block['blockdata'] for block in api.mainchain.chain if block!=BlockChain.initialblock]
    return render_template('listblocks.html',app_data=app_data,blocksdata=blocksdata)

@app.route('/checkandsaveimage',methods=["POST"])
def checkandsaveimage():
    result,error=None,None
    if request.method=="POST":
        image=request.files.get("file")
        username=request.form.get('username')
        path=os.path.join("templates","static","images",image.filename)
        image.save(path)
        result=api.append2Chain(username,path)
    return render_template('imgvector.html',imgvec=result,imgnamewithextention=image.filename.split("/")[-1],app_data=app_data,error=result==None)

@app.route('/hakkimizda')
def hakkimizda():
    return render_template('contact.html',app_data=app_data)
if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)