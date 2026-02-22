## visualize_data.py
## Responsável por visualizações gráficas

import matplotlib.pyplot as plt

def visualize_data(df_clean_2):
    ##Explorando limite de crédito e características demográficas

    ##Gerando histograma para 'Age' e 'Limit_Bal'
    df_clean_2[['AGE', 'LIMIT_BAL']].hist()
    plt.show()

    ##estatística descritiva de Age e Limit_Bal
    print(df_clean_2[['AGE', 'LIMIT_BAL']].describe())

    ##contagem de ocorrências por categoria em education
    print(df_clean_2['EDUCATION'].value_counts())

    ##transformar 0, 5 e 6 em outros (4 = outros) - inplace modifica o dataframe original
    df_clean_2['EDUCATION'].replace(to_replace=(0,5,6), value = 4, inplace=True)
    print(df_clean_2['EDUCATION'].value_counts())

    ##contagem de ocorrências por categoria em 'Marriage'
    df_clean_2['MARRIAGE'].value_counts()
    ##transformar 0 em outros (3)
    df_clean_2['MARRIAGE'].replace(to_replace=(0), value=3, inplace=True)
    df_clean_2['MARRIAGE'].value_counts()

    ##Características categóricas (experimento)
    default_by_edu = df_clean_2.groupby('EDUCATION').agg({'default payment next month': 'mean'})
    ##gerando gráfico de barras (mantendo a média calculada com agg)
    default_by_edu.plot(kind='bar', legend=False, title='Média de Defaults por Educação')
    plt.ylabel('Defalut Rate')
    plt.xlabel('Education Level: ordinal encoding')
    plt.show()
