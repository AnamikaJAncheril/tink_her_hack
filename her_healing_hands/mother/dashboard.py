import streamlit as st
import database as db
from utils import format_datetime

def show_mother_dashboard(user):
    """Display mother's main dashboard."""
    st.title(f"Welcome, {user['name']} 💐")
    
    # Display invite code prominently
    st.info(f"**Your Invite Code:** `{user['link_code']}`")
    st.caption("Share this code with your partner so they can create an account and access your assessment results (with your consent).")
    
    st.markdown("---")
    
    # Dashboard overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        happy_entries = db.get_happy_entries(user['id'])
        st.metric("Happy Entries", len(happy_entries))
    
    with col2:
        assessments = db.get_all_assessments(user['id'])
        st.metric("Assessments", len(assessments))
    
    with col3:
        if user['linked_user_id']:
            partner = db.get_user_by_id(user['linked_user_id'])
            st.metric("Partner Linked", "✓")
            st.caption(f"Connected to {partner['name']}")
        else:
            st.metric("Partner Linked", "✗")
    
    st.markdown("---")
    
    # Recent activity
    st.subheader("Recent Activity")
    
    # Latest assessment
    if assessments:
        latest = assessments[0]
        with st.expander("📊 Latest Assessment", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Score:** {latest['score']}/30")
                st.write(f"**Risk Level:** {latest['risk_level']}")
            with col2:
                st.write(f"**Date:** {format_datetime(latest['created_at'])}")
                st.write(f"**Shared:** {'Yes' if latest['consent_given'] else 'No'}")
            if latest['summary']:
                st.write("**Summary:**")
                st.write(latest['summary'])
    
    # Recent happy entries
    if happy_entries:
        with st.expander("💛 Recent Happy Moments", expanded=True):
            for entry in happy_entries[:3]:
                st.write(f"**{format_datetime(entry['created_at'])}**")
                st.write(entry['content'])
                st.markdown("---")
    
    # Quick actions
    st.markdown("---")
    st.subheader("Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💛 Add Happy Moment", use_container_width=True):
            st.session_state.page = 'happy'
            st.rerun()
    
    with col2:
        if st.button("📝 Chat Support", use_container_width=True):
            st.session_state.page = 'thoughts'
            st.rerun()
    
    with col3:
        if st.button("📊 Take Assessment", use_container_width=True):
            st.session_state.page = 'assessment'
            st.rerun()
