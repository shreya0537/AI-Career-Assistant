import streamlit as st

# Import AI extractors & scoring
from backend.ai.skills import extract_skills, get_job_roles_detailed, extract_projects_from_pdf
from backend.ai.scoring import calculate_resume_score_detailed
from backend.ai.readiness import compute_readiness_score, get_readiness_status
from backend.ai.branch_detection import detect_branch_from_resume
from backend.interview.interview_manager import generate_performance_analysis, reset_interview_state
from backend.interview.interview_config import get_branch_round_names
from backend.constants import SKILL_DOMAINS, SKILL_ROADMAP_SUGGESTIONS, BRANCH_FULL_NAMES


# =====================================================================
# RENDER HELPER: TOP CENTER PROJECT BRANDING HEADER
# =====================================================================
def render_top_project_header():
    st.markdown(
        """
        <div class="top-brand-header">
            <div class="top-brand-badge">⚡ Placement Analytics & Multi-Branch Interview Platform</div>
            <h1 class="top-brand-title">🤖 AI-Driven Career Assistant</h1>
            <p class="top-brand-subtitle">
                Resume Intelligence, 100% Weighted Scoring & 5-Round Campus Evaluation
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================================
# RENDER HELPER: CELEBRATION BANNER
# =====================================================================
def check_and_render_celebration(interview_score, readiness_score):
    if st.session_state.get("just_completed_interview", False):
        st.markdown(
            f"""
            <div class="celebration-banner">
                <div class="celebration-icon">🎉</div>
                <div>
                    <div class="celebration-title">5-Round Recruitment Drive Completed & Evaluated!</div>
                    <div class="celebration-desc">
                        Congratulations! Your overall interview score reached <strong>{interview_score:.0f}%</strong>.
                        Your overall Placement Readiness Index has updated to <strong>{readiness_score}%</strong>!
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.session_state.just_completed_interview = False


# =====================================================================
# RENDER HELPER: CANDIDATE HERO BANNER
# =====================================================================
def render_candidate_hero(username, branch, badge_label, badge_color, badge_desc):
    branch_full = BRANCH_FULL_NAMES.get(branch, branch)
    st.markdown(
        f"""
        <div class="dashboard-hero">
            <div class="dashboard-hero-header">
                <div>
                    <div class="dashboard-hero-tag">🎓 {branch_full} • Candidate Evaluation Hub</div>
                    <h1 class="dashboard-hero-title">Candidate Profile: {username} 👋</h1>
                    <p class="dashboard-hero-desc">{badge_desc}</p>
                </div>
                <div class="dashboard-badge-box">
                    <div class="dashboard-badge-label">Placement Readiness</div>
                    <div class="dashboard-status-badge" style="color: {badge_color};">
                        {badge_label}
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================================
# RENDER HELPER: READINESS GAUGE METER
# =====================================================================
def render_readiness_meter(readiness_score):
    st.markdown(
        f"""
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 18px; padding: 20px 24px; margin-bottom: 22px; box-shadow: 0 4px 14px rgba(0,0,0,0.03);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-weight: 700; color: #1e293b; font-size: 1.02rem;">🎯 Overall Placement Readiness Index</span>
                <span style="font-size: 1.45rem; font-weight: 800; color: #4f46e5;">{readiness_score}%</span>
            </div>
            <div class="readiness-meter-container">
                <div class="readiness-meter-bar" style="width: {max(readiness_score, 4)}%;"></div>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: #64748b; font-weight: 600;">
                <span>⚪ 0% Start</span>
                <span>🟡 50% Resume Parsed</span>
                <span>🟢 80%+ Placement Ready 🚀</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================================
# RENDER HELPER: TOP KPI METRICS
# =====================================================================
def render_kpi_cards(resume_score, skills_count, top_role, interview_score, readiness_score):
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        res_display = f"{resume_score}%" if resume_score is not None else "Not Uploaded"
        st.metric("📄 100% Resume Score", res_display, help="Weighted 100-point score derived from Skills (30%), Education (15%), Projects (20%), Experience (15%), Certs (5%), Structure (10%), and Achievements (5%).")

    with col2:
        st.metric("🛠️ Verified Skills", skills_count, help="Verified technical skills extracted from resume.")

    with col3:
        st.metric("🎯 Top Role Match", top_role, help="Primary matched job role from authoritative dataset.")

    with col4:
        int_display = f"{interview_score:.0f}%" if interview_score is not None else "Pending"
        st.metric("🎤 5-Round Score", int_display, help="Overall average score evaluated across completed interview rounds.")

    with col5:
        st.metric("🏆 Readiness Index", f"{readiness_score}%", help="Combined placement readiness index based on Resume + Interview scores.")


# =====================================================================
# RENDER HELPER: COMPREHENSIVE RESUME ANALYSIS & SCORE BREAKDOWN
# =====================================================================
def render_comprehensive_resume_results(score_details, resume_text, skills, projects):
    st.subheader("📄 Comprehensive Resume Analysis & Score Breakdown")
    st.caption("All detailed evaluation results from your uploaded PDF resume are displayed below.")

    if not score_details:
        st.info("ℹ️ Upload your PDF resume in **Resume Analysis** to generate a complete section-wise breakdown, strengths, missing details, and improvement suggestions.")
        return

    col_score_left, col_details_right = st.columns([0.8, 1.2])

    with col_score_left:
        st.markdown(
            f"""
            <div style="background: white; border: 2px solid #6366f1; border-radius: 18px; padding: 22px; text-align: center; box-shadow: 0 4px 14px rgba(0,0,0,0.05);">
                <div style="font-size: 0.85rem; font-weight: 700; color: #64748b; text-transform: uppercase;">100% Weighted Resume Score</div>
                <div style="font-size: 3.2rem; font-weight: 900; color: #4f46e5; margin: 8px 0;">{score_details['overall_score']}%</div>
                <div style="font-size: 0.85rem; font-weight: 700; color: {'#16a34a' if score_details['overall_score']>=70 else '#d97706'};">
                    {'🏆 Outstanding Resume Profile' if score_details['overall_score']>=70 else '⏳ Enhancement Recommended'}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        st.markdown("#### 📊 Section-Wise Score Breakdown")

        for sec, info in score_details["section_scores"].items():
            sc = info["score"]
            mx = info["max"]
            pct = info["percentage"]
            st.write(f"**{sec} ({mx}% weight):** **{sc}/{mx} pts** ({pct}%)")
            st.progress(pct / 100)

    with col_details_right:
        st.markdown("#### 🌟 Resume Strengths")
        if score_details.get("strengths"):
            for s in score_details["strengths"]:
                st.markdown(f"✅ **{s}**")
        else:
            st.info("Upload detailed sections to generate resume strengths.")

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        st.markdown("#### ⚠️ Missing Information")
        if score_details.get("missing_info"):
            for m in score_details["missing_info"]:
                st.markdown(f"📌 **{m}**")
        else:
            st.markdown("🎉 **No critical missing information detected!**")

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        st.markdown("#### 🚀 Specific Improvement Suggestions")
        if score_details.get("improvement_suggestions"):
            for imp in score_details["improvement_suggestions"]:
                st.markdown(f"💡 **{imp}**")

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    with st.expander("📄 View Parsed Resume Text & Extracted Raw Competencies"):
        c1, c2 = st.columns(2)
        with c1:
            st.write(f"**Skills Extracted ({len(skills)}):**")
            for sk in skills:
                st.write(f"- {sk}")
        with c2:
            st.write(f"**Projects Found ({len(projects)}):**")
            for pr in projects:
                st.write(f"- {pr}")


# =====================================================================
# RENDER HELPER: EXACTLY TWO RECOMMENDED JOB ROLES
# =====================================================================
def render_job_roles_section(job_roles_detailed, branch):
    st.subheader(f"💼 Recommended Job Roles ({branch}) — Exactly 2 Matched Profiles")
    st.caption("Matched against our authoritative master dataset based on actual resume evidence.")

    if not job_roles_detailed:
        st.info("Upload your resume in **Resume Analysis** to generate job role recommendations.")
        return

    c1, c2 = st.columns(2)
    for idx, role_info in enumerate(job_roles_detailed[:2]):
        col_target = c1 if idx == 0 else c2
        with col_target:
            st.markdown(
                f"""
                <div style="background: white; border: 1px solid #e2e8f0; border-radius: 16px; padding: 18px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                        <span style="font-weight: 800; font-size: 1.05rem; color: #1e293b;">🎯 Role {idx+1}: {role_info['role']}</span>
                        <span style="background: #4f46e5; color: white; padding: 2px 10px; border-radius: 12px; font-weight: 800; font-size: 0.8rem;">
                            {role_info['match_percentage']}% Match
                        </span>
                    </div>
                    <p style="font-size: 0.82rem; color: #64748b; margin-bottom: 10px;">{role_info['explanation']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write(f"**Matching Skills:** " + (", ".join(role_info["matching_skills"]) if role_info["matching_skills"] else "General Branch Skills"))
            st.write(f"**Missing Skills:** " + (", ".join(role_info["missing_skills"]) if role_info["missing_skills"] else "None (Full Match!)"))
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)


# =====================================================================
# RENDER HELPER: INTERVIEW DIAGNOSTICS & RETAKE
# =====================================================================
def render_interview_diagnostics(interview_score, has_interview, branch):
    st.subheader("🎤 5-Round Interview Scorecard & Performance Analysis")

    if not has_interview or interview_score is None:
        st.markdown(
            f"""
            <div style="background: white; border: 1.5px dashed #cbd5e1; border-radius: 16px; padding: 24px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
                <div style="font-size: 2.2rem; margin-bottom: 8px;">🎯</div>
                <div style="font-weight: 700; color: #1e293b; font-size: 1.05rem; margin-bottom: 6px;">5-Round Interview Not Completed</div>
                <div style="font-size: 0.84rem; color: #64748b; margin-bottom: 16px;">
                    Take the 5-round recruitment drive (Aptitude, Coding, Technical, Project, & HR) tailored for <strong>{branch}</strong>.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("🎤 Start 5-Round Interview", type="primary", key="btn_go_interview_dash"):
            st.session_state.nav_module = "Interview"
            st.rerun()
        return

    st.markdown(
        f"""
        <div style="background: white; border: 1px solid #e2e8f0; border-radius: 16px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); margin-bottom: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-weight: 700; color: #1e293b; font-size: 0.95rem;">Overall Recruitment Score</span>
                <span style="font-size: 1.35rem; font-weight: 800; color: #4f46e5;">{interview_score:.1f}%</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    round_scores = st.session_state.get("round_scores", {})
    if round_scores:
        with st.expander("📊 Round-wise Performance Breakdown", expanded=True):
            r_names = get_branch_round_names(branch)
            for r_k, sc in round_scores.items():
                if sc is not None:
                    st.write(f"**{r_k} ({r_names.get(r_k, '')}):** {sc:.1f}%")
                    st.progress(sc / 100)

    # Realistic Strong & Weak Performance Analysis
    if st.session_state.get("round_summaries"):
        strong_areas, improvement_areas = generate_performance_analysis(st.session_state.round_summaries, branch)
        st.markdown("**🌟 Strong Performance Areas:**")
        for sa in strong_areas:
            st.markdown(f"- {sa}")
        st.markdown("**⚠️ Areas Requiring Improvement:**")
        for ia in improvement_areas:
            st.markdown(f"- {ia}")

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # RETAKE INTERVIEW BUTTON
    if st.button("🔄 Retake Interview (Fresh Question Set)", type="primary", key="btn_retake_interview_dash"):
        reset_interview_state(retake=True)
        st.session_state.nav_module = "Interview"
        st.rerun()


# =====================================================================
# RENDER HELPER: SKILL DOMAINS & PROJECTS
# =====================================================================
def render_skills_and_projects(skills, projects, has_resume, branch):
    st.subheader(f"💻 Extracted Competencies ({branch})")

    if not has_resume:
        st.info("ℹ️ No resume uploaded yet. Go to **Resume Analysis** to upload your resume for automatic branch detection and scoring.")
        if st.button("📄 Go to Resume Analysis", key="btn_go_resume_dash"):
            st.session_state.nav_module = "Resume Analysis"
            st.rerun()
        return

    if not skills:
        st.warning(f"⚠️ No technical skills were detected specifically for {branch} Engineering.")
        return

    branch_domains = SKILL_DOMAINS.get(branch, SKILL_DOMAINS["CSE"])
    categorized = {}
    for domain, domain_skills in branch_domains.items():
        matched = [s for s in skills if s in domain_skills]
        if matched:
            categorized[domain] = matched

    assigned = {s for dom in branch_domains.values() for s in dom}
    other_skills = [s for s in skills if s not in assigned]
    if other_skills:
        categorized["Other Technical Skills"] = other_skills

    for domain, matched_skills in categorized.items():
        badges = "".join([f'<span class="skill-pill">{s}</span>' for s in matched_skills])
        st.markdown(
            f"""
            <div class="domain-card">
                <div class="domain-card-title">📁 {domain} ({len(matched_skills)})</div>
                <div>{badges}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if projects:
        with st.expander(f"📁 Extracted Resume Projects ({len(projects)})"):
            for p in projects:
                st.markdown(f"- **{p}**")


# =====================================================================
# MAIN DASHBOARD ENTRYPOINT
# =====================================================================
def dashboard_page():
    username = st.session_state.get("user", "Candidate")
    branch = st.session_state.get("selected_branch", "CSE")
    resume_text = st.session_state.get("resume_text", None)
    resume_pdf = st.session_state.get("resume_pdf", None)

    skills = []
    job_roles_detailed = []
    resume_score = None
    projects = []
    score_details = st.session_state.get("resume_score_details", None)

    if resume_text:
        skills = extract_skills(resume_text, branch=branch)
        job_roles_detailed = get_job_roles_detailed(skills, branch=branch, resume_text=resume_text)
        
        if resume_pdf:
            try:
                projects = extract_projects_from_pdf(resume_pdf)
            except Exception:
                projects = []

        if not score_details:
            try:
                score_details = calculate_resume_score_detailed(
                    resume_text=resume_text,
                    pdf_bytes=resume_pdf,
                    branch=branch,
                    skills=skills,
                    projects=projects
                )
                st.session_state.resume_score_details = score_details
            except Exception:
                score_details = None

        if score_details:
            resume_score = score_details["overall_score"]

    interview_score = st.session_state.get("interview_score", None)

    has_resume = bool(resume_text)
    has_interview = interview_score is not None
    readiness_score = compute_readiness_score(resume_score, interview_score)
    badge_label, badge_color, badge_desc = get_readiness_status(readiness_score, has_resume, has_interview)
    top_role = job_roles_detailed[0]["role"] if job_roles_detailed else ("Pending" if not has_resume else f"{branch} Graduate")

    render_top_project_header()

    if has_interview:
        check_and_render_celebration(interview_score, readiness_score)

    render_candidate_hero(username, branch, badge_label, badge_color, badge_desc)
    render_readiness_meter(readiness_score)

    render_kpi_cards(resume_score, len(skills), top_role, interview_score, readiness_score)
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # RENDER ALL RESUME RESULTS ON DASHBOARD
    render_comprehensive_resume_results(score_details, resume_text, skills, projects)
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    render_job_roles_section(job_roles_detailed, branch)
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    left_col, right_col = st.columns([1.1, 0.9])
    with left_col:
        render_skills_and_projects(skills, projects, has_resume, branch)
    with right_col:
        render_interview_diagnostics(interview_score, has_interview, branch)

    st.divider()
