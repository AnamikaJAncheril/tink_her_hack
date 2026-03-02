import streamlit as st
from datetime import datetime

def calculate_risk_level(score: int) -> str:
    """Calculate risk level based on assessment score."""
    if score <= 7:
        return "Normal"
    elif score <= 14:
        return "Mild"
    elif score <= 22:
        return "Moderate"
    else:
        return "High"

def get_risk_color(risk_level: str) -> str:
    """Get color for risk level."""
    colors = {
        "Normal": "#90EE90",
        "Mild": "#FFD700",
        "Moderate": "#FFA500",
        "High": "#FF6347"
    }
    return colors.get(risk_level, "#CCCCCC")

def format_datetime(dt_string: str) -> str:
    """Format datetime string for display."""
    try:
        dt = datetime.fromisoformat(dt_string)
        return dt.strftime("%B %d, %Y at %I:%M %p")
    except:
        return dt_string

def apply_custom_css():
    """Apply custom CSS styling."""
    st.markdown("""
        <style>
        .main {
            background-color: #FFF5F7;
        }
        .stButton>button {
            background-color: #E6B8D7;
            color: #4A4A4A;
            border-radius: 10px;
            border: none;
            padding: 0.5rem 2rem;
            font-weight: 500;
        }
        .stButton>button:hover {
            background-color: #D8A5C8;
        }
        .css-1d391kg {
            background-color: #F3E5F5;
        }
        h1, h2, h3 {
            color: #6B4C7A;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
        }
        .stTextArea>div>div>textarea {
            border-radius: 10px;
        }
        div[data-testid="stMetricValue"] {
            font-size: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

def show_logo():
    """Display logo if available."""
    try:
        st.image("assets/logo.png", width=200)
    except:
        st.markdown("### 🌸 Her Healing Hands")

def init_session_state():
    """Initialize session state variables."""
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'page' not in st.session_state:
        st.session_state.page = 'login'

def logout():
    """Logout user and clear session."""
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.chat_history = []
    st.session_state.page = 'login'
    st.rerun()
