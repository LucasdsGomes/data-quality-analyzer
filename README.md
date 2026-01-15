# 📊 Analyst Dashboard — Data Quality Analyzer

Aplicação interativa desenvolvida em **Python + Streamlit** para análise de qualidade de dados em arquivos CSV, com métricas automáticas, score de qualidade e exportação de relatórios.

🔗 **Aplicação online:** https://data-quality-analyzer.streamlit.app

---

## 🚀 Funcionalidades

- 📁 Upload de arquivos CSV  
- 👀 Pré-visualização dos dados  
- 📊 Visão geral do dataset  
- 🧮 Estatísticas descritivas automáticas  
- ⚠️ Detecção de valores ausentes  
- 🚨 Detecção de outliers (IQR)  
- 🧠 **Quality Score** do dataset (0–100)  
- 📦 Visualização com boxplot  
- 📤 Exportação de relatório em JSON  
- 🔤 Suporte a colunas numéricas e categóricas  

---

## 🧠 Quality Score — Como funciona?

O **Quality Score** é uma métrica criada para avaliar a qualidade geral do dataset.  
O score inicia em **100 pontos** e sofre penalizações com base em:

- Percentual de valores ausentes  
- Presença de outliers em colunas numéricas  
- Colunas problemáticas (mais de 50% de valores nulos)  

### 📌 Interpretação do score

- **80 – 100:** Alta qualidade  
- **50 – 79:** Qualidade média  
- **< 50:** Baixa qualidade  

---

## 🛠️ Tecnologias utilizadas

- **Python 3.11+**
- **Streamlit**
- **Pandas**
- **Matplotlib**

---

## ▶️ Como executar localmente

### 1️⃣ Clone o repositório
```
git clone https://github.com/seu-usuario/analyst-dashboard.git
```
```
cd analyst-dashboard
```

## 2️⃣ Crie e ative o ambiente virtual
```
python -m venv .venv
```

### Windows
```
.venv\Scripts\activate
```

### Linux / Mac
```
source .venv/bin/activate
```

# 3️⃣ Instale as dependências
```
pip install -r requirements.txt
```

# 4️⃣ Execute a aplicação
```
streamlit run src/app.py
```

## 📌 Exemplos de uso
- Avaliar rapidamente a qualidade de um dataset
- Apoiar decisões de limpeza de dados
- Criar relatórios automáticos de diagnóstico
- Uso educacional em análise exploratória de dados

## 📈 Roadmap (Próximas melhorias)

- 📊 Visualização detalhada do score
- 🧪 Comparação entre múltiplos datasets
- 📄 Exportação de relatórios em PDF
- 🧠 Sugestões automáticas de limpeza
- 🗂️ Dataset de exemplo embutido

## 👨‍💻 Autor

Lucas Gomes

- Desenvolvedor focado em Back-end, automação e análise de dados.
[LinkedIn](https://www.linkedin.com/in/lucasdsgomes/)

