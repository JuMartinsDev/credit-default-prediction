import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score


def evaluate_with_roc(X_train, X_test, y_train, y_test):

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Probabilidades da classe positiva
    y_proba = model.predict_proba(X_test)[:, 1]

    # AUC
    auc = roc_auc_score(y_test, y_proba)
    print("AUC:", auc)

    # Curva ROC
    fpr, tpr, thresholds = roc_curve(y_test, y_proba)

    plt.figure()
    plt.plot(fpr, tpr)
    plt.plot([0,1], [0,1])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Curva ROC")
    plt.show()

    # Criando arquivo final com score
    df_resultado = X_test.copy()
    df_resultado["real_default"] = y_test.values
    df_resultado["prob_default"] = y_proba

    df_resultado.to_excel("resultado_modelo_credito.xlsx", index=False)

    print("Arquivo 'resultado_modelo_credito.xlsx' gerado!")

    return model