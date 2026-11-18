import streamlit as st

from backend.database import (
    register_user,
    login_user
)


def login():
    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #1e293b; font-size: 1.8rem; font-weight: 800;">
                Welcome Back! 👋
            </h2>
            <p style="color: #64748b; margin-top: 6px; font-size: 0.95rem;">
                Sign in to analyze your resume and launch your tailored mock interview.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.container():
        username = st.text_input(
            "👤 Username",
            placeholder="Enter your username",
            key="login_username"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter your password",
            key="login_password"
        )

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        if st.button("🚀 Sign In to Assistant", use_container_width=True):
            if not username or not password:
                st.warning("⚠️ Please enter both your username and password.")
                return

            user = login_user(username, password)

            if user:
                st.session_state.logged_in = True
                st.session_state.user = username
                st.session_state.resume_text = None
                st.session_state.resume_pdf = None
                st.session_state.nav_module = "Resume Analysis"
                st.session_state.interview_score = None
                st.session_state.interview_answered = 0
                st.session_state.interview_total = 0
                st.session_state.interview_breakdown = []
                st.session_state.just_completed_interview = False
                st.session_state.question_number = 0
                st.session_state.question_scores = []
                st.success("✅ Login successful! Redirecting to Resume Analysis...")
                st.rerun()
            else:
                st.error("❌ Invalid username or password. Please try again.")


def register():
    st.markdown(
        """
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #1e293b; font-size: 1.8rem; font-weight: 800;">
                Create Your Account 📝
            </h2>
            <p style="color: #64748b; margin-top: 6px; font-size: 0.95rem;">
                Join the AI-Driven Career Assistant to boost your interview readiness.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.container():
        username = st.text_input(
            "👤 Choose Username",
            placeholder="e.g. alex_developer",
            key="register_username"
        )

        password = st.text_input(
            "🔒 Choose Password",
            type="password",
            placeholder="Enter a secure password",
            key="register_password"
        )

        confirm_password = st.text_input(
            "🔒 Confirm Password",
            type="password",
            placeholder="Re-enter your password",
            key="confirm_password"
        )

        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

        if st.button("✨ Create Free Account", use_container_width=True):
            if not username or not password:
                st.warning("⚠️ Please fill in all the required fields.")
                return

            if password != confirm_password:
                st.error("❌ Passwords do not match.")
                return

            success = register_user(username, password)

            if success:
                st.success("🎉 Account created successfully! Please select 'Login' from the sidebar.")
            else:
                st.error("❌ Username already exists. Please choose a different username.")