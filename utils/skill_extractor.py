def extract_skills(resume_text, skill_list):
    resume_text = resume_text.lower()

    extracted = []
    for skill in skill_list:
        if skill in resume_text:
            extracted.append(skill)

    # Bonus: detect common keywords
    if "pandas" in resume_text:
        extracted.append("pandas")

    return list(set(extracted))