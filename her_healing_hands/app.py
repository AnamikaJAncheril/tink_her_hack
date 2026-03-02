import streamlit as st
import database as db
import auth
from utils import apply_custom_css, show_logo, init_session_state, logout

# Mother pages
from mother.dashboard import show_mother_dashboard
from mother.happy_page import show_happy_page
from mother.thoughts_page import show_thoughts_page
from mother.assessment_page import show_assessment_page

# Partner pages
from partner.dashboard import show_partner_dashboard
from partner.care_guide import show_care_guide
from partner.nutrition import show_nutrition_page
from partner.symptoms import show_symptoms_page
from partner.results_page import show_results_page

# Page configuration
st.set_page_config(
    page_title="Her Healing Hands",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
db.init_db()

# Initialize session state
init_session_state()

# Apply custom styling
apply_custom_css()

def show_login_page():
    """Display login page."""
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        show_logo()
        st.title("Welcome to Her Healing Hands 🌸")
        st.write("Supporting mothers and partners through the postpartum journey")
        
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        with tab1:
            st.subheader("Login")
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")
            
            if st.button("Login", type="primary", use_container_width=True):
                success, user, message = auth.login_user(email, password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.session_state.page = 'dashboard'
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)
        
        with tab2:
            st.subheader("Register")
            name = st.text_input("Full Name", key="reg_name")
            email = st.text_input("Email", key="reg_email")
            password = st.text_input("Password", type="password", key="reg_password", help="Minimum 6 characters")
            role = st.selectbox("I am a:", ["Mother", "Partner"], key="reg_role")
            
            invite_code = None
            if role == "Mother":
                st.info("💡 After registration, you'll receive an invite code to share with your partner.")
            else:
                invite_code = st.text_input("Mother's Invite Code", placeholder="HH-XXXXXX", key="reg_invite")
                st.caption("Enter the invite code provided by your partner")
            
            if st.button("Register", type="primary", use_container_width=True):
                success, message = auth.register_user(name, email, password, role, invite_code)
                if success:
                    st.success(message)
                    st.info("Please login with your credentials.")
                else:
                    st.error(message)

def show_mother_portal(user):
    """Display mother's portal with sidebar navigation."""
    with st.sidebar:
        show_logo()
        st.title(f"Hello, {user['name']} 💐")
        st.markdown("---")
        
        # Navigation
        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state.page = 'dashboard'
            st.rerun()
        
        if st.button("💛 What Makes You Happy", use_container_width=True):
            st.session_state.page = 'happy'
            st.rerun()
        
        if st.button("📝 Share Your Thoughts", use_container_width=True):
            st.session_state.page = 'thoughts'
            st.rerun()
        
        if st.button("📊 Weekly Assessment", use_container_width=True):
            st.session_state.page = 'assessment'
            st.rerun()
        
        st.markdown("---")
        
        if st.button("🚪 Logout", use_container_width=True):
            logout()
    
    # Main content
    if st.session_state.page == 'dashboard':
        show_mother_dashboard(user)
    elif st.session_state.page == 'happy':
        show_happy_page(user)
    elif st.session_state.page == 'thoughts':
        show_thoughts_page(user)
    elif st.session_state.page == 'assessment':
        show_assessment_page(user)

def show_partner_portal(user):
    """Display partner's portal with sidebar navigation."""
    with st.sidebar:
        show_logo()
        st.title(f"Hello, {user['name']} 🤝")
        st.markdown("---")
        
        # Navigation
        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state.page = 'dashboard'
            st.rerun()
        
        if st.button("🤝 How to Support", use_container_width=True):
            st.session_state.page = 'support'
            st.rerun()
        
        if st.button("🍲 Nutrition", use_container_width=True):
            st.session_state.page = 'nutrition'
            st.rerun()
        
        if st.button("⚠️ Postpartum Symptoms", use_container_width=True):
            st.session_state.page = 'symptoms'
            st.rerun()
        
        if st.button("📈 Assessment Results", use_container_width=True):
            st.session_state.page = 'results'
            st.rerun()
        
        st.markdown("---")
        
        if st.button("🚪 Logout", use_container_width=True):
            logout()
    
    # Main content
    if st.session_state.page == 'dashboard':
        show_partner_dashboard(user)
    elif st.session_state.page == 'support':
        show_care_guide()
    elif st.session_state.page == 'nutrition':
        show_nutrition_page()
    elif st.session_state.page == 'symptoms':
        show_symptoms_page()
    elif st.session_state.page == 'results':
        show_results_page(user)

# Main application logic
def main():
    if not st.session_state.logged_in:
        show_login_page()
    else:
        user = st.session_state.user
        if user['role'] == 'Mother':
            show_mother_portal(user)
        else:
            show_partner_portal(user)

if __name__ == "__main__":
    main()
