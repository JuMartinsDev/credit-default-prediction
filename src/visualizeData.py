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


def implementacao_ohe(df_clean_2):
    ##criando uma coluna vazia
    df_clean_2['EDUCATION_CAT'] = 'none'
    ##Examinando as primeiras 10 linhas
    print(df_clean_2[['EDUCATION', 'EDUCATION_CAT']].head(10))
    ##criando um dicionário de mapeamento de categorias
    cat_mapping={
        1:'graduate school',
        2:'university',
        3:'high school',
        4:'others'
    }
    #print(cat_mapping)
    ##aplicando o mapeamento de categorias - e substitui a coluna anterior
    df_clean_2['EDUCATION_CAT'] = df_clean_2['EDUCATION'].map(cat_mapping)
    print(df_clean_2[['EDUCATION', 'EDUCATION_CAT']].head(10))

    ##codificação de características com OHE - gera df em que gera 4 colunas em que tudo é zero menos o valor correspondente
    edu_ohe = pd.get_dummies(df_clean_2, ['EDUCATION_CAT'])
    print(edu_ohe.head(10))

    #concatenando o dataframe original com OHE - axis=1 concatena lado a lado
    df_with_one = pd.concat([df_clean_2, edu_ohe], axis=1)
    df_with_one[['EDUCATION_CAT', 'graduate school', 'high school', 'others', 'university']].head(10)
    df_with_one.shape

    df_with_one.to_csv('cleaned_data.csv', index=False)

##TESTES
if __name__ == "__main__":
    import pandas as pd

    # Criando um DataFrame de teste só para ver os prints
    df_test = pd.DataFrame({
        'EDUCATION': [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
    })

    # Chama a função para ver os prints
    implementacao_ohe(df_test)