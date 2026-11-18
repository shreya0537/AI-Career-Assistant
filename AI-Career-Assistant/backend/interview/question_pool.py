import random
import re
import streamlit as st


def extract_mentioned_programming_languages(skills=None, resume_text=""):
    """
    Identifies programming languages mentioned in candidate's skills list or resume text.
    Returns list of matched programming language names (e.g. ['Python', 'SQL', 'C++']).
    """
    known_langs = {
        "python": "Python",
        "java": "Java",
        "c++": "C++",
        "cpp": "C++",
        "c": "C",
        "c#": "C#",
        "csharp": "C#",
        "javascript": "JavaScript",
        "js": "JavaScript",
        "typescript": "TypeScript",
        "ts": "TypeScript",
        "go": "Go",
        "golang": "Go",
        "rust": "Rust",
        "ruby": "Ruby",
        "php": "PHP",
        "sql": "SQL",
        "html": "HTML",
        "css": "CSS",
        "r": "R",
        "swift": "Swift",
        "kotlin": "Kotlin",
        "matlab": "MATLAB",
        "embedded c": "Embedded C",
        "verilog": "Verilog",
        "vhdl": "VHDL",
        "assembly": "Assembly"
    }

    skills = skills or []
    found = set()

    for s in skills:
        s_clean = s.strip().lower()
        if s_clean in known_langs:
            found.add(known_langs[s_clean])
        else:
            for k, name in known_langs.items():
                if len(k) > 1 and k in s_clean:
                    found.add(name)

    if resume_text:
        txt_lower = resume_text.lower()
        for k, name in known_langs.items():
            if k in ["c", "r"]:
                pattern = r'\b' + k + r'\b'
            elif k in ["c++", "c#"]:
                pattern = re.escape(k)
            else:
                pattern = r'\b' + re.escape(k) + r'\b'

            if re.search(pattern, txt_lower):
                found.add(name)

    return sorted(list(found))



def clear_cached_interview_questions():
    """
    Clears all cached question sets and user answers from session state
    so that new resume uploads, branch changes, or retakes generate
    100% fresh questions based on the latest resume and branch.
    """
    keys_to_remove = [
        k for k in st.session_state.keys()
        if k.startswith("r1_questions_pres_") or
        k.startswith("r2_questions_pres_") or
        k.startswith("r3_questions_pres_") or
        k.startswith("r4_questions_pres_") or
        k.startswith("r5_questions_pres_") or
        k.startswith("apt_choice_") or
        k.startswith("r2_ans_") or
        k.startswith("r3_ans_") or
        k.startswith("r4_ans_") or
        k.startswith("r5_ans_") or
        k.startswith("mcq_radio_")
    ]
    for k in keys_to_remove:
        del st.session_state[k]


def select_presented_questions(pool, count, used_ids=None):
    """
    Given a pool of 15 generated questions for a round:
    - If count == 3 (Round 2): selects EXACTLY 1 Easy, 1 Medium, 1 Hard.
    - If count == 5 (Rounds 1, 3, 4, 5): selects EXACTLY 1 Easy, 2 Medium, 2 Hard.
    Filters out questions in used_ids (from previous interview retakes) if possible.
    """
    if not pool:
        return []

    used_set = set(used_ids or [])
    available = [q for q in pool if q.get("id") not in used_set]
    if len(available) < count:
        available = list(pool)

    easy_q = [q for q in available if q.get("difficulty") == "Easy"]
    med_q = [q for q in available if q.get("difficulty") == "Medium"]
    hard_q = [q for q in available if q.get("difficulty") == "Hard"]

    # Fallbacks in case any difficulty subset is empty
    if not easy_q: easy_q = list(available)
    if not med_q: med_q = list(available)
    if not hard_q: hard_q = list(available)

    selected = []

    if count == 3:
        # Round 2: 1 Easy, 1 Medium, 1 Hard
        if easy_q:
            selected.append(easy_q[0])
        for q in med_q:
            if q not in selected:
                selected.append(q)
                break
        for q in hard_q:
            if q not in selected:
                selected.append(q)
                break

    elif count == 5:
        # Rounds 1, 3, 4, 5: 1 Easy, 2 Medium, 2 Hard
        if easy_q:
            selected.append(easy_q[0])
        for q in med_q:
            if q not in selected and len([x for x in selected if x.get("difficulty") == "Medium"]) < 2:
                selected.append(q)
        for q in hard_q:
            if q not in selected and len([x for x in selected if x.get("difficulty") == "Hard"]) < 2:
                selected.append(q)

    # Fill up if needed to reach target count
    for q in available:
        if len(selected) >= count:
            break
        if q not in selected:
            selected.append(q)

    for q in pool:
        if len(selected) >= count:
            break
        if q not in selected:
            selected.append(q)

    return selected[:count]

