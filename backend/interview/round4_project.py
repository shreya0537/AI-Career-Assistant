import streamlit as st
from backend.interview.cse.round4_project import get_cse_project_questions
from backend.interview.ece.round4_project import get_ece_project_questions
from backend.interview.mechanical.round4_project import get_mech_project_questions
from backend.interview.civil.round4_project import get_civil_project_questions
from backend.interview.scoring import evaluate_question_answer, calculate_round_summary
from backend.interview.speech import render_speech_and_text_input
from backend.interview.question_pool import select_presented_questions


def get_round4_questions(branch, projects, skills, used_ids=None):
    """
    Generates 15-question pool for branch, then selects 5 questions (1 Easy, 2 Medium, 2 Hard) for presentation.
    """
    if branch == "ECE":
        pool = get_ece_project_questions(projects, skills, used_ids=used_ids)
    elif branch == "Mechanical":
        pool = get_mech_project_questions(projects, skills, used_ids=used_ids)
    elif branch == "Civil":
        pool = get_civil_project_questions(projects, skills, used_ids=used_ids)
    else:
        pool = get_cse_project_questions(projects, skills, used_ids=used_ids)

    return select_presented_questions(pool, count=5, used_ids=used_ids)


def render_round4_project(branch, projects, skills, is_submitted=False, used_ids=None):
    """Renders Round 4 Project Questions with Verbal (Mic) & Text input support, and submission locking."""
    st.markdown(f"### 📁 Round 4: Project & Resume Technical ({branch})")
    st.caption(f"Contains exactly 5 questions (1 Easy + 2 Medium + 2 Hard) connected to your uploaded PDF resume for **{branch}**.")

    if is_submitted:
        st.markdown(
            """
            <div style="background: #f0fdf4; border: 1px solid #22c55e; border-radius: 10px; padding: 10px 14px; margin-bottom: 15px; color: #15803d; font-weight: 700;">
                Round Submitted ✓ Answers for Round 4 are LOCKED and cannot be edited.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    r4_key = f"r4_questions_pres_{branch}_{st.session_state.get('interview_attempt_id', 1)}"
    if r4_key not in st.session_state:
        st.session_state[r4_key] = get_round4_questions(branch, projects, skills, used_ids=used_ids)

    questions = st.session_state[r4_key]
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

        saved_text = st.session_state.get(f"r4_ans_{q['id']}", "")

        # Dual Option: 🎤 Verbal Answer / ⌨️ Type Answer
        user_text = render_speech_and_text_input(
            q_key=q['id'],
            label=f"Your Project Response Q{q_idx + 1} ({diff}):",
            default_val=saved_text,
            disabled=is_submitted
        )

        st.session_state[f"r4_ans_{q['id']}"] = user_text
        user_answers[q['id']] = user_text

        if is_submitted and q.get("model_answer"):
            with st.expander("💡 View Detailed Model Answer"):
                st.info(q["model_answer"])

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    return questions, user_answers


def evaluate_round4_project(questions, user_answers):
    """Evaluates Round 4 project answers and returns summary metrics."""
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
