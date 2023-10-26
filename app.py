#!/usr/bin/env python3
import requests
from flask import Flask
import pandas as pd
#from database import Database
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)
# static information as metric
info = metrics.info('app_info', 'Application info', version='1.0.3')

@app.route("/")
def home():
    return "Crypto"

@app.route("/metrics")
def metrics_info():
    return info

@app.route("/health")
def health():
    return "200 OK"

@app.route('/coins')    
def get_coins():
    #Database.db_connect()  
    response = requests.get("https://api.coincap.io/v2/rates/bitcoin")
    #Database.db_insert(response.json()["data"]["rateUsd"])
    return response.json()["data"]["rateUsd"]

if __name__ == "__main__":
    app.run()
