## load_data.py
## Responsável por carregar os dados do Excel

import pandas as pd

def load_data(caminho):
    ## problemas de negócio ->
    ## temos bons e maus pagadores, temos que identificar quem são para liberar cartões de crédito.
    ## Empresa não sabe pra quem oferecer

    ## carregando dados - armazenamos a base na variável
    df = pd.read_excel(caminho)

    ## explorando dados
    print(df.head(),"\n")

    return df