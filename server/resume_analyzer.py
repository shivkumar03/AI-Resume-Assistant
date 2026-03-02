import PyPDF2

COMMON_SKILLS = [
    "python", "react", "flask", "java", "c++",
    "machine learning", "ai", "nlp", "sql",
    "git", "github", "api", "data structures"
]

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def analyze_resume(file):

    text = extract_text_from_pdf(file)
    text_lower = text.lower()

    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in text_lower:
            found_skills.append(skill)

    word_count = len(text.split())

    suggestions = []

    if word_count < 200:
        suggestions.append("Resume is too short. Add more project details.")

    if len(found_skills) < 5:
        suggestions.append("Add more technical skills.")

    if "project" not in text_lower:
        suggestions.append("Mention your projects clearly.")

    return {
        "word_count": word_count,
        "skills_found": found_skills,
        "suggestions": suggestions
    }