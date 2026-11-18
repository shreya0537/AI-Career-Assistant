import streamlit as st
import os
import sys
import shutil

# Add the project root so imports such as `from backend...` work on Streamlit Cloud.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from backend.database import (
    create_tables
)

from backend.auth import (
    login,
    register
)

from backend.resume import (
    resume_page
)

from backend.interview import (
    interview_page
)

from backend.dashboard import (
    dashboard_page
)


# =========================================
# INITIALIZE DATABASE & ASSETS
# =========================================

create_tables()

# Asset Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
HERO_IMG_PATH = os.path.join(ASSETS_DIR, "hero_career_ai.jpg")



# =========================================
# PAGE SETTINGS
# =========================================

st.set_page_config(
    page_title="AI Career Assistant - Resume Analysis & Interview Evaluation",
    page_icon="🤖",
    layout="wide"
)


# =========================================
# LOAD CSS
# =========================================

def load_css():
    css_path = os.path.join(
        os.path.dirname(__file__),
        "style.css"
    )

    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as file:
            st.markdown(
                f"<style>{file.read()}</style>",
                unsafe_allow_html=True
            )


# =========================================
# SIDEBAR COMPONENTS
# =========================================

def render_sidebar_header():
    st.markdown(
        """
        <div class="sidebar-brand-card">
            <div class="sidebar-badge">⚡ AI Platform</div>
            <div class="sidebar-title">🤖 Career Assistant</div>
            <div class="sidebar-subtitle">
                AI-Driven Career Assistant with Resume Analysis and Interview Evaluation
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_sidebar_features():
    st.markdown(
        """
        <div style="margin-top: 15px; margin-bottom: 10px;">
            <div style="font-size: 0.78rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8px;">
                Platform Capabilities
            </div>
            <div class="sidebar-feature-pill">
                <span>📄</span> <span>PDF Resume Parser</span>
            </div>
            <div class="sidebar-feature-pill">
                <span>🎯</span> <span>Career Role Matcher</span>
            </div>
            <div class="sidebar-feature-pill">
                <span>🎤</span> <span>5-Stage Mock Interview</span>
            </div>
            <div class="sidebar-feature-pill">
                <span>📊</span> <span>NLP Answer Scoring</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================
# DASHBOARD (LOGGED IN)
# =========================================

def dashboard():
    # Sidebar
    with st.sidebar:
        render_sidebar_header()

        st.markdown(
            f"""
            <div style="background: rgba(255,255,255,0.08); border-radius: 12px; padding: 12px; margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.12);">
                <div style="font-size: 0.75rem; color: #cbd5e1;">Logged in as:</div>
                <div style="font-size: 1rem; font-weight: 700; color: #ffffff;">👤 {st.session_state.user}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("### 🧭 Navigation")

        modules = ["Resume Analysis", "Interview", "Dashboard"]
        if "nav_module" not in st.session_state or st.session_state.nav_module not in modules:
            st.session_state.nav_module = "Resume Analysis"

        current_idx = modules.index(st.session_state.nav_module)
        selected_module = st.selectbox(
            "CHOOSE MODULE",
            modules,
            index=current_idx
        )

        if selected_module != st.session_state.nav_module:
            st.session_state.nav_module = selected_module
            st.rerun()

        render_sidebar_features()

        st.divider()

        if st.button("🚪 Sign Out"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.selected_branch = "CSE"
            st.session_state.resume_text = None
            st.session_state.resume_pdf = None
            st.session_state.resume_skills = None
            st.session_state.interview_score = None
            st.session_state.unlocked_round = 1
            st.session_state.round_scores = {"Round 1": None, "Round 2": None, "Round 3": None, "Round 4": None, "Round 5": None}
            st.session_state.round_details = {"Round 1": [], "Round 2": [], "Round 3": [], "Round 4": [], "Round 5": []}
            st.session_state.just_completed_interview = False
            st.session_state.nav_module = "Resume Analysis"
            st.rerun()

        st.markdown(
            """
            <div style="margin-top: 25px; font-size: 0.76rem; color: #94a3b8; text-align: center;">
                © 2026 AI Career Assistant
            </div>
            """,
            unsafe_allow_html=True
        )


    # Main content
    if st.session_state.nav_module == "Resume Analysis":
        resume_page()
    elif st.session_state.nav_module == "Interview":
        interview_page()
    elif st.session_state.nav_module == "Dashboard":
        dashboard_page()


# =========================================
# LANDING & AUTH PAGE (LOGGED OUT)
# =========================================

def landing_page():
    # Sidebar for unauthenticated users
    with st.sidebar:
        render_sidebar_header()

        st.write("### 🔐 Get Started")

        option = st.selectbox(
            "AUTHENTICATION",
            [
                "Login",
                "Register"
            ]
        )

        render_sidebar_features()

        st.markdown(
            """
            <div style="margin-top: 25px; font-size: 0.76rem; color: #94a3b8; text-align: center;">
                © 2026 AI Career Assistant
            </div>
            """,
            unsafe_allow_html=True
        )



    # =========================================
    # MAIN CONTENT (CENTERED LAYOUT)
    # =========================================

    # Hero Banner (Centered)
    st.markdown(
        """
        <div class="hero-container" style="text-align: center;">
            <div class="hero-tag">✨ Next-Gen Placement Prep</div>
            <div class="hero-title">AI-Driven Career Assistant</div>
            <div class="hero-desc" style="margin: 0 auto;">
                AI-Driven Career Assistant with Resume Analysis and Interview Evaluation 
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Centered Authentication Card
    _, col_center, _ = st.columns([1, 2, 1])

    with col_center:
        st.markdown('<div class="auth-box">', unsafe_allow_html=True)
        if option == "Login":
            login()
        else:
            register()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)

    # Show Project Illustration if available (Centered)
    if os.path.exists(HERO_IMG_PATH):
        _, img_col, _ = st.columns([1, 4, 1])
        with img_col:
            st.image(
                HERO_IMG_PATH,
                caption="AI Career Assistant — Resume Intelligence & Real-time Evaluation",
                use_container_width=True
            )


    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # Project Highlight Cards (4 Columns)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📄</div>
                <div class="feature-title">Resume Parser</div>
                <div class="feature-desc">
                    Extracts skills and projects from PDF resumes using structural font heuristics.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <div class="feature-title">Role Matcher</div>
                <div class="feature-desc">
                    Maps detected competencies directly to in-demand industry job profiles.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">🎤</div>
                <div class="feature-title">5-Stage Interview</div>
                <div class="feature-desc">
                    Comprehensive 5-round simulation covering Aptitude, Coding, Technical Core, Project, & HR.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c4:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <div class="feature-title">NLP Scoring</div>
                <div class="feature-desc">
                    Automated TF-IDF vector similarity scoring with immediate actionable feedback.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )



# =========================================
# MAIN APP CONTROLLER
# =========================================

def main():
    load_css()

    # Session variables
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user" not in st.session_state:
        st.session_state.user = None

    if "resume_text" not in st.session_state:
        st.session_state.resume_text = None

    if "resume_pdf" not in st.session_state:
        st.session_state.resume_pdf = None

    if "question_number" not in st.session_state:
        st.session_state.question_number = 0

    if "question_scores" not in st.session_state:
        st.session_state.question_scores = []

    # Route according to auth state
    if st.session_state.logged_in:
        dashboard()
    else:
        landing_page()


# =========================================
# START ENTRYPOINT
# =========================================

if __name__ == "__main__":
    main()