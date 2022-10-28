from bs4 import BeautifulSoup
from requests import request
import requests
import pandas as pd

html = requests.get('https://www.significados.com.br/siglas-dos-estados-do-brasil-e-suas-capitais/')

codeHtml= BeautifulSoup(html.text, 'html.parser')

tabelaHtmlTitulo = codeHtml.find('table').find('thead').find('tr').find_all('th')

tabelaHtmldados = codeHtml.find('table').find('tbody').find_all('tr')

listaTituloColuna = []
for tituloColuna in tabelaHtmlTitulo:
    listaTituloColuna.append(tituloColuna.get_text().lower().replace('ã','a'))

listaDados = []
for dadosLinha in tabelaHtmldados:
    listaDadosPorLinhas = []
    for dadosColuna in dadosLinha.find_all('td'):
        listaDadosPorLinhas.extend(dadosColuna)
    listaDados.append(listaDadosPorLinhas)

DataFrameRegiao = pd.DataFrame(listaDados, columns=listaTituloColuna)
DataFrameRegiao.to_csv('../DataFrame_Regiao.csv', index = False)