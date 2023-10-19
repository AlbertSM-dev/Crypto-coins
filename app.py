#!/usr/bin/env python3
import requests
from flask import Flask
import pandas as pd
from database import db_connect, db_insert, db_show

app = Flask(__name__)

@app.route('/coins')    
def get_coins():
    db_connect()  
    response = requests.get("https://api.coincap.io/v2/rates/bitcoin")
    db_insert(response.json()["data"]["rateUsd"])
    return response.json()["data"]["rateUsd"]

if __name__ == "__main__":
    db = db_show()
