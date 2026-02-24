# 💳 Credit Default Prediction

Projeto de Python, Análise de dados e Machine Learning para previsão de inadimplência de clientes de cartão de crédito.

---

## 📊 Sobre o Projeto

Este projeto tem como objetivo prever se um cliente irá entrar em default no próximo mês, utilizando dados históricos de crédito.

O dataset contém informações sobre:

- Limite de crédito (`LIMIT_BAL`)
- Dados demográficos (`SEX`, `AGE`, `EDUCATION`, `MARRIAGE`)
- Histórico de pagamentos (`PAY_1` a `PAY_6`)
- Valores de faturas (`BILL_AMT1` a `BILL_AMT6`)
- Valores pagos anteriormente (`PAY_AMT1` a `PAY_AMT6`)

O pipeline foi estruturado de forma modular, separando cada etapa do processo em arquivos distintos dentro da pasta `src`.

---

## 🧠 Pipeline do Projeto

O fluxo completo é executado pelo arquivo `main.py`:

1. **Load Data** – Carregamento da base `.xls`
2. **Data Cleaning** – Tratamento de inconsistências, duplicados e dados inválidos
3. **Exploratory Data Analysis (EDA)**
4. **Visualizações estatísticas**
5. **Feature Engineering (One Hot Encoding)**
6. **Train/Test Split**
7. **Treinamento com Regressão Logística**
8. **Avaliação do Modelo**
9. **Geração de score dos clientes**

---

## 📈 Resultados do Modelo

Modelo utilizado: **Regressão Logística**

Métricas obtidas:

- Acurácia: 73%
- Precisão: 41%
- Recall: 57%

```

O modelo apresenta desempenho consistente, com boa capacidade de identificar clientes com risco de inadimplência.

---

## 🗂️ Estrutura do Projeto
.
├── main.py
├── base/
│   └── default_of_credit_card_clients.xls
├── src/
│   ├── loadData.py
│   ├── cleanData.py
│   ├── exploreData.py
│   ├── visualizeData.py
│   ├── trainModel.py
│   ├── modelPipeline.py
└── README.md

````

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## ▶️ Como Executar o Projeto

1️⃣ Clone o repositório:

git clone https://github.com/seuusuario/seurepositorio.git

2️⃣ Crie um ambiente virtual:

python -m venv venv

3️⃣ Ative o ambiente virtual:

**Windows:**
venv\Scripts\activate


**Mac/Linux:**
source venv/bin/activate

4️⃣ Instale as dependências:

pip install -r requirements.txt


5️⃣ Execute o projeto:

python main.py


## 👨‍💻 Autor
LinkedIn: https://www.linkedin.com/in/julia-martins3/

