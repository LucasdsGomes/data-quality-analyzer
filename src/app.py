import streamlit as st
import pandas as pd
from metrics import dataset_overview
from metrics import quality_score
import json
from report import generate_dataset_report, generate_pdf_report

st.set_page_config(page_title="EDA Dashboard", layout="wide")

st.title("📊 Dashboard de Análise Exploratória de Dados")

uploaded_file = st.file_uploader("Carregar arquivo CSV", type=["csv"])

if uploaded_file:
    
    df = pd.read_csv(uploaded_file)
    overview = dataset_overview(df)
    
    st.subheader("Visualização dos Dados")
    st.dataframe(df.head())

    st.subheader("Estatísticas Descritivas")
    #st.write(df.describe()) # Gráfico de estatísticas descritivas
    st.write(overview)

    st.subheader("Pontuação de Qualidade do Dataset")
    score = quality_score(df)

    st.divider()
    st.metric(label="Pontuação de Qualidade", value=f"{score} / 100")

    if score >= 80:
        st.success("Dados com ótima qualidade ✅")
    elif score >= 60:
        st.warning("Qualidade aceitável, mas com pontos de atenção ⚠️")
    else:
        st.error("Qualidade baixa, revisão recomendada ❌")

    st.divider()
    st.subheader("Exportar Relatório Geral")

    report = generate_dataset_report(df)
    report_json = json.dumps(report, indent=4, ensure_ascii=False)

    report = generate_dataset_report(df)
    report_json = json.dumps(report, indent=4, ensure_ascii=False)

    # JSON
    st.download_button(
        label="📥 Baixar Relatório JSON",
        data=report_json,
        file_name="relatorio_dataset.json",
        mime="application/json"
    )

    # PDF
    pdf_buffer = generate_pdf_report(report)

    st.download_button(
        label="📄 Baixar Relatório PDF",
        data=pdf_buffer,
        file_name="relatorio_dataset.pdf",
        mime="application/pdf"
    )
