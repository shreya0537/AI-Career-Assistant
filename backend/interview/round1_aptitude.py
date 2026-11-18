import streamlit as st
from backend.interview.cse.round1_aptitude import get_cse_aptitude
from backend.interview.ece.round1_aptitude import get_ece_aptitude
from backend.interview.mechanical.round1_aptitude import get_mech_aptitude
from backend.interview.civil.round1_aptitude import get_civil_aptitude
from backend.interview.scoring import calculate_round_summary
from backend.interview.question_pool import select_presented_questions


def get_aptitude_questions(branch="CSE", used_ids=None):
    """
    Generates 15-question pool for branch, then selects 5 questions for display.
    Preserves existing question count (5 MCQs).
    """
    if branch == "ECE":
        pool = get_ece_aptitude(used_ids=used_ids)
    elif branch == "Mechanical":
        pool = get_mech_aptitude(used_ids=used_ids)
    elif branch == "Civil":
        pool = get_civil_aptitude(used_ids=used_ids)
    else:
        pool = get_cse_aptitude(used_ids=used_ids)

    return select_presented_questions(pool, count=5, used_ids=used_ids)


def render_round1_aptitude(branch="CSE", is_submitted=False, used_ids=None):
    """Renders Round 1 Aptitude MCQs for the candidate's branch. Locks inputs if is_submitted=True."""
    st.markdown(f"### 📝 Round 1: Aptitude & Assessment ({branch})")
    st.caption(f"Branch-specific aptitude test covering Quantitative, Logical, and Verbal reasoning for **{branch}** Engineering.")

    if is_submitted:
        st.markdown(
            """
            <div style="background: #f0fdf4; border: 1px solid #22c55e; border-radius: 10px; padding: 10px 14px; margin-bottom: 15px; color: #15803d; font-weight: 700;">
                Round Submitted ✓ Answers for Round 1 are LOCKED and cannot be edited.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # Store presented questions in session state so they persist across reruns
    r1_key = f"r1_questions_pres_{branch}_{st.session_state.get('interview_attempt_id', 1)}"
    if r1_key not in st.session_state:
        st.session_state[r1_key] = get_aptitude_questions(branch=branch, used_ids=used_ids)

    questions = st.session_state[r1_key]
    user_selections = {}

    for q_idx, q in enumerate(questions):
        st.markdown(f"#### Question {q_idx + 1}: {q['category']}")
        st.write(f"**{q['question']}**")

        saved_choice = st.session_state.get(f"apt_choice_{q['id']}", "Select an answer...")
        options_list = ["Select an answer..."] + q["options"]
        opt_idx = options_list.index(saved_choice) if saved_choice in options_list else 0

        choice = st.radio(
            f"Select Answer for Q{q_idx + 1} {'' if not is_submitted else '[LOCKED]'}:",
            options=options_list,
            index=opt_idx,
            disabled=is_submitted,
            key=f"mcq_radio_{q['id']}"
        )

        st.session_state[f"apt_choice_{q['id']}"] = choice
        user_selections[q['id']] = choice

        if is_submitted and q.get("model_answer"):
            with st.expander("💡 View Detailed Model Answer"):
                st.info(q["model_answer"])

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    return questions, user_selections


def evaluate_round1_aptitude(questions, user_selections):
    """Evaluates Round 1 selections and returns summary metrics."""
    evaluations = []

    for q in questions:
        choice = user_selections.get(q['id'])
        if not choice or choice == "Select an answer...":
            evaluations.append({
                "question": q['question'],
                "category": q['category'],
                "attempted": False,
                "is_correct": False,
                "user_answer": "Unanswered",
                "correct_answer": q['correct_option'],
                "explanation": q['explanation'],
                "score": 0
            })
        else:
            is_corr = (choice == q['correct_option'])
            evaluations.append({
                "question": q['question'],
                "category": q['category'],
                "attempted": True,
                "is_correct": is_corr,
                "user_answer": choice,
                "correct_answer": q['correct_option'],
                "explanation": q['explanation'],
                "score": 100 if is_corr else 0
            })

    summary = calculate_round_summary(evaluations)
    summary["evaluations"] = evaluations
    return summary
