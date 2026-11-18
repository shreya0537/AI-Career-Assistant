import re
from backend.constants import ENGINEERING_BRANCHES, BRANCH_FULL_NAMES

# Keyword patterns for education & branch detection
BRANCH_PATTERNS = {
    "CSE": {
        "degree": [
            r"\bcomputer\s+science\b", r"\bcse\b", r"\binformation\s+technology\b",
            r"\bsoftware\s+engineering\b", r"\bcomputer\s+engineering\b",
            r"\bcomp\s+sci\b", r"\bcs\b"
        ],
        "keywords": [
            "python", "java", "c++", "data structures", "algorithms", "sql", "dbms",
            "operating systems", "computer networks", "html", "css", "javascript",
            "react", "flask", "django", "machine learning", "deep learning", "nlp",
            "power bi", "cloud computing", "git", "rest api", "full stack", "web developer"
        ]
    },
    "ECE": {
        "degree": [
            r"\belectronics\s*(?:&|and)\s*communication\b", r"\bece\b", r"\bec\b",
            r"\belectronics\s+engineering\b", r"\btelecommunication\b", r"\bec\s+engineering\b"
        ],
        "keywords": [
            "embedded c", "microcontrollers", "arduino", "raspberry pi", "vlsi",
            "verilog", "vhdl", "matlab", "simulink", "pcb design", "digital electronics",
            "analog electronics", "communication systems", "signals and systems", "iot",
            "sensors", "microprocessors", "fpga", "rtos"
        ]
    },
    "Mechanical": {
        "degree": [
            r"\bmechanical\s+engineering\b", r"\bmech\b", r"\bmechanical\b",
            r"\bthermal\s+engineering\b", r"\bmanufacturing\s+engineering\b"
        ],
        "keywords": [
            "autocad", "solidworks", "catia", "ansys", "thermodynamics", "fluid mechanics",
            "strength of materials", "machine design", "cnc", "manufacturing processes",
            "heat transfer", "materials science", "production engineering", "cad/cam",
            "gd&t", "hvac", "mechatronics"
        ]
    },
    "Civil": {
        "degree": [
            r"\bcivil\s+engineering\b", r"\bcivil\b", r"\bstructural\s+engineering\b",
            r"\bgeotechnical\s+engineering\b", r"\bconstruction\s+engineering\b"
        ],
        "keywords": [
            r"staad\.pro", "etabs", "surveying", "concrete technology", "structural engineering",
            "soil mechanics", "geotechnical engineering", "transportation engineering",
            "environmental engineering", "hydraulics", "construction management", "estimation",
            "revit", "total station", "bim", "structural analysis"
        ]
    }
}


def detect_branch_from_resume(resume_text):
    """
    Analyzes uploaded resume text to automatically detect the candidate's engineering branch.
    Returns tuple: (detected_branch, confidence_score, explanation, is_confident)
    """
    if not resume_text or not resume_text.strip():
        return ("CSE", 0.0, "Resume text is empty or unreadable.", False)

    text_lower = resume_text.lower()
    scores = {b: 0 for b in ENGINEERING_BRANCHES}
    matched_evidences = {b: [] for b in ENGINEERING_BRANCHES}

    # 1. Degree & Education Section Match (Weight: 50 points per degree match)
    for branch, patterns in BRANCH_PATTERNS.items():
        for deg_pat in patterns["degree"]:
            matches = re.findall(deg_pat, text_lower)
            if matches:
                weight = 50 * len(matches)
                scores[branch] += weight
                matched_evidences[branch].append(f"Degree match: '{matches[0]}'")

    # 2. Skill & Terminology Match (Weight: 5 points per keyword match)
    for branch, patterns in BRANCH_PATTERNS.items():
        for kw in patterns["keywords"]:
            if kw == "c":
                pat = r"(?<![a-zA-z])c(?![a-zA-z\+\#])"
            else:
                pat = r"\b" + re.escape(kw) + r"\b"

            found = re.findall(pat, text_lower)
            if found:
                scores[branch] += 5 * len(found)
                matched_evidences[branch].append(f"Keyword: '{kw}'")

    top_branch = max(scores, key=scores.get)
    top_score = scores[top_branch]
    total_score = sum(scores.values())

    if total_score == 0:
        return ("CSE", 0.0, "Insufficient branch markers found in resume.", False)

    confidence_score = round(top_score / max(total_score, 1), 2)
    evidences = matched_evidences[top_branch][:3]
    evidence_str = ", ".join(evidences) if evidences else "Keyword analysis"

    # Confident threshold: Top score >= 20 and confidence_score >= 0.45
    is_confident = (top_score >= 20 and confidence_score >= 0.45)

    explanation = (
        f"Detected {BRANCH_FULL_NAMES[top_branch]} based on resume evidence ({evidence_str}) "
        f"with {int(confidence_score * 100)}% confidence."
    )

    return (top_branch, confidence_score, explanation, is_confident)
