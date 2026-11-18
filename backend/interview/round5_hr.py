import streamlit as st
from backend.interview.cse.round5_hr import get_cse_hr
from backend.interview.ece.round5_hr import get_ece_hr
from backend.interview.mechanical.round5_hr import get_mech_hr
from backend.interview.civil.round5_hr import get_civil_hr
from backend.interview.scoring import evaluate_question_answer, calculate_round_summary
from backend.interview.speech import render_speech_and_text_input
from backend.interview.question_pool import select_presented_questions


def get_hr_questions(username, branch, skills, used_ids=None):
    """
    Generates 15-question pool for branch, then selects 5 questions for presentation.
    """
    if branch == "ECE":
        pool = get_ece_hr(username, skills, used_ids=used_ids)
    elif branch == "Mechanical":
        pool = get_mech_hr(username, skills, used_ids=used_ids)
    elif branch == "Civil":
        pool = get_civil_hr(username, skills, used_ids=used_ids)
    else:
        pool = get_cse_hr(username, skills, used_ids=used_ids)

    return select_presented_questions(pool, count=5, used_ids=used_ids)


def render_round5_hr(username, branch, skills, is_submitted=False, used_ids=None):
    """Renders Round 5 HR Questions with Verbal (Mic) & Text input support, and submission locking."""
    st.markdown(f"### 🤝 Round 5: HR & Behavioral Interview ({branch})")
    st.caption(f"Tailored for **{branch}** Engineering candidates. Evaluates communication clarity, relevance, confidence, completeness, and professionalism.")

    if is_submitted:
        st.markdown(
            """
            <div style="background: #f0fdf4; border: 1px solid #22c55e; border-radius: 10px; padding: 10px 14px; margin-bottom: 15px; color: #15803d; font-weight: 700;">
                Round Submitted ✓ Answers for Round 5 are LOCKED and cannot be edited.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    r5_key = f"r5_questions_pres_{branch}_{st.session_state.get('interview_attempt_id', 1)}"
    if r5_key not in st.session_state:
        st.session_state[r5_key] = get_hr_questions(username, branch, skills, used_ids=used_ids)

    questions = st.session_state[r5_key]
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

        saved_text = st.session_state.get(f"r5_ans_{q['id']}", "")

        # Dual Option: 🎤 Verbal Answer / ⌨️ Type Answer
        user_text = render_speech_and_text_input(
            q_key=q['id'],
            label=f"Your HR Response Q{q_idx + 1} ({diff}):",
            default_val=saved_text,
            disabled=is_submitted
        )

        st.session_state[f"r5_ans_{q['id']}"] = user_text
        user_answers[q['id']] = user_text

        if is_submitted and q.get("model_answer"):
            with st.expander("💡 View Detailed Model Answer"):
                st.info(q["model_answer"])

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    return questions, user_answers


def evaluate_round5_hr(questions, user_answers):
    """Evaluates Round 5 HR answers and returns summary metrics."""
    evaluations = []

    for q in questions:
        text = user_answers.get(q['id'], "").strip()
        acceptable = q.get("acceptable_answers", [])
        result = evaluate_question_answer(text, acceptable)
        result["question"] = q['question']
        result["category"] = q['category']
        result["difficulty"] = q.get("difficulty", "Standard")
        evaluations.append(result)

    summary = calculate_round_summary(evaluations)
    summary["evaluations"] = evaluations
    return summary
