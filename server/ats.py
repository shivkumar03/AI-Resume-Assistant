def calculate_ats_score(resume_text, job_desc):

    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())

    if len(job_words) == 0:
        return 0, []

    matched = resume_words.intersection(job_words)

    score = int((len(matched) / len(job_words)) * 100)

    return score, list(matched)