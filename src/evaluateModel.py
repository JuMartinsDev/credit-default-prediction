from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score
import numpy as np

def evaluate_model(X_train, X_test, y_train, y_test):

    #treinamento
    lr = LogisticRegression()
    lr.fit(X_train, y_train)

    #previsão
    y_pred = lr.predict(X_test)

    #acurácia - previsão vs base
    acc = np.mean(y_pred == y_test)
    # acc = sum(y_pred == y_test) / len(y_pred)
    
    ## matriz de confusão
    TP = sum((y_pred==1) & (y_test==1))
    TN = sum((y_pred==0) & (y_test==0))
    FP = sum((y_pred==1) & (y_test==0))
    FN = sum((y_pred==0) & (y_test==1))

    confusion_matrix = np.array([[TN, FP], [FN, TP]])

    acuracia = (TP + TN) / (TP+TN+FP+FN)
    print("Acurácia:", acuracia)

    sum(confusion_matrix.diagonal()) / confusion_matrix.sum()

    return lr