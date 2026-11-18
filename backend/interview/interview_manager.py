import streamlit as st
import datetime
from backend.ai.skills import extract_skills, extract_projects_from_pdf, get_job_roles_detailed
from backend.constants import BRANCH_FULL_NAMES, SKILL_ROADMAP_SUGGESTIONS
from backend.interview.interview_config import get_branch_timings, get_branch_round_names
from backend.interview.timer import render_round_timer_widget
from backend.interview.round1_aptitude import render_round1_aptitude, evaluate_round1_aptitude
from backend.interview.round2_coding import render_round2_coding, evaluate_round2_coding
from backend.interview.round3_technical import render_round3_technical, evaluate_round3_technical
from backend.interview.round4_project import render_round4_project, evaluate_round4_project
from backend.interview.round5_hr import render_round5_hr, evaluate_round5_hr


def generate_performance_analysis(round_summaries, branch):
    """
    Generates realistic Strong Areas and Areas Requiring Improvement based on actual candidate interview evaluation metrics.
    Does NOT simply list resume skills.
    """
    strong_areas = []
    improvement_areas = []

    b_names = get_branch_round_names(branch)
    r_names = {
        "Round 1": f"{b_names['Round 1']} & Analytical Logic",
        "Round 2": f"{b_names['Round 2']} & Technical Evaluation",
        "Round 3": f"{b_names['Round 3']} Fundamentals",
        "Round 4": f"{b_names['Round 4']} Defense",
        "Round 5": f"{b_names['Round 5']} & Behavioral Interview"
    }

    # Gather evaluations
    for r_k, summary in round_summaries.items():
        if summary is not None:
            sc = summary.get("score", 0)
            evals = summary.get("evaluations", [])
            r_title = r_names.get(r_k, r_k)

            # Analyze round score
            if sc >= 75:
                # Find specific high-scoring categories
                high_cats = [ev.get("category", "") for ev in evals if ev.get("is_correct", False) or ev.get("score", 0) >= 70]
                high_cat_str = (", ".join(high_cats[:2])) if high_cats else r_title
                strong_areas.append(f"You demonstrated strong accuracy ({sc:.0f}%) in {r_title}, particularly in {high_cat_str}.")
            elif sc >= 45:
                # Moderate performance
                low_cats = [ev.get("category", "") for ev in evals if not ev.get("is_correct", False) or ev.get("score", 0) < 70]
                low_cat_str = (", ".join(low_cats[:2])) if low_cats else r_title
                improvement_areas.append(f"Your performance in {r_title} ({sc:.0f}%) was moderate. Further revision is recommended in {low_cat_str}.")
            else:
                # Poor performance
                low_cats = [ev.get("category", "") for ev in evals if not ev.get("is_correct", False)]
                low_cat_str = (", ".join(low_cats[:2])) if low_cats else r_title
                improvement_areas.append(f"Priority area: {r_title} scored {sc:.0f}%. Key topics requiring study include {low_cat_str}.")

    if not strong_areas:
        strong_areas.append("You showed structured problem-solving approach across attempted questions.")

    if not improvement_areas:
        improvement_areas.append("All interview rounds scored above 75%! Continue maintaining your high accuracy and edge-case handling.")

    return strong_areas, improvement_areas


def reset_interview_state(retake=False):
    """Resets active interview state while preserving history across retakes."""
    if retake:
        # Save previous completed attempt if available
        if st.session_state.get("interview_score") is not None:
            if "interview_history" not in st.session_state:
                st.session_state.interview_history = []

            attempt_record = {
                "attempt_id": st.session_state.get("interview_attempt_id", 1),
                "branch": st.session_state.get("selected_branch", "CSE"),
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "overall_score": st.session_state.interview_score,
                "round_scores": dict(st.session_state.get("round_scores", {})),
                "round_summaries": dict(st.session_state.get("round_summaries", {}))
            }
            st.session_state.interview_history.append(attempt_record)

        # Increment attempt ID to force new question pools
        st.session_state.interview_attempt_id = st.session_state.get("interview_attempt_id", 1) + 1

    st.session_state.unlocked_round = 1
    st.session_state.interview_score = None
    st.session_state.just_completed_interview = False
    st.session_state.round_summaries = {
        "Round 1": None,
        "Round 2": None,
        "Round 3": None,
        "Round 4": None,
        "Round 5": None
    }
    st.session_state.round_scores = {
        "Round 1": None,
        "Round 2": None,
        "Round 3": None,
        "Round 4": None,
        "Round 5": None
    }


def interview_page():
    """Main Coordinator for the 5-Round Campus Interview Drive."""
    username = st.session_state.get("user", "Candidate")
    branch = st.session_state.get("selected_branch", "CSE")
    branch_full = BRANCH_FULL_NAMES.get(branch, branch)
    b_names = get_branch_round_names(branch)

    resume_text = st.session_state.get("resume_text", None)
    resume_pdf = st.session_state.get("resume_pdf", None)

    # Extract skills & projects
    skills = extract_skills(resume_text, branch=branch) if resume_text else []
    projects = extract_projects_from_pdf(resume_pdf) if resume_pdf else []

    # Session State Initialization
    if "interview_attempt_id" not in st.session_state:
        st.session_state.interview_attempt_id = 1

    if "unlocked_round" not in st.session_state:
        st.session_state.unlocked_round = 1

    if "round_summaries" not in st.session_state or not isinstance(st.session_state.round_summaries, dict):
        st.session_state.round_summaries = {
            "Round 1": None, "Round 2": None, "Round 3": None, "Round 4": None, "Round 5": None
        }

    if "round_scores" not in st.session_state or not isinstance(st.session_state.round_scores, dict):
        st.session_state.round_scores = {
            "Round 1": None, "Round 2": None, "Round 3": None, "Round 4": None, "Round 5": None
        }

    # Gather used question IDs from previous attempts to avoid repeating in retakes
    used_question_ids = set()
    if "interview_history" in st.session_state:
        for past in st.session_state.interview_history:
            for r_k, sm in past.get("round_summaries", {}).items():
                if sm and "evaluations" in sm:
                    for ev in sm["evaluations"]:
                        if "question" in ev:
                            used_question_ids.add(ev.get("question"))

    # Fetch branch timings
    timings = get_branch_timings(branch)

    # Top Header
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
                    border-radius: 18px; padding: 24px; color: white; margin-bottom: 20px;
                    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.3);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 0.82rem; font-weight: 700; color: #818cf8; text-transform: uppercase;">
                        ⚡ Enterprise Recruitment Drive Simulation • Attempt #{st.session_state.interview_attempt_id}
                    </div>
                    <h1 style="font-size: 1.85rem; font-weight: 800; margin: 4px 0 8px 0; color: #ffffff;">
                        🎤 5-Round Interview: {branch_full}
                    </h1>
                    <p style="font-size: 0.9rem; color: #cbd5e1; margin: 0;">
                        Complete the recruitment drive in order: Round 1 ({b_names['Round 1']}) ➔ Round 2 ({b_names['Round 2']}) ➔ Round 3 ({b_names['Round 3']}) ➔ Round 4 ({b_names['Round 4']}) ➔ Round 5 ({b_names['Round 5']}).
                    </p>
                </div>
                <div>
                    <span style="background: rgba(255,255,255,0.15); padding: 6px 14px; border-radius: 20px; font-weight: 700; font-size: 0.85rem;">
                        Attempt #{st.session_state.interview_attempt_id}
                    </span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Profile Info
    if resume_text:
        st.info(f"✅ **Active Profile:** Branch = **{branch_full}** | Parsed **{len(skills)} Skills** & **{len(projects)} Projects** from resume.")
    else:
        st.warning(f"⚠️ **Branch:** **{branch_full}** | Upload your PDF resume in **Resume Analysis** for personalized project and coding questions.")

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # =====================================================================
    # STEPPER PROGRESSION DASHBOARD
    # =====================================================================
    st.subheader("🧭 Interview Process")

    r_keys = ["Round 1", "Round 2", "Round 3", "Round 4", "Round 5"]
    r_names = [
        f"Round 1 – {b_names['Round 1']}",
        f"Round 2 – {b_names['Round 2']}",
        f"Round 3 – {b_names['Round 3']}",
        f"Round 4 – {b_names['Round 4']}",
        f"Round 5 – {b_names['Round 5']}"
    ]

    stepper_cols = st.columns(5)
    for i in range(5):
        r_num = i + 1
        r_key = r_keys[i]
        r_label = r_names[i]
        summary = st.session_state.round_summaries.get(r_key)

        with stepper_cols[i]:
            if summary is not None:
                st.markdown(
                    f"""
                    <div style="background: #f0fdf4; border: 1.5px solid #22c55e; border-radius: 12px; padding: 12px; text-align: center;">
                        <div style="font-size: 0.78rem; font-weight: 800; color: #15803d;">✅ {r_label}</div>
                        <div style="font-size: 1.2rem; font-weight: 800; color: #16a34a; margin-top: 4px;">{summary['score']:.1f}%</div>
                        <div style="font-size: 0.7rem; color: #166534; font-weight: 600;">{summary['attempted']}/{summary['total']} Attempted</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif r_num <= st.session_state.unlocked_round:
                st.markdown(
                    f"""
                    <div style="background: #eff6ff; border: 2px solid #3b82f6; border-radius: 12px; padding: 12px; text-align: center;">
                        <div style="font-size: 0.78rem; font-weight: 800; color: #1d4ed8;">🔓 {r_label}</div>
                        <div style="font-size: 0.95rem; font-weight: 800; color: #2563eb; margin-top: 6px;">UNLOCKED</div>
                        <div style="font-size: 0.7rem; color: #1e40af; font-weight: 600;">Ready</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div style="background: #f8fafc; border: 1.5px dashed #cbd5e1; border-radius: 12px; padding: 12px; text-align: center; opacity: 0.75;">
                        <div style="font-size: 0.78rem; font-weight: 700; color: #64748b;">🔒 {r_label}</div>
                        <div style="font-size: 0.9rem; font-weight: 700; color: #94a3b8; margin-top: 6px;">LOCKED</div>
                        <div style="font-size: 0.7rem; color: #94a3b8;">Complete R{r_num - 1}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.divider()

    # Dynamic Tabs
    tab_labels = []
    for i in range(5):
        r_num = i + 1
        r_key = r_keys[i]
        summary = st.session_state.round_summaries.get(r_key)
        if summary is not None:
            tab_labels.append(f"✅ R{r_num}: {b_names[r_key]} ({summary['score']:.1f}%)")
        elif r_num <= st.session_state.unlocked_round:
            tab_labels.append(f"🔓 R{r_num}: {b_names[r_key]}")
        else:
            tab_labels.append(f"🔒 R{r_num}: {b_names[r_key]} (Locked)")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_labels)

    # TAB 1: ROUND 1 – APTITUDE
    with tab1:
        is_sub_1 = (st.session_state.round_summaries["Round 1"] is not None)
        time_expired_1 = render_round_timer_widget("Round 1", "R1", timings["Round 1"], is_submitted=is_sub_1)
        questions_r1, user_sel_r1 = render_round1_aptitude(branch=branch, is_submitted=is_sub_1, used_ids=used_question_ids)

        if not is_sub_1:
            if st.button(f"📊 Submit Round 1 ({b_names['Round 1']})", type="primary", key="btn_sub_r1") or time_expired_1:
                summary = evaluate_round1_aptitude(questions_r1, user_sel_r1)
                st.session_state.round_summaries["Round 1"] = summary
                st.session_state.round_scores["Round 1"] = summary["score"]
                st.session_state.unlocked_round = max(st.session_state.unlocked_round, 2)
                st.rerun()

    # TAB 2: ROUND 2 – CODING / PROBLEM SOLVING
    with tab2:
        if st.session_state.unlocked_round < 2 and st.session_state.round_summaries["Round 1"] is None:
            st.warning(f"🔒 **Round 2 is LOCKED.** Complete and submit Round 1 ({b_names['Round 1']}) first to unlock Round 2.")
        else:
            is_sub_2 = (st.session_state.round_summaries["Round 2"] is not None)
            time_expired_2 = render_round_timer_widget("Round 2", "R2", timings["Round 2"], is_submitted=is_sub_2)
            questions_r2, user_ans_r2 = render_round2_coding(branch, skills=skills, projects=projects, is_submitted=is_sub_2, used_ids=used_question_ids, resume_text=resume_text)

            if not is_sub_2:
                if st.button(f"📊 Submit Round 2 ({b_names['Round 2']})", type="primary", key="btn_sub_r2") or time_expired_2:
                    summary = evaluate_round2_coding(questions_r2, user_ans_r2)
                    st.session_state.round_summaries["Round 2"] = summary
                    st.session_state.round_scores["Round 2"] = summary["score"]
                    st.session_state.unlocked_round = max(st.session_state.unlocked_round, 3)
                    st.rerun()

    # TAB 3: ROUND 3 – TECHNICAL CORE
    with tab3:
        if st.session_state.unlocked_round < 3 and st.session_state.round_summaries["Round 2"] is None:
            st.warning(f"🔒 **Round 3 is LOCKED.** Complete and submit Round 2 ({b_names['Round 2']}) first to unlock Round 3.")
        else:
            is_sub_3 = (st.session_state.round_summaries["Round 3"] is not None)
            time_expired_3 = render_round_timer_widget("Round 3", "R3", timings["Round 3"], is_submitted=is_sub_3)
            questions_r3, user_ans_r3 = render_round3_technical(branch, is_submitted=is_sub_3, used_ids=used_question_ids)

            if not is_sub_3:
                if st.button(f"📊 Submit Round 3 ({b_names['Round 3']})", type="primary", key="btn_sub_r3") or time_expired_3:
                    summary = evaluate_round3_technical(questions_r3, user_ans_r3)
                    st.session_state.round_summaries["Round 3"] = summary
                    st.session_state.round_scores["Round 3"] = summary["score"]
                    st.session_state.unlocked_round = max(st.session_state.unlocked_round, 4)
                    st.rerun()

    # TAB 4: ROUND 4 – PROJECT / RESUME
    with tab4:
        if st.session_state.unlocked_round < 4 and st.session_state.round_summaries["Round 3"] is None:
            st.warning(f"🔒 **Round 4 is LOCKED.** Complete and submit Round 3 ({b_names['Round 3']}) first to unlock Round 4.")
        else:
            is_sub_4 = (st.session_state.round_summaries["Round 4"] is not None)
            time_expired_4 = render_round_timer_widget("Round 4", "R4", timings["Round 4"], is_submitted=is_sub_4)
            questions_r4, user_ans_r4 = render_round4_project(branch, projects, skills, is_submitted=is_sub_4, used_ids=used_question_ids)

            if not is_sub_4:
                if st.button(f"📊 Submit Round 4 ({b_names['Round 4']})", type="primary", key="btn_sub_r4") or time_expired_4:
                    summary = evaluate_round4_project(questions_r4, user_ans_r4)
                    st.session_state.round_summaries["Round 4"] = summary
                    st.session_state.round_scores["Round 4"] = summary["score"]
                    st.session_state.unlocked_round = max(st.session_state.unlocked_round, 5)
                    st.rerun()

    # TAB 5: ROUND 5 – HR INTERVIEW
    with tab5:
        if st.session_state.unlocked_round < 5 and st.session_state.round_summaries["Round 4"] is None:
            st.warning(f"🔒 **Round 5 is LOCKED.** Complete and submit Round 4 ({b_names['Round 4']}) first to unlock Round 5.")
        else:
            is_sub_5 = (st.session_state.round_summaries["Round 5"] is not None)
            time_expired_5 = render_round_timer_widget("Round 5", "R5", timings["Round 5"], is_submitted=is_sub_5)
            questions_r5, user_ans_r5 = render_round5_hr(username, branch, skills, is_submitted=is_sub_5, used_ids=used_question_ids)

            if not is_sub_5:
                if st.button(f"📊 Submit Round 5 & Generate Final Result", type="primary", key="btn_sub_r5") or time_expired_5:
                    summary = evaluate_round5_hr(questions_r5, user_ans_r5)
                    st.session_state.round_summaries["Round 5"] = summary
                    st.session_state.round_scores["Round 5"] = summary["score"]

                    completed_scores = [sm['score'] for sm in st.session_state.round_summaries.values() if sm is not None]
                    overall_score = (sum(completed_scores) / len(completed_scores)) if completed_scores else 0

                    st.session_state.interview_score = overall_score
                    st.session_state.just_completed_interview = True
                    st.rerun()


    # =====================================================================
    # FINAL RESULT REPORT & RETAKE INTERVIEW
    # =====================================================================
    completed_rounds_list = [sm for sm in st.session_state.round_summaries.values() if sm is not None]

    if len(completed_rounds_list) == 5:
        st.divider()
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, #059669 0%, #10b981 100%);
                        border-radius: 18px; padding: 24px; color: white; margin-bottom: 24px;
                        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.3);">
                <div style="font-size: 0.85rem; font-weight: 700; color: #d1fae5; text-transform: uppercase;">
                    🏆 Campus Recruitment Drive Complete • Attempt #{st.session_state.interview_attempt_id}
                </div>
                <h2 style="font-size: 1.9rem; font-weight: 800; margin: 4px 0;">
                    5 ROUND MOCK INTERVIEW RESULT
                </h2>
                <div style="font-size: 1.1rem; font-weight: 700; margin-top: 6px;">
                    Branch: {branch_full} | Overall Score: {st.session_state.interview_score:.1f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Generate Realistic Strong Areas & Areas Requiring Improvement based on actual performance
        strong_areas, improvement_areas = generate_performance_analysis(st.session_state.round_summaries, branch)

        col_str, col_imp = st.columns(2)

        with col_str:
            st.subheader("🌟 Realistic Strong Areas")
            for sa in strong_areas:
                st.markdown(f"✅ **{sa}**")

        with col_imp:
            st.subheader("⚠️ Areas Requiring Improvement")
            for ia in improvement_areas:
                st.markdown(f"📌 **{ia}**")

        st.divider()

        # Retake Interview Button
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🔄 Retake Interview (Generate Fresh Question Set)", type="primary", key="btn_retake_interview_page"):
                reset_interview_state(retake=True)
                st.rerun()

        with col_btn2:
            if st.button("🚀 View Updated Placement Dashboard", key="btn_go_dash_final"):
                st.session_state.nav_module = "Dashboard"
                st.rerun()

        # Display Previous Attempts History if exists
        if "interview_history" in st.session_state and st.session_state.interview_history:
            st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
            with st.expander(f"📜 View Previous Interview Attempts ({len(st.session_state.interview_history)})"):
                for past in reversed(st.session_state.interview_history):
                    st.write(f"**Attempt #{past['attempt_id']}** ({past['date']}) - **Branch:** {past['branch']} - **Score:** {past['overall_score']:.1f}%")
                    for r_k, sc in past["round_scores"].items():
                        if sc is not None:
                            st.caption(f"- {r_k}: {sc:.1f}%")
                    st.divider()
