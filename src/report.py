from metrics import dataset_overview, quality_score
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from datetime import datetime

def generate_dataset_report(df):
    overview = dataset_overview(df)
    score = quality_score(df)

    report = {
        "overview": {
            "numero_linhas": int(overview["Número de linhas"]),
            "numero_colunas": int(overview["Número de colunas"]),
            "colunas": list(overview["Colunas"]),

            "tipos_dados": {
                col: str(dtype)
                for col, dtype in overview["Tipos de dados"].items()
            },

            "colunas_numericas": list(overview["Colunas Numéricas"]),
            "colunas_categoricas": list(overview["Colunas Categóricas"]),

            "valores_nulos_por_coluna": {
                col: int(qtd)
                for col, qtd in overview["Valores nulos por coluna"].items()
            },

            "percentual_valores_faltantes": round(
                float(overview["Percentual de valores faltantes"]), 2
            )
        },

        "estatisticas_descritivas": {
            col: {
                stat: float(value)
                for stat, value in stats.items()
                if value is not None
            }
            for col, stats in overview["Estatísticas descritivas"].items()
        },

        "quality_score": float(score)
    }

    return report

def generate_pdf_report(report: dict) -> BytesIO:
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()
    elements = []

    # Título
    elements.append(Paragraph("Relatório de Análise Exploratória de Dados", styles['Title']))
    elements.append(Spacer(1, 12))

    # Data
    elements.append(Paragraph(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", styles['Normal']))
    elements.append(Spacer(1, 20))

    # Conteúdo dinâmico
    for section, content in report.items():
        elements.append(Paragraph(f"<b>{section}</b>", styles['Heading2']))
        elements.append(Spacer(1, 12))

        if isinstance(content, dict):
            for key, value in content.items():
                elements.append(Paragraph(f"<b>{key}:</b> {value}", styles['Normal']))

        else:
            elements.append(Paragraph(str(content), styles['Normal']))
            
        elements.append(Spacer(1, 15))

        doc.build(elements)
        buffer.seek(0)
        return buffer
