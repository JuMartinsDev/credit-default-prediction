#importando biblioteca
import numpy as np
import matplotlib.pyplot as plt

# criando dados sintéticos
# criando dados para testar regressão linear com dados aleatórios

def train_model():

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

    URL = 'https://raw.githubusercontent.com/TrainingByPackt/Data-Science-Projects-with-Python/master/Data/Chapter_1_cleaned_data.csv'
    df = pd.read_csv(URL)

    # separando variáveis corretamente
    X_real = df[['EDUCATION']]
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