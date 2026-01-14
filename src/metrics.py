import pandas as pd

def dataset_overview(df):
    """Retorna uma visão geral do dataset."""
    overview = {
        "Número de linhas": df.shape[0],
        "Número de colunas": df.shape[1],
        "Colunas": df.columns.tolist(),
        "Tipos de dados": df.dtypes.to_dict(),
        "Colunas Numéricas": df.select_dtypes(include="number").columns,
        "Colunas Categóricas": df.select_dtypes(exclude="number").columns,
        "Valores nulos por coluna": df.isnull().sum().to_dict(),
        "Estatísticas descritivas": df.describe().to_dict(),
        "Percentual de valores faltantes": (df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100),
    }
    return overview

def quality_score(df):
    score = 100
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()
    missing_percentage = (missing_cells / total_cells) * 100

    # Penalidade por dados faltantes (máx -40)
    missing_penalty = min(40, missing_percentage * 0.5)

    # Penalidade por outliers (máx -30)
    outlier_penalty = 0
    numeric_cols = df.select_dtypes(include="number")

    for col in numeric_cols.columns:
        series = numeric_cols[col]
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = numeric_cols[(numeric_cols[col] < lower_bound) | (numeric_cols[col] > upper_bound)]
        outlier_ratio = len(outliers) / len(df)
        outlier_penalty += min(10, outlier_ratio * 100)

    outlier_penalty += len(outliers) / total_cells * 30

    # Penalidade por colunas problemáticas
    problematic_cols = df.columns[
        df.isnull().mean() > 0.5
    ]

    column_penalty = min(30, len(problematic_cols) * 5)
    score -= (missing_penalty + outlier_penalty + column_penalty)

    return round(max(score, 0 ), 2)