## explore_data.py
## Responsável por explorar estatísticas do dataset

def explore_data(df):
    print("Explorando dados")
    ## vizualizando as primeiras 5 linhas
    print(df['PAY_1'].head(5))

    ## contagem de valores únicos
    print(df['PAY_1'].value_counts(), "\n")