#importando biblioteca
import numpy as np
import matplotlib.pyplot as plt

# criando dados sintéticos
# criando dados para testar regressão linear com dados aleatórios

def train_model(df):

    np.random.seed(42)
    X = np.random.uniform(low=0.0, high=10.0, size=(1000,))
    len(X), X.max(), X.min()

    slope = 0.25
    intercep = -1.25
    noise = np.random.normal(loc=0.0, scale=1.0, size=(1000,))

    Y = slope * X + intercep + noise

    # visualizando os dados
    plt.scatter(X, Y, s=1)

    ## regressão linear com scikit-learn - modelo
    from sklearn.linear_model import LinearRegression

    lr = LinearRegression()
    lr.get_params()

    ## treinamento do modelo
    lr.fit(X.reshape(-1, 1), Y)
    lr.intercept_
    lr.coef_

    ## fazendo previsões
    y_pred = lr.predict(X.reshape(-1,1))
    print(y_pred[:10])

    ## plotando dados e linha de regressão
    plt.scatter(X,Y, s=1)
    plt.plot(X, y_pred, 'r')

   
    ## PARTE DO DATASET REAL

    from sklearn.model_selection import train_test_split
    import pandas as pd

    # separando variáveis corretamente
    X_real = df.drop(['ID', 'default payment next month'], axis=1)
    y_real = df['default payment next month']

    X_train, X_test, y_train, y_test = train_test_split(
        X_real,
        y_real,
        test_size=0.2,
        random_state=24
    )

    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)

    return X_train, X_test, y_train, y_test

    # #predict probabilidade
    # lr.predict_proba(X_test)

    # #cálculo da soma de "probabilidades"
    # np.sum(lr.predict_proba(X_test), 1)
    # #verificar formato do array
    # np.sum(lr.predict_proba(X_test), 1).shape
    # # verificar elmentos exclusivos
    # np.unique(np.sum(lr.predict_proba(X_test), 1))
    # #verificar probabilidades positivas
    # pos_proba = lr.predict_proba(X_test)[:, 1]

    # #calculo do histograma
    # plt.hist(pos_proba)
    # #plotar probabilidades
    # plt.hist(pos_proba)
    # plt.xlabel('Predicted probability of positive class for testing data')
    # plt.ylabel('Number of samples')

    # threshold = 0.25 #aumentando ao invés de 0.5
    # #isolar probablidades (pos;neg)
    # pos_sample_pos_proba = pos_proba[y_test==1]
    # neg_sample_pos_proba = neg_proba[y_test==0]

    # print(lr.predict_proba(X_test))
    # #plotar histograma empilhado
    # print(plt.hist([pos_sample_pos_proba, neg_sample_pos_proba], histtype='barstacked'))
    # plt.legend(['Positive', 'Negative'])