
# API com dados sobre as regiões do Brasil
![icons](https://skills.thijs.gg/icons?i=python,heroku,&theme=light)

    A api possui uma tabela com os dados: Nome dos estados, sigla, capital,região.  
    
    Repositório criado para ser consumido pela plataforma Heroku.




## Documentação da API

#### Retorna tabela

```
  GET /
```

| Tipo       | Descrição                           |
| :--------- | :---------------------------------- |
| `json` | retorna a tabela contendo os dados|




## Demonstração

| estado     | sigla|capital|regiao
| :--------- | :----|:------| :----|
| Roraima    |  RR  |Boa Vista|Norte|
| Amapá    |  AP  |Macapá|Norte|


[![tabela](https://img.shields.io/badge/Link-Tabela_Enviada-brightgreen)](https://github.com/caiosilvestre/api_extracao_regiao_do_brasil/blob/main/DataFrame_Regiao.csv)


## Stack utilizada

![python](https://skills.thijs.gg/icons?i=flask,python,&theme=light)

**Back-end:** Python,Flask, Gunicorn.

[![requirements](https://img.shields.io/badge/link-requirements.txt-brightgreen)](https://github.com/caiosilvestre/api_extracao_regiao_do_brasil/blob/main/requirements.txt)




## Scrap realizado para obter a tabela 

Tabela foi raspada do site: [www.significados.com.br](https://www.significados.com.br/siglas-dos-estados-do-brasil-e-suas-capitais/)

![python](https://skills.thijs.gg/icons?i=python,&theme=light)

**Back-end:** Beautiful Soup.

[![scrap](https://img.shields.io/badge/link-arquivo_scrap-brightgreen)](https://github.com/caiosilvestre/api_extracao_regiao_do_brasil/blob/main/scrap/scrap.py)

## Autor
- [@caiosilvestre](https://www.github.com/caiosilvestre)
