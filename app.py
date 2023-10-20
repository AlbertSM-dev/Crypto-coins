#!/usr/bin/env python3
import requests
from flask import Flask
import pandas as pd
from database import Database

app = Flask(__name__)

@app.route('/coins')    
def get_coins():
    Database.db_connect()  
    response = requests.get("https://api.coincap.io/v2/rates/bitcoin")
    Database.db_insert(response.json()["data"]["rateUsd"])
    return response.json()["data"]["rateUsd"]

if __name__ == "__main__":
    db = Database.db_show()
