from flask import Flask, render_template, redirect
import pandas as pd
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def home():
    return (
        f"Here are the JSON files you can access!<br/>"
        f"/historical_2016_cleaned<br/>"
        f"/HomeSalesData_cleaned<br/>"
        f"/MarketHotness_cleaned<br/>"
    )
    
@app.route("/historical_2016_cleaned")
def jsonfile():
    return pd.read_csv("historical_2016_cleaned.csv").to_dict()

@app.route("/HomeSalesData_cleaned")
def jsonfile1():
    return pd.read_csv("HomeSalesData_cleaned.csv").to_dict()

@app.route("/MarketHotness_cleaned")
def jsonfile2():
    return pd.read_csv("MarketHotness_cleaned.csv").to_dict()

if __name__ == "__main__":
    app.run(debug=True)