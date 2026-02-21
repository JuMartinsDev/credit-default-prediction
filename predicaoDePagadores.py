##problemas de negócio ->
##temos bons e mals pagadores, temos que identificar quem são para liberar cartões de crédito. Empresa não sabe pra quem oferecer

##bibliotecas
import pandas as pd

##carregando dados - armazenamos a base na variável
df = pd.read_excel('./base/default_of_credit_card_clients__courseware_version_1_21_19.xls')

##Verificando a integridade dos dados - Qualidade dos dados
##examinando as colunas
print('Nomenclatura das colunas: ', df.columns)

##explorando dados
print(df.head())

##verificando qtd de linhas e colunas com a base
print('Quantidade linhas e colunas: ', df.shape)
## verificando quantidade de IDs únicos
print('Quantidade de IDs únicos: ', df['ID'].nunique())

## verificando a frequência de cada ID
id_counts = df['ID'].value_counts()
print('Frequência dos IDs: ', id_counts.head())

##contagem de repetiçãogit add .
print('Repetição de IDs: ', id_counts.value_counts())
