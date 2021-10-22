import pandas as pd
import tk as tk
from wtforms.fields.simple import PasswordField
import yfinance as yf
import flask
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
import datetime
import csv
from secret import API_KEY
from flask_login import LoginManager, login_user
from wtforms import StringField, validators, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = API_KEY
Bootstrap(app)



price_list = []




class ContactForm(FlaskForm):
    ticker = StringField('Name', [validators.Length(min=2, max=8)])
    clear = SubmitField('Clear')
    submit = SubmitField('Submit')
    clear = SubmitField('Clear')

@app.route("/home", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if request.method == "POST":
        if request.form.get("submit"):
            stock = str(form.ticker.data)
            ticker = yf.Ticker(stock)
            time = str(datetime.datetime.now()).split(".")[0]
            try:
                info = ticker.info['regularMarketPrice']
                price_list.append(f"{stock}'s price is ${info} at {time}")
            except:
                flash("ERROR")
        elif request.form.get("clear"):
            price_list.clear()
    return render_template("home.html", pricelist=price_list, form=form)

@app.route("/tickers")
def tickers():
    return render_template("tickers.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
