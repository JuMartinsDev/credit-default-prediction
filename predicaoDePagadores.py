##problemas de negócio ->
##temos bons e mals pagadores, temos que identificar quem são para liberar cartões de crédito. Empresa não sabe pra quem oferecer

##bibliotecas
import pandas as pd

##carregando dados - armazenamos a base na variável
df = pd.read_excel('./base/default_of_credit_card_clients__courseware_version_1_21_19.xls')

##explorando dados
print(df.head())

##VERIFICANDO A INTEGRAIDADE DOS DADOS - QUALIDADE DOS DADOS
##examinando as colunas
print('Nomenclatura das colunas: ', df.columns)

##verificando qtd de linhas e colunas com a base
print('Quantidade linhas e colunas: ', df.shape)
## verificando quantidade de IDs únicos
print('Quantidade de IDs únicos: ', df['ID'].nunique())

##verificando a frequência de cada ID
id_counts = df['ID'].value_counts()
print('Frequência dos IDs: ', id_counts.head())

##contagem de repetiçãogit add .
print('Repetição de IDs: ', id_counts.value_counts())

##ANÁLISE DE DADOS DUPLICADOS
## IDs que se repetem - bool
dupe_mask = id_counts == 2
print(dupe_mask[:5])

## exibindo os 5 primeiros indices
print(id_counts.index[:5])
#selecionar os IDs duplicados - filtra bool dupe_mask - todo ID == true é armazenado
dupe_ids = id_counts.index[dupe_mask]
print(dupe_ids)

##conversão dos dupe_ids em lista
dupe_ids = list(dupe_ids)
print(len(dupe_ids))

##Verificando os 5 primeiros itens de 'dupe_ids'
dupe_ids[:5]

##selecionando linhas com IDs duplicados
##filtragem para verificar se ID está em dupe_id 
df.loc[df['ID'].isin(dupe_ids[0:3])]

##preparando a matriz booleana para filtragem do dataframe
##se todas as colunas estiverem zeradas, a linha não tem valor para nós
df_zero_mask = df == 0
##Criando uma série booleana -[: (linha), 1: (coluna)] - iloc (linhas e colunas)
feature_zero_mask = df_zero_mask.iloc[:, 1:].all(axis=1)
print('Soma de linhas com todas as colunas zeradas (Exeto ID): ', sum(feature_zero_mask))
##Eliminar as linhas com todas as colunas zeradas - ~ significa o contrário - loc seleciona todos os falses
## loc escolhe linhas e colunas da tabela - : é todas as colunas
df_clean_1 = df.loc[~feature_zero_mask, :].copy()
##verificando o dataframe
df_clean_1.shape
##verificando se o problema doi resolvido
print(df_clean_1['ID'].nunique())


##EXPLORANDO E LIMPANDO DADOS
##informações sobre o dataset - quando removemos as linhas ele manteve a contagem e se resetarmos ele deixa em sequencia novamente
df_clean_1.reset_index(drop=True).info
##vizualizando as primeras 5 linhas
print(df_clean_1['PAY_1'].head(5))
##contagem de valores únicos
print(df_clean_1['PAY_1'].value_counts())

##Criar máscara booleana para remover valores ausentes
valid_pay_1_mask = df_clean_1['PAY_1'] != 'Not available'
print(valid_pay_1_mask[0:5])
sum(valid_pay_1_mask)
##limpando as linhas com valores ausentes mantendo as colunas
df_clean_2 = df_clean_1.loc[valid_pay_1_mask, :].copy()
##verificando o shape do dataframe
print(df_clean_2.shape)
##substituindo coluna original (object) pela nova (int)
df_clean_2['PAY_1'] = df_clean_2['PAY_1'].astype('int64')
df_clean_2[('PAY_1, PAY_2')].info()
