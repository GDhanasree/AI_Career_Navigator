def generate_learning_phases(role):

    if role == "Data Scientist":
        return {
            "Phase 1: Foundations (2-3 weeks)": [
                "Revise statistics, probability, linear algebra",
                "Understand evaluation metrics"
            ],
            "Phase 2: Core ML (3-4 weeks)": [
                "Learn Logistic Regression, SVM, Trees",
                "Build 2 ML projects"
            ],
            "Phase 3: Advanced (3-4 weeks)": [
                "Deep Learning basics",
                "NLP or Time Series"
            ],
            "Phase 4: Deployment (2-3 weeks)": [
                "Build APIs using Flask/FastAPI",
                "Learn Docker"
            ],
            "Phase 5: Portfolio": [
                "Build 3-5 strong projects",
                "Upload to GitHub"
            ]
        }

    return {}