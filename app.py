from flask import Flask, send_file
import pandas as pd
import os


app = Flask(__name__)

@app.route('/')
def download_csv():
    df = pd.read_csv('./DataFrame_Regiao.csv')
    return df.to_dict(), 200
