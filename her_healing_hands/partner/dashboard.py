import streamlit as st
import database as db

def show_partner_dashboard(user):
    """Display partner's main dashboard."""
    st.title(f"Welcome, {user['name']} 🤝")
    
    # Check if linked to a mother
    if not user['linked_user_id']:
        st.warning("⚠️ You are not linked to a mother's account yet.")
        st.info("Please contact your partner to get their invite code and register again with the correct code.")
        return
    
    # Get mother's information
    mother = db.get_user_by_id(user['linked_user_id'])
    
    st.success(f"✓ Connected to {mother['name']}")
    
    st.markdown("---")
    
    # Dashboard overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Partner Status", "Active")
    
    with col2:
        assessments = db.get_all_assessments(mother['id'])
        shared_assessments = [a for a in assessments if a['consent_given']]
        st.metric("Shared Assessments", len(shared_assessments))
    
    with col3:
        latest = db.get_latest_assessment(mother['id'])
        if latest and latest['consent_given']:
            st.metric("Latest Risk Level", latest['risk_level'])
        else:
            st.metric("Latest Risk Level", "N/A")
    
    st.markdown("---")
    
    # Quick info
    st.subheader("Supporting Your Partner")
    
    st.write("""
    Your role as a partner is crucial during the postpartum period. Here's how you can help:
    
    - **Be Present:** Listen without judgment and validate her feelings
    - **Be Practical:** Help with household tasks and baby care
    - **Be Patient:** Recovery takes time, both physically and emotionally
    - **Be Informed:** Learn about postpartum challenges and symptoms
    - **Be Supportive:** Encourage professional help if needed
    """)
    
    # Latest assessment preview
    if latest and latest['consent_given']:
        st.markdown("---")
        st.subheader("Latest Assessment Preview")
        with st.expander("View Details", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Score:** {latest['score']}/30")
                st.write(f"**Risk Level:** {latest['risk_level']}")
            with col2:
                st.write(f"**Date:** {latest['created_at'][:10]}")
            
            st.info("💡 Visit the 'Assessment Results' page for detailed guidance on how to support your partner.")
    
    # Quick actions
    st.markdown("---")
    st.subheader("Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🤝 Support Guide", use_container_width=True):
            st.session_state.page = 'support'
            st.rerun()
    
    with col2:
        if st.button("⚠️ Learn Symptoms", use_container_width=True):
            st.session_state.page = 'symptoms'
            st.rerun()
    
    with col3:
        if st.button("📈 View Results", use_container_width=True):
            st.session_state.page = 'results'
            st.rerun()
