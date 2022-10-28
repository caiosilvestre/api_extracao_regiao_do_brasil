from flask import Flask, send_file
import os


app = Flask(__name__)

@app.route('/')
def download_csv():
    csv_path = os.path.join('./DataFrame_Regiao.csv')

    return send_file(csv_path, as_attachment=True)