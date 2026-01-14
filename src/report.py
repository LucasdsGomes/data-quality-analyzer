from metrics import dataset_overview, quality_score

def generate_dataset_report(df):
    overview = dataset_overview(df)
    score = quality_score(df)

    return {
        "overview": overview,
        "quality_score": score
    }