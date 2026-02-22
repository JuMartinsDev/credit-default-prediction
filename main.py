## main.py
## Script principal que chama todos os módulos

from src.loadData import load_data
from src.cleanData import clean_data
from src.exploreData import explore_data
from src.visualizeData import visualize_data

caminho = './base/default_of_credit_card_clients__courseware_version_1_21_19.xls'

## carregando dados
df = load_data(caminho)

## limpando dados
df_clean = clean_data(df)

## explorando dados
explore_data(df_clean)

## visualizando dados
visualize_data(df_clean)