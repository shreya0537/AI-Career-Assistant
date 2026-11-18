import streamlit as st
import pymupdf

from backend.ai.skills import (
    extract_skills,
    get_job_roles_detailed,
    extract_projects_from_pdf
)

from backend.ai.scoring import (
    calculate_resume_score_detailed
)

from backend.ai.branch_detection import (
    detect_branch_from_resume
)

from backend.constants import (
    ENGINEERING_BRANCHES,
    BRANCH_FULL_NAMES
)


# =========================================
# RESUME PAGE WITH AUTOMATIC BRANCH DETECTION
# =========================================

def resume_page():

    st.header("Resume Analysis & Branch Profiling 📄")
    st.caption("Upload your PDF resume to detect your Engineering Branch, view your Resume Score, and see Recommended Job Roles. (Full breakdown & analysis are available on the Dashboard).")

    # Initialize Session States
    if "selected_branch" not in st.session_state or st.session_state.selected_branch not in ENGINEERING_BRANCHES:
        st.session_state.selected_branch = "CSE"

    if "branch_auto_detected" not in st.session_state:
        st.session_state.branch_auto_detected = False

    # =====================================
    # 1. UPLOAD RESUME PDF FIRST
    # =====================================
    st.markdown("### 📄 Step 1: Upload Your Resume")

    uploaded_file = st.file_uploader(
        "Upload your PDF resume",
        type=["pdf"],
        key="resume_uploader"
    )

    if uploaded_file is None:
        st.info("Please upload your PDF resume to begin branch detection, scoring, and job role matching.")

        # Show manual branch selector fallback when no resume is uploaded yet
        st.markdown("#### 🎓 Or Select Branch Manually:")
        current_branch_idx = ENGINEERING_BRANCHES.index(st.session_state.selected_branch)
        selected_branch_label = st.selectbox(
            "CHOOSE ENGINEERING BRANCH",
            options=[BRANCH_FULL_NAMES[b] for b in ENGINEERING_BRANCHES],
            index=current_branch_idx,
            key="branch_selector_dropdown_fallback"
        )
        for code, full_name in BRANCH_FULL_NAMES.items():
            if full_name == selected_branch_label:
                st.session_state.selected_branch = code
                break

        return

    # Read PDF Text
    pdf_bytes = uploaded_file.getvalue()
    st.session_state.resume_pdf = pdf_bytes

    try:
        document = pymupdf.open(stream=pdf_bytes, filetype="pdf")
        resume_text = ""
        for page in document:
            page_text = page.get_text("text")
            if page_text:
                resume_text += page_text + "\n"
        document.close()
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return

    st.session_state.resume_text = resume_text
    st.session_state.resume_uploaded = True

    # =====================================
    # 2. AUTOMATIC BRANCH DETECTION
    # =====================================
    detected_branch, confidence, explanation, is_confident = detect_branch_from_resume(resume_text)

    if is_confident:
        st.session_state.selected_branch = detected_branch
        st.session_state.branch_auto_detected = True
        st.success(f"🤖 **Automatic Branch Detected:** **{BRANCH_FULL_NAMES[detected_branch]}** ({int(confidence*100)}% Confidence) ✅")
        st.caption(f"ℹ️ {explanation}")
    else:
        st.warning("⚠️ Could not automatically determine engineering branch with high confidence. Please confirm your branch below:")
        current_branch_idx = ENGINEERING_BRANCHES.index(st.session_state.selected_branch)
        selected_branch_label = st.selectbox(
            "CONFIRM YOUR ENGINEERING BRANCH",
            options=[BRANCH_FULL_NAMES[b] for b in ENGINEERING_BRANCHES],
            index=current_branch_idx,
            key="branch_selector_dropdown_confirm"
        )
        for code, full_name in BRANCH_FULL_NAMES.items():
            if full_name == selected_branch_label:
                st.session_state.selected_branch = code
                break

    selected_branch = st.session_state.selected_branch

    # Allow user to change branch manually if needed
    with st.expander("🔄 Change Branch Manually (If Incorrect)"):
        manual_branch_label = st.selectbox(
            "OVERRIDE DETECTED BRANCH",
            options=[BRANCH_FULL_NAMES[b] for b in ENGINEERING_BRANCHES],
            index=ENGINEERING_BRANCHES.index(selected_branch),
            key="branch_override_dropdown"
        )
        for code, full_name in BRANCH_FULL_NAMES.items():
            if full_name == manual_branch_label:
                st.session_state.selected_branch = code
                selected_branch = code
                break

    st.divider()

    # Extract skills & projects
    skills = extract_skills(resume_text, branch=selected_branch)
    projects = extract_projects_from_pdf(pdf_bytes)

    st.session_state.resume_skills = skills
    st.session_state.resume_projects = projects

    # =====================================
    # 3. SCORE RESULT ONLY
    # =====================================
    score_details = calculate_resume_score_detailed(
        resume_text=resume_text,
        pdf_bytes=pdf_bytes,
        branch=selected_branch,
        skills=skills,
        projects=projects
    )

    st.session_state.resume_score_details = score_details
    st.session_state.resume_score = score_details["overall_score"]

    st.markdown("### 📊 Resume Score Result")
    st.markdown(
        f"""
        <div style="background: white; border: 2px solid #6366f1; border-radius: 18px; padding: 22px; text-align: center; box-shadow: 0 4px 14px rgba(0,0,0,0.05); max-width: 450px; margin: 0 auto 20px auto;">
            <div style="font-size: 0.85rem; font-weight: 700; color: #64748b; text-transform: uppercase;">100% Weighted Resume Score</div>
            <div style="font-size: 3.5rem; font-weight: 900; color: #4f46e5; margin: 8px 0;">{score_details['overall_score']}%</div>
            <div style="font-size: 0.9rem; font-weight: 700; color: {'#16a34a' if score_details['overall_score']>=70 else '#d97706'};">
                {'🏆 Outstanding Resume Profile' if score_details['overall_score']>=70 else '⏳ Enhancement Recommended'}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # =====================================
    # 4. RECOMMENDED JOB ROLES RESULT
    # =====================================
    st.subheader(f"💼 Recommended Job Roles for {selected_branch}")
    st.caption("Matched directly from our master dataset based on your extracted resume competencies.")

    job_roles_detailed = get_job_roles_detailed(skills, branch=selected_branch, resume_text=resume_text)
    st.session_state.recommended_job_roles_detailed = job_roles_detailed
    st.session_state.recommended_job_roles = [r["role"] for r in job_roles_detailed]

    role_col1, role_col2 = st.columns(2)

    for idx, role_info in enumerate(job_roles_detailed[:2]):
        col_target = role_col1 if idx == 0 else role_col2
        with col_target:
            st.markdown(
                f"""
                <div style="background: white; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <span style="font-weight: 800; font-size: 1.15rem; color: #0f172a;">🎯 Role {idx+1}: {role_info['role']}</span>
                        <span style="background: #e0e7ff; color: #4338ca; font-size: 0.9rem; font-weight: 800; padding: 4px 12px; border-radius: 20px;">
                            {role_info['match_percentage']}% Match
                        </span>
                    </div>
                    <p style="font-size: 0.85rem; color: #475569; margin-bottom: 12px;">{role_info['explanation']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write(f"**✅ Matching Skills:** " + (", ".join(role_info["matching_skills"]) if role_info["matching_skills"] else "General Branch Fundamentals"))
            st.write(f"**📌 Missing Skills:** " + (", ".join(role_info["missing_skills"]) if role_info["missing_skills"] else "None (Full Match!)"))
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    st.divider()

    # Callout for Dashboard Full Results
    st.info("💡 **All detailed resume results (Section-wise Breakdown, Strengths, Missing Info, Improvement Suggestions, & Extracted Competencies) are displayed on your Dashboard.**")
    
    col_dash, col_interview = st.columns(2)
    with col_dash:
        if st.button("📊 View All Resume Results on Dashboard", type="primary", key="btn_go_dashboard"):
            st.session_state.nav_module = "Dashboard"
            st.rerun()

    with col_interview:
        if st.button(f"🎤 Start 5-Round {selected_branch} Mock Interview", type="secondary", key="btn_resume_to_interview"):
            st.session_state.nav_module = "Interview"
            st.rerun()