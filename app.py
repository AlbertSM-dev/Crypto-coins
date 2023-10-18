#!/usr/bin/env python3
import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Crypto.sqlite3'

db = SQLAlchemy(app)

class Crypto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String(50))

@app.route('/')    
def get_coins():
    response = requests.get("https://api.coincap.io/v2/assets")
    return response.json()["data"]

if __name__ == "__main__":
    current_price = get_coins()
    new_entry = Crypto(price=current_price["priceUs"])
    db.session.add(new_entry)
    db.session.commit()