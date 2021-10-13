import pandas as pd
import tk as tk
import yfinance as yf
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import datetime
import csv
from secret import API_KEY

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
                price_list.append(f"The Price of {stock} at {time} = {info}")
            except:
                flash("ERROR")
        elif request.form.get("clear"):
            price_list.clear()
    return render_template("index.html", pricelist=price_list, form=form)


@app.route("/stocks")
def stocks():
    pass



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
