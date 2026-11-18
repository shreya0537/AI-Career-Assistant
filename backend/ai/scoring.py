import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_resume_score_detailed(resume_text, pdf_bytes=None, branch="CSE", skills=None, projects=None):
    """
    Calculates resume score using EXACTLY the 100-point weighted model:
    - Skills: 30% (10-15 relevant skills)
    - Education: 15% (1 degree + details)
    - Projects: 20% (2-3 projects)
    - Internship/Experience: 15% (1-2 relevant experiences)
    - Certifications: 5% (2-3 relevant certifications)
    - Resume Structure: 10% (7-8 important sections)
    - Achievements: 5% (2-3 relevant achievements)
    Total = 100%
    """
    text = str(resume_text) if resume_text else ""
    text_lower = text.lower()

    skills = skills or []
    projects = projects or []

    # ---------------------------------------------------------
    # 1. SKILLS EVALUATION (30%)
    # ---------------------------------------------------------
    skill_count = len(skills)
    if skill_count >= 12:
        skills_score = 30
    elif skill_count >= 8:
        skills_score = 25
    elif skill_count >= 5:
        skills_score = 18
    elif skill_count >= 2:
        skills_score = 12
    elif skill_count == 1:
        skills_score = 6
    else:
        skills_score = 0

    # ---------------------------------------------------------
    # 2. EDUCATION EVALUATION (15%)
    # ---------------------------------------------------------
    edu_score = 0
    has_degree = bool(re.search(r"\b(b\.?e|b\.?tech|m\.?tech|b\.?sc|diploma|bachelor|master|degree)\b", text_lower))
    has_branch = bool(re.search(r"\b(computer|mechanical|civil|electronics|communication|cse|ece|it)\b", text_lower))
    has_institution = bool(re.search(r"\b(university|institute|college|school|academy)\b", text_lower))
    has_cgpa = bool(re.search(r"\b(cgpa|gpa|percentage|%|\d\.\d\d?\/10)\b", text_lower))
    has_year = bool(re.search(r"\b(20\d\d|19\d\d)\b", text_lower))

    if has_degree:
        edu_score += 5
    if has_branch:
        edu_score += 4
    if has_institution:
        edu_score += 3
    if has_cgpa or has_year:
        edu_score += 3

    edu_score = min(edu_score, 15)

    # ---------------------------------------------------------
    # 3. PROJECTS EVALUATION (20%)
    # ---------------------------------------------------------
    proj_count = len(projects)
    if proj_count >= 3:
        proj_score = 20
    elif proj_count == 2:
        proj_score = 16
    elif proj_count == 1:
        proj_score = 10
    else:
        # Check text heuristic for project mentions
        if re.search(r"\b(project|developed|built|implemented|created)\b", text_lower):
            proj_score = 8
        else:
            proj_score = 0

    # ---------------------------------------------------------
    # 4. INTERNSHIP / EXPERIENCE EVALUATION (15%)
    # ---------------------------------------------------------
    exp_matches = re.findall(
        r"\b(intern|internship|trainee|work experience|experience|developer|engineer|apprentice)\b",
        text_lower
    )
    exp_count = len(set(exp_matches))

    if exp_count >= 3:
        exp_score = 15
    elif exp_count == 2:
        exp_score = 12
    elif exp_count == 1:
        exp_score = 8
    else:
        exp_score = 0

    # ---------------------------------------------------------
    # 5. CERTIFICATIONS EVALUATION (5%)
    # ---------------------------------------------------------
    cert_matches = re.findall(
        r"\b(certificate|certification|certified|coursera|udemy|nptel|aws|cisco|workshop)\b",
        text_lower
    )
    cert_count = len(cert_matches)

    if cert_count >= 2:
        cert_score = 5
    elif cert_count == 1:
        cert_score = 3
    else:
        cert_score = 0

    # ---------------------------------------------------------
    # 6. RESUME STRUCTURE EVALUATION (10%)
    # ---------------------------------------------------------
    section_checks = {
        "Contact Info": bool(re.search(r"(@|phone|mobile|\+91|\d{10})", text_lower)),
        "Summary / Objective": bool(re.search(r"\b(summary|objective|profile|about)\b", text_lower)),
        "Education": bool(re.search(r"\b(education|academic|qualification)\b", text_lower)),
        "Skills": bool(re.search(r"\b(skills|technical|competencies)\b", text_lower)),
        "Projects": bool(re.search(r"\b(projects?|major project|mini project)\b", text_lower)),
        "Experience / Internship": bool(re.search(r"\b(experience|internship|training)\b", text_lower)),
        "Certifications": bool(re.search(r"\b(certifications?|certificates?|courses)\b", text_lower)),
        "Achievements": bool(re.search(r"\b(achievements?|awards?|honors|activities)\b", text_lower))
    }

    sections_found = sum(1 for v in section_checks.values() if v)
    structure_score = round((sections_found / 8) * 10)

    # ---------------------------------------------------------
    # 7. ACHIEVEMENTS EVALUATION (5%)
    # ---------------------------------------------------------
    achieve_matches = re.findall(
        r"\b(award|won|hackathon|first place|second place|rank|scholarship|leader|publication|certificated)\b",
        text_lower
    )
    achieve_count = len(achieve_matches)

    if achieve_count >= 2:
        achieve_score = 5
    elif achieve_count == 1:
        achieve_score = 3
    else:
        achieve_score = 0

    # Total Score Calculation (Exact Sum of 7 Weighted Components)
    total_score = skills_score + edu_score + proj_score + exp_score + cert_score + structure_score + achieve_score
    total_score = max(0, min(100, round(total_score)))

    # Breakdown dictionary
    section_scores = {
        "Skills": {"score": skills_score, "max": 30, "percentage": round((skills_score / 30) * 100)},
        "Education": {"score": edu_score, "max": 15, "percentage": round((edu_score / 15) * 100)},
        "Projects": {"score": proj_score, "max": 20, "percentage": round((proj_score / 20) * 100)},
        "Internship / Experience": {"score": exp_score, "max": 15, "percentage": round((exp_score / 15) * 100)},
        "Certifications": {"score": cert_score, "max": 5, "percentage": round((cert_score / 5) * 100)},
        "Resume Structure": {"score": structure_score, "max": 10, "percentage": round((structure_score / 10) * 100)},
        "Achievements": {"score": achieve_score, "max": 5, "percentage": round((achieve_score / 5) * 100)}
    }

    # Generate Strengths, Missing Info, and Improvement Suggestions
    strengths = []
    missing_info = []
    improvement_suggestions = []

    if skills_score >= 20:
        strengths.append(f"Strong technical skill diversity with {skill_count} relevant branch skills detected.")
    else:
        missing_info.append("Fewer than 10 technical skills found (10-15 recommended for optimal scoring).")
        improvement_suggestions.append("Add core branch technical tools, frameworks, and specific technical keywords.")

    if proj_score >= 15:
        strengths.append(f"Comprehensive project history with {proj_count} project entries detailed.")
    else:
        missing_info.append("Only " + (f"{proj_count}" if proj_count > 0 else "0") + " projects identified (2-3 recommended).")
        improvement_suggestions.append("Detail at least 2-3 technical projects with clear tech stacks, candidate roles, and outcomes.")

    if exp_score >= 10:
        strengths.append("Relevant industrial internship / work experience documented.")
    else:
        missing_info.append("No explicit internship or corporate experience section found.")
        improvement_suggestions.append("Include 1-2 industrial internships or hands-on training programs.")

    if cert_score >= 3:
        strengths.append("Verified professional certifications listed.")
    else:
        missing_info.append("No technical certifications detected.")
        improvement_suggestions.append("Add 2-3 recognized certifications (Coursera, NPTEL, Udemy, IEEE, or domain workshops).")

    if not has_cgpa:
        missing_info.append("Academic CGPA / Percentage or graduation details missing.")
        improvement_suggestions.append("Mention your exact CGPA/percentage and institution details in Education.")

    if achievements_str := achieve_score >= 3:
        strengths.append("Demonstrated extra achievements, competition awards, or leadership roles.")
    else:
        missing_info.append("No achievements or hackathon wins identified.")
        improvement_suggestions.append("Include hackathon participation, academic awards, or leadership responsibilities.")

    if structure_score >= 8:
        strengths.append(f"Well-structured resume layout containing {sections_found} key sections.")

    return {
        "overall_score": total_score,
        "section_scores": section_scores,
        "strengths": strengths,
        "missing_info": missing_info,
        "improvement_suggestions": improvement_suggestions
    }


def calculate_score(resume_text):
    """Backwards compatible function for single resume score calculation."""
    res = calculate_resume_score_detailed(resume_text)
    return res["overall_score"]


def calculate_answer_score(user_answer, reference_answers):
    """Calculates answer score using TF-IDF cosine similarity."""
    if not user_answer or not user_answer.strip():
        return 0
    if not reference_answers:
        return 0

    answers = [str(answer) for answer in reference_answers]
    all_text = [user_answer] + answers

    try:
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform(all_text)
        similarities = cosine_similarity(vectors[0:1], vectors[1:])[0]
        best_score = max(similarities)
        return round(best_score * 100)
    except ValueError:
        return 0