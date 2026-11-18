import streamlit as st
from backend.interview.cse.round2_coding import get_cse_coding
from backend.interview.ece.round2_coding import get_ece_coding
from backend.interview.mechanical.round2_coding import get_mech_coding
from backend.interview.civil.round2_coding import get_civil_coding
from backend.interview.scoring import evaluate_question_answer, calculate_round_summary
from backend.interview.question_pool import select_presented_questions, extract_mentioned_programming_languages
from backend.interview.interview_config import get_round_name


def get_round2_questions(branch, skills=None, projects=None, used_ids=None, resume_text=""):
    """
    Generates 15-question pool for branch based on programming language rules,
    then selects 3 questions (1 Easy, 1 Medium, 1 Hard) for presentation.
    """
    skills = skills or []
    projects = projects or []

    if branch == "ECE":
        pool = get_ece_coding(skills, projects, used_ids=used_ids, resume_text=resume_text)
    elif branch == "Mechanical":
        pool = get_mech_coding(skills, projects, used_ids=used_ids, resume_text=resume_text)
    elif branch == "Civil":
        pool = get_civil_coding(skills, projects, used_ids=used_ids, resume_text=resume_text)
    else:
        pool = get_cse_coding(skills, projects, used_ids=used_ids, resume_text=resume_text)

    return select_presented_questions(pool, count=3, used_ids=used_ids)


def render_round2_coding(branch, skills=None, projects=None, is_submitted=False, used_ids=None, resume_text=""):
    """Renders Round 2 Problem Solving / Coding Questions tailored by branch & mentioned programming languages."""
    skills = skills or []
    projects = projects or []
    r2_name = get_round_name(branch, "Round 2")

    mentioned_langs = extract_mentioned_programming_languages(skills, resume_text)

    # Determine if Round 2 is Coding vs Non-Coding Problem Solving
    if branch == "CSE":
        is_coding = True
    elif branch == "ECE":
        is_coding = bool(mentioned_langs)
    else:  # Civil or Mechanical
        is_coding = False

    if is_coding:
        st.markdown(f"### 💻 Round 2: {r2_name} ({branch}) — Coding & Programming Assessment")
        if mentioned_langs:
            st.info(f"📄 **Language-Based Coding Assessment Active:** Questions generated based on programming language(s) mentioned in resume: **{', '.join(mentioned_langs)}**.")
        else:
            st.caption(f"Customized coding assessment tailored for **{branch}** candidates.")
    else:
        st.markdown(f"### ⚙️ Round 2: {r2_name} ({branch}) — Technical Problem Solving (Non-Coding)")
        if branch == "ECE":
            st.info("ℹ️ **Core Electronics Problem Solving Active:** No programming languages were detected in resume, so Round 2 evaluates non-coding hardware, circuit, and signal analysis capabilities.")
        else:
            st.info(f"⚙️ **{branch} Engineering Problem Solving Active:** Non-coding domain calculations, formulas, and technical problem-solving evaluation.")

    if is_submitted:
        st.markdown(
            """
            <div style="background: #f0fdf4; border: 1px solid #22c55e; border-radius: 10px; padding: 10px 14px; margin-bottom: 15px; color: #15803d; font-weight: 700;">
                Round Submitted ✓ Answers for Round 2 are LOCKED and cannot be edited.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    r2_key = f"r2_questions_pres_{branch}_{st.session_state.get('interview_attempt_id', 1)}"
    if r2_key not in st.session_state:
        st.session_state[r2_key] = get_round2_questions(branch, skills=skills, projects=projects, used_ids=used_ids, resume_text=resume_text)

    questions = st.session_state[r2_key]
    user_answers = {}

    for q_idx, q in enumerate(questions):
        diff = q.get("difficulty", f"Level {q_idx + 1}")
        diff_color = "#16a34a" if diff == "Easy" else ("#d97706" if diff == "Medium" else "#dc2626")

        st.markdown(
            f"""
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                <span style="font-weight: 800; font-size: 1.05rem; color: #1e293b;">Question {q_idx + 1}: {q['category']}</span>
                <span style="background: {diff_color}; color: white; padding: 2px 10px; border-radius: 12px; font-weight: 700; font-size: 0.75rem;">
                    {diff}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(f"**Q:** {q['question']}")

        if q.get("expected_input_output"):
            st.caption(f"**Expected Input/Output:**\n```\n{q['expected_input_output']}\n```")

        saved_text = st.session_state.get(f"r2_ans_{q['id']}", "")

        if is_coding:
            input_label = f"Write your code / logic solution for Q{q_idx + 1} ({diff}) {'' if not is_submitted else '[LOCKED]'}:"
            input_ph = f"Enter executable code or programming logic for {branch}..."
        else:
            input_label = f"Write your step-by-step engineering solution / calculations for Q{q_idx + 1} ({diff}) {'' if not is_submitted else '[LOCKED]'}:"
            input_ph = f"Enter engineering formulas, calculation steps, and technical solution for {branch}..."

        ans = st.text_area(
            input_label,
            value=saved_text,
            height=140,
            disabled=is_submitted,
            key=f"r2_coding_input_{q['id']}",
            placeholder=input_ph
        )
        st.session_state[f"r2_ans_{q['id']}"] = ans
        user_answers[q['id']] = ans

        if is_submitted or st.session_state.get("show_model_solutions", False):
            if q.get("solution_code") or q.get("model_answer"):
                expander_title = "💻 View Executable Code Solution & Complexity Analysis" if is_coding else "📋 View Engineering Solution & Step-by-Step Calculation"
                with st.expander(expander_title):
                    if q.get("solution_code"):
                        st.code(q["solution_code"], language="python")
                    if q.get("time_complexity") and is_coding:
                        st.write(f"⏱️ **Time Complexity:** {q['time_complexity']}")
                    if q.get("space_complexity") and is_coding:
                        st.write(f"💾 **Space Complexity:** {q['space_complexity']}")
                    if q.get("model_answer"):
                        st.info(q["model_answer"])

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    return questions, user_answers


def evaluate_round2_coding(questions, user_answers):
    """Evaluates Round 2 answers and returns summary metrics."""
    evaluations = []

    for q in questions:
        text = user_answers.get(q['id'], "").strip()
        acceptable = q.get("acceptable_answers", q.get("answers", []))
        result = evaluate_question_answer(text, acceptable)
        result["question"] = q['question']
        result["category"] = q['category']
        result["difficulty"] = q.get("difficulty", "Standard")
        evaluations.append(result)

    summary = calculate_round_summary(evaluations)
    summary["evaluations"] = evaluations
    return summary
