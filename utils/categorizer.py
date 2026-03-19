def categorize_skills(skills):
    categories = {
        "Programming": ["python", "javascript"],
        "Data": ["sql", "statistics"],
        "AI": ["machine learning", "deep learning"]
    }

    result = {}

    for category, cat_skills in categories.items():
        result[category] = [s for s in skills if s in cat_skills]

    return result