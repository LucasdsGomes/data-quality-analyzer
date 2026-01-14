import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#from report import generate_report
import json

#from loader import load_csv
#from main import quality_report

st.set_page_config(
    page_title="Dashboard de Qualidade de Dados",
    layout="wide"
)

st.title("📊 Dashboard de Qualidade de Dados")

# Upload do CSV
uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📁 Pré-visualização dos dados")
    st.dataframe(df.head())

    column = st.selectbox("Selecione a coluna para análise", df.columns)

    if column:
        col_data = df[column]

        st.subheader(f"📌 Coluna selecionada: {column}")

        # 🔹 VERIFICAÇÃO DO TIPO DA COLUNA
        if pd.api.types.is_numeric_dtype(col_data):

            try:
                quality = quality_report(df, column)

            except TypeError as e:
                st.warning(str(e))
                st.stop()

            st.subheader("🔍 Valores ausentes")
            col1, col2 = st.columns(2)
            col1.metric("Quantidade", quality["missing"]["count"])
            col2.metric("Percentual (%)", quality["missing"]["percent"])

            st.subheader("🚨 Outliers")
            if len(quality["outliers"]) == 0:
                st.success("Nenhum outlier encontrado 🎉")
            else:
                st.warning(f"{len(quality['outliers'])} outliers encontrados")
                st.dataframe(quality["outliers"])

            # 📦 BOXPLOT
            st.subheader("📦 Boxplot")
            fig = plt.figure()
            plt.boxplot(col_data.dropna(), vert=False)
            plt.title(f"Boxplot - {column}")
            st.pyplot(fig)

            st.divider()
            st.subheader("📤 Exportar relatório")

            export_report = generate_report(df, column)

            st.json(export_report)

            report_json = json.dumps(export_report, indent=4, ensure_ascii=False)

            st.download_button(
                label="📄 Baixar relatório (JSON)",
                data=report_json,
                file_name=f"relatorio_{column}.json",
                mime="application/json"
            )

        else:
            # 🔹 COLUNA CATEGÓRICA
            st.info("🔤 Coluna categórica (análise de frequência)")

            value_counts = col_data.value_counts()

            st.subheader("📊 Frequência de valores")
            st.dataframe(
                value_counts.reset_index().rename(
                    columns={"index": "Valor", column: "Frequência"}
                )
            )

            st.subheader("📈 Distribuição")
            st.bar_chart(value_counts)

            st.divider()
            st.subheader("📤 Exportar relatório")

            export_report = generate_report(df, column)

            st.json(export_report)

            report_json = json.dumps(export_report, indent=4, ensure_ascii=False)

            st.download_button(
                label="📄 Baixar relatório (JSON)",
                data=report_json,
                file_name=f"relatorio_{column}.json",
                mime="application/json"
            )

