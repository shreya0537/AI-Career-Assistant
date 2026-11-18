# =====================================================================
# PLACEMENT READINESS EVALUATION ENGINE
# =====================================================================

def compute_readiness_score(resume_score, interview_score):
    """
    Computes a weighted placement readiness score out of 100%.
    
    Formula:
    - If both Resume and Interview are completed:
        Readiness = (0.4 * Resume Score) + (0.6 * Interview Score)
    - If only Resume is analyzed:
        Readiness = 0.5 * Resume Score
    - If neither is completed:
        Readiness = 0
    """
    if resume_score is not None and interview_score is not None:
        return round((resume_score * 0.4) + (interview_score * 0.6))
    elif resume_score is not None:
        return round(resume_score * 0.5)
    return 0


def get_readiness_status(readiness_score, has_resume, has_interview):
    """
    Evaluates candidate status and returns:
    (badge_label, badge_color, description)
    """
    if not has_resume:
        return (
            "⚪ Profile Incomplete",
            "#64748b",
            "Upload your resume to begin your placement preparation journey."
        )

    if not has_interview:
        return (
            "🟡 Interview Pending",
            "#d97706",
            "Resume analyzed! Take the AI Mock Interview to complete your profile."
        )

    if readiness_score >= 80:
        return (
            "🟢 Placement Ready",
            "#16a34a",
            "Outstanding preparation! You are well-positioned for placement drives."
        )
    elif readiness_score >= 60:
        return (
            "🔵 Strong Candidate",
            "#2563eb",
            "Good progress. Refine your answers to boost your readiness index."
        )
    else:
        return (
            "🟠 Needs Practice",
            "#ea580c",
            "Additional technical preparation and mock interview practice recommended."
        )
