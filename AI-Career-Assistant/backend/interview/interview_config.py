# =====================================================================
# CENTRALIZED INTERVIEW TIMINGS CONFIGURATION (PER BRANCH)
# =====================================================================

ROUND_TIMINGS = {
    "CSE": {
        "Round 1": 300,  # 5 minutes for Aptitude
        "Round 2": 600,  # 10 minutes for Coding
        "Round 3": 480,  # 8 minutes for Technical
        "Round 4": 480,  # 8 minutes for Project
        "Round 5": 360   # 6 minutes for HR
    },
    "ECE": {
        "Round 1": 300,
        "Round 2": 600,
        "Round 3": 480,
        "Round 4": 480,
        "Round 5": 360
    },
    "Mechanical": {
        "Round 1": 300,
        "Round 2": 600,
        "Round 3": 480,
        "Round 4": 480,
        "Round 5": 360
    },
    "Civil": {
        "Round 1": 300,
        "Round 2": 600,
        "Round 3": 480,
        "Round 4": 480,
        "Round 5": 360
    }
}


def get_branch_timings(branch):
    """Returns timing dictionary for the specified branch or default CSE."""
    return ROUND_TIMINGS.get(branch, ROUND_TIMINGS["CSE"])


# =====================================================================
# BRANCH-SPECIFIC 5-ROUND INTERVIEW NAMES
# =====================================================================

BRANCH_ROUND_NAMES = {
    "CSE": {
        "Round 1": "Aptitude",
        "Round 2": "Coding",
        "Round 3": "Core CS",
        "Round 4": "Project/Resume",
        "Round 5": "HR"
    },
    "Mechanical": {
        "Round 1": "Aptitude",
        "Round 2": "Mechanical Problem Solving",
        "Round 3": "Core Mechanical",
        "Round 4": "Project/Resume",
        "Round 5": "HR"
    },
    "Civil": {
        "Round 1": "Aptitude",
        "Round 2": "Civil Problem Solving",
        "Round 3": "Core Civil",
        "Round 4": "Project/Resume",
        "Round 5": "HR"
    },
    "ECE": {
        "Round 1": "Aptitude",
        "Round 2": "Electronics Problem Solving",
        "Round 3": "Core ECE",
        "Round 4": "Project/Resume",
        "Round 5": "HR"
    }
}


def get_branch_round_names(branch):
    """Returns round names dictionary for the specified branch or default CSE."""
    return BRANCH_ROUND_NAMES.get(branch, BRANCH_ROUND_NAMES["CSE"])


def get_round_name(branch, round_key):
    """Returns the branch-specific name for a specific round key (e.g. 'Round 2')."""
    branch_names = get_branch_round_names(branch)
    return branch_names.get(round_key, round_key)

