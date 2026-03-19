def generate_structured_roadmap(missing_skills, role):

    roadmap = {
        "Core ML Depth": [
            "Supervised/Unsupervised algorithms (SVM, XGBoost, clustering)",
            "Model evaluation (ROC-AUC, F1, cross-validation)"
        ],
        "Deep Learning": [
            "Neural Networks, CNN, RNN",
            "TensorFlow / PyTorch"
        ],
        "Feature Engineering & EDA": [
            "Data cleaning",
            "Advanced visualization"
        ],
        "MLOps / Deployment": [
            "Flask / FastAPI",
            "Docker basics"
        ]
    }

    if missing_skills:
        return roadmap
    else:
        return {}