from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def download_csv():
    csv = 'Arquivo enviado  .csv'
    response = make_response(csv)
    cd = 'attachment; filename=DataFrame_Regiao.csv'
    response.headers['Content-Disposition'] = cd
    response.mimetype='text/csv'

    return 'hellow'