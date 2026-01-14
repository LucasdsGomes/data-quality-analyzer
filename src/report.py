from metrics import dataset_overview, quality_score

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
