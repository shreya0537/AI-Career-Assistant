import re
import pymupdf
from backend.constants import MASTER_JOB_ROLES

# =========================================
# MASTER SKILLS BY BRANCH
# =========================================

ALL_BRANCH_SKILLS = {
    "CSE": [
        "Python", "Java", "C++", "C", "SQL", "HTML", "CSS", "JavaScript",
        "Machine Learning", "Deep Learning", "React", "Flask", "Django",
        "Streamlit", "Scikit-learn", "NLP", "Power BI", "MS Excel",
        "Operating Systems", "Computer Networks", "DBMS", "Cloud Computing",
        "Data Structures", "Algorithms", "Git", "REST APIs", "Docker"
    ],
    "ECE": [
        "C", "C++", "Embedded C", "Microcontrollers", "Arduino", "Raspberry Pi",
        "VLSI", "Verilog", "VHDL", "MATLAB", "Simulink", "PCB Design",
        "Digital Electronics", "Analog Electronics", "Communication Systems",
        "Signals and Systems", "IoT", "Sensors", "Microprocessors", "FPGA", "RTOS"
    ],
    "Mechanical": [
        "AutoCAD", "SolidWorks", "CATIA", "ANSYS", "Thermodynamics",
        "Fluid Mechanics", "Strength of Materials", "Machine Design",
        "CNC", "Manufacturing Processes", "Heat Transfer", "Materials Science",
        "Production Engineering", "Engineering Mechanics", "CAD/CAM", "MATLAB", "Python",
        "GD&T", "HVAC", "Mechatronics"
    ],
    "Civil": [
        "AutoCAD", "STAAD.Pro", "ETABS", "Surveying", "Concrete Technology",
        "Structural Engineering", "Soil Mechanics", "Geotechnical Engineering",
        "Transportation Engineering", "Environmental Engineering", "Hydraulics",
        "Construction Management", "Estimation", "Revit", "MATLAB", "Python",
        "Structural Analysis", "Total Station", "BIM"
    ]
}


PROGRAMMING_LANGUAGES = [
    "Python", "C++", "C", "Java", "JavaScript", "TypeScript", "C#",
    "SQL", "Go", "Rust", "PHP", "Kotlin", "Swift", "R", "MATLAB",
    "Verilog", "VHDL", "Assembly", "Embedded C", "HTML", "CSS"
]


def extract_programming_languages(skills=None, resume_text=""):
    """
    Extracts programming languages explicitly mentioned in candidate skills or resume text.
    """
    found = []
    text_lower = (resume_text or "").lower()

    for s in (skills or []):
        s_clean = s.strip()
        s_lower = s_clean.lower()
        for lang in PROGRAMMING_LANGUAGES:
            if lang.lower() == s_lower:
                if lang not in found:
                    found.append(lang)

    if not found and text_lower:
        import re
        for lang in PROGRAMMING_LANGUAGES:
            if lang.upper() == "C":
                pattern = r"(?<![A-Za-z])c(?![A-Za-z\+\#])"
            else:
                pattern = r"\b" + re.escape(lang.lower()) + r"\b"
            if re.search(pattern, text_lower) and lang not in found:
                found.append(lang)

    return found


def extract_skills(resume_text, branch="CSE"):
    """
    Extracts branch-specific technical skills from the uploaded resume text.
    """
    if not resume_text:
        return []

    branch_skills = ALL_BRANCH_SKILLS.get(branch, ALL_BRANCH_SKILLS["CSE"])
    all_combined = list(dict.fromkeys(
        branch_skills + [s for b_list in ALL_BRANCH_SKILLS.values() for s in b_list]
    ))

    text = str(resume_text)

    pattern = (
        r"\b(?:technical\s+skills|skills|skill\s+set|competencies|expertise)"
        r"\s*(?::|-|–)?\s*"
        r"(.*?)"
        r"(?=\n\s*(?:"
        r"education|"
        r"academic\s+qualification|"
        r"experience|"
        r"work\s+experience|"
        r"projects?|"
        r"certifications?|"
        r"certificates?|"
        r"achievements?|"
        r"internships?|"
        r"languages|"
        r"hobbies|"
        r"interests|"
        r"references?|"
        r"declaration"
        r")\s*:?\s*|\Z)"
    )

    skills_match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    search_scope = skills_match.group(1) if skills_match else text

    found_skills = []

    for skill in all_combined:
        if skill.upper() == "C":
            skill_pattern = r"(?<![A-Za-z])C(?![A-Za-z\+\#])"
        else:
            skill_pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(skill_pattern, search_scope, re.IGNORECASE):
            if skill not in found_skills:
                found_skills.append(skill)

    # Sort skills putting current branch skills first
    branch_set = set(branch_skills)
    found_skills.sort(key=lambda s: 0 if s in branch_set else 1)

    return found_skills


def get_job_roles_detailed(skills, branch="CSE", resume_text=""):
    """
    Matches candidate skills against the provided MASTER_JOB_ROLES dataset
    and returns EXACTLY 2 most relevant job roles with detailed metrics:
    - role name
    - match percentage (%)
    - matching skills
    - missing important skills
    - short explanation of why the role is relevant
    """
    branch_roles = MASTER_JOB_ROLES.get(branch, MASTER_JOB_ROLES["CSE"])
    cand_skills_lower = {s.lower() for s in skills}
    res_text_lower = (resume_text or "").lower()

    scored_roles = []

    for role_info in branch_roles:
        role_name = role_info["role"]
        req_skills = role_info["required_skills"]

        matching = []
        missing = []

        for req_s in req_skills:
            req_s_lower = req_s.lower()
            if req_s_lower in cand_skills_lower or req_s_lower in res_text_lower:
                matching.append(req_s)
            else:
                missing.append(req_s)

        total_req = len(req_skills)
        match_count = len(matching)

        if cand_skills_lower:
            match_pct = round((match_count / max(total_req, 1)) * 100)
            # Add a slight boost if match_count >= 1 to differentiate
            match_pct = min(100, max(match_pct, 40 if match_count >= 1 else 20))
        else:
            # Baseline default match if resume has few skills
            match_pct = 50 if role_name in [branch_roles[0]["role"], branch_roles[1]["role"]] else 30

        scored_roles.append({
            "role": role_name,
            "match_percentage": match_pct,
            "matching_skills": matching,
            "missing_skills": missing,
            "explanation": role_info["explanation"]
        })

    # Sort roles by match_percentage descending
    scored_roles.sort(key=lambda x: (x["match_percentage"], len(x["matching_skills"])), reverse=True)

    # Return EXACTLY 2 job roles
    return scored_roles[:2]


def get_job_roles(skills, branch="CSE"):
    """
    Returns list of role strings for the top 2 recommended job roles.
    """
    detailed = get_job_roles_detailed(skills, branch=branch)
    return [d["role"] for d in detailed]


def extract_projects_from_pdf(pdf_bytes):
    """
    Extracts project titles from uploaded PDF resume.
    """
    if not pdf_bytes:
        return []

    try:
        document = pymupdf.open(stream=pdf_bytes, filetype="pdf")
    except Exception:
        return []

    projects_bold = []
    projects_heuristic = []
    inside_projects = False

    project_headings = {
        "projects", "project", "academic projects", "academic project",
        "personal projects", "personal project", "major project", "mini project"
    }

    stop_sections = {
        "education", "academic qualification", "academic qualifications",
        "experience", "work experience", "skills", "technical skills",
        "skill set", "certification", "certifications", "certificate",
        "certificates", "achievements", "achievement", "internship",
        "internships", "languages", "hobbies", "interests", "references", "declaration"
    }

    certificate_words = [
        "certificate", "certification", "certified", "coursera",
        "udemy", "nptel", "workshop", "course completion"
    ]

    sentence_starters = [
        "this", "the", "a", "an", "developed", "created",
        "implemented", "designed", "built", "used", "worked",
        "performed", "analyzed", "utilized", "achieved", "guided"
    ]

    current_proj_bold = ""
    current_proj_heur = ""

    for page in document:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                spans = line["spans"]
                if not spans:
                    continue

                line_text = " ".join(s["text"].strip() for s in spans if s["text"].strip()).strip()
                if not line_text:
                    continue

                bold_found = any("bold" in s.get("font", "").lower() or s.get("flags", 0) & 16 for s in spans)

                normalized = re.sub(r"[^a-zA-Z ]", "", line_text)
                normalized = re.sub(r"\s+", " ", normalized).strip().lower()

                if normalized in project_headings:
                    inside_projects = True
                    continue

                if inside_projects and normalized in stop_sections:
                    inside_projects = False
                    if current_proj_bold:
                        projects_bold.append(current_proj_bold.strip())
                        current_proj_bold = ""
                    continue

                if not inside_projects:
                    continue

                clean_line = re.sub(r"^[•●▪◦■□*\-]+\s*", "", line_text)
                clean_line = re.sub(r"^\d+[\.\)]\s*", "", clean_line).strip()
                if not clean_line:
                    continue

                lower_line = clean_line.lower()
                if any(w in lower_line for w in certificate_words):
                    continue

                first_w = clean_line.split()[0].lower() if clean_line.split() else ""

                if bold_found or (current_proj_bold and not current_proj_bold.rstrip().endswith((".", "!", "?")) and first_w not in sentence_starters):
                    if not current_proj_bold:
                        current_proj_bold = clean_line.rstrip(".:;,")
                    else:
                        current_proj_bold += " " + clean_line.rstrip(".:;,")
                else:
                    if current_proj_bold:
                        clean_b = current_proj_bold.strip()
                        if clean_b and clean_b not in projects_bold:
                            projects_bold.append(clean_b)
                        current_proj_bold = ""

                if first_w in sentence_starters:
                    if current_proj_heur:
                        clean_h = current_proj_heur.rstrip(".:;,").strip()
                        if clean_h and clean_h not in projects_heuristic:
                            projects_heuristic.append(clean_h)
                        current_proj_heur = ""
                else:
                    if not current_proj_heur:
                        current_proj_heur = clean_line
                    else:
                        if not current_proj_heur.rstrip().endswith((".", "!", "?")):
                            current_proj_heur += " " + clean_line
                        else:
                            clean_h = current_proj_heur.rstrip(".:;,").strip()
                            if clean_h and clean_h not in projects_heuristic:
                                projects_heuristic.append(clean_h)
                            current_proj_heur = clean_line

    if current_proj_bold:
        clean_b = current_proj_bold.strip()
        if clean_b and clean_b not in projects_bold:
            projects_bold.append(clean_b)

    if current_proj_heur:
        clean_h = current_proj_heur.rstrip(".:;,").strip()
        if clean_h and clean_h not in projects_heuristic:
            projects_heuristic.append(clean_h)

    document.close()

    final_bold = [p for p in projects_bold if 2 <= len(p.split()) <= 25 and p.split()[0].lower() not in sentence_starters]
    final_heuristic = [p for p in projects_heuristic if 2 <= len(p.split()) <= 25 and p.split()[0].lower() not in sentence_starters]

    return final_bold if final_bold else final_heuristic