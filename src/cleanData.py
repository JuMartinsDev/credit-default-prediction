## clean_data.py
## Responsável por limpar e preparar os dados

import pandas as pd

def clean_data(df):
    ## examinando as colunas
    print("VERIFICANDO A INTEGRAIDADE DOS DADOS - QUALIDADE DOS DADOS")
    print('Nomenclatura das colunas: ', df.columns, '\n')

    ## verificando qtd de linhas e colunas com a base
    print('Quantidade linhas e colunas: ', df.shape)
    ## verificando quantidade de IDs únicos
    print('Quantidade de IDs únicos: ', df['ID'].nunique(), "\n")

    ## verificando a frequência de cada ID
    id_counts = df['ID'].value_counts()
    print('Frequência dos IDs: ', id_counts.head())

    ## contagem de repetição
    print('Repetição de IDs: ', id_counts.value_counts(), "\n")

    print("ANÁLISE DE DADOS DUPLICADOS")
    dupe_mask = id_counts == 2
    print(dupe_mask[:5])

    ## exibindo os 5 primeiros indices
    print(id_counts.index[:5], '\n')

    ## selecionando os IDs duplicados
    dupe_ids = id_counts.index[dupe_mask]
    print(dupe_ids)

    ## conversão dos dupe_ids em lista
    dupe_ids = list(dupe_ids)
    print(len(dupe_ids))
    print(dupe_ids[:5], "\n")

    print("Matriz Booleana")
    ## preparando a matriz booleana para filtragem do dataframe
    ## se todas as colunas estiverem zeradas, a linha não tem valor para nós
    df_zero_mask = df == 0
    feature_zero_mask = df_zero_mask.iloc[:, 1:].all(axis=1)
    print('Soma de linhas com todas as colunas zeradas (Exceto ID): ', sum(feature_zero_mask))

    ## eliminar as linhas com todas as colunas zeradas
    df_clean_1 = df.loc[~feature_zero_mask, :].copy()
    print(df_clean_1['ID'].nunique())

    ## removendo valores ausentes da coluna PAY_1
    valid_pay_1_mask = df_clean_1['PAY_1'] != 'Not available'
    df_clean_2 = df_clean_1.loc[valid_pay_1_mask, :].copy()
    df_clean_2['PAY_1'] = df_clean_2['PAY_1'].astype('int64')

    ## verificando o shape final
    print(df_clean_2.shape, '\n')

    return df_clean_2