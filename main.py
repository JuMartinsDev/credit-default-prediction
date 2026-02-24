## main.py
## Script principal que chama todos os módulos

from src.loadData import load_data
from src.cleanData import clean_data
from src.exploreData import explore_data
from src.visualizeData import visualize_data
from src.visualizeData import implementacao_ohe
from src.trainModel import train_model
from src.modelPipeline import run_model_pipeline

caminho = './base/default_of_credit_card_clients__courseware_version_1_21_19.xls'

## carregando dados
print("Carregando dados...")
df = load_data(caminho)

## limpando dados
print("Limpando dados...")
df_clean = clean_data(df)

## explorando dados
print("Explorando dados...")
explore_data(df_clean)

## visualizando dados
print("Visualizando dados...")
visualize_data(df_clean)

# implementação OHE
print("Aplicando One Hot Encoding...")
df_model = implementacao_ohe(df_clean)

#  BASE TRATADA
df_model.to_excel("base_tratada_modelagem.xlsx", index=False)
print("Base tratada exportada com sucesso!")

print("Preparando treino e teste...")
X_train, X_test, y_train, y_test = train_model(df_model)

print("Rodando pipeline do modelo...")
run_model_pipeline(X_train, X_test, y_train, y_test)

print("Processo finalizado com sucesso!")