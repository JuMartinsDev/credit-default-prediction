# model_pipeline.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix


def run_model_pipeline(X_train, X_test, y_train, y_test, threshold=0.25):

    print("=== Treinando modelo de Regressão Logística ===")

    # Modelo
    model = LogisticRegression(max_iter=1000)

    # Treinamento
    model.fit(X_train, y_train)

    # Probabilidades
    y_proba = model.predict_proba(X_test)
    pos_proba = y_proba[:, 1]

    # Aplicando threshold customizado
    y_pred = (pos_proba >= threshold).astype(int)

    print("\n=== Métricas ===")
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("Precisão:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))

    print("\nMatriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))

    # Histograma das probabilidades
    plt.hist(pos_proba)
    plt.xlabel("Probabilidade prevista de Default")
    plt.ylabel("Quantidade de Clientes")
    plt.title("Distribuição das Probabilidades de Inadimplência")
    plt.show()

    # Criando DataFrame com score
    df_score = X_test.copy()
    df_score["real_default"] = y_test.values
    df_score["prob_default"] = pos_proba
    df_score["prediction"] = y_pred

    # Exportando resultado
    df_score.to_excel("clientes_com_score.xlsx", index=False)

    print("\nArquivo 'clientes_com_score.xlsx' gerado com sucesso!")

    return model