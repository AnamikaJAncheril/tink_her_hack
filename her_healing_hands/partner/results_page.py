import streamlit as st
import database as db
from utils import format_datetime, get_risk_color
from ai.partner_ai import get_partner_guidance

def show_results_page(user):
    """Display assessment results for partner."""
    st.title("Assessment Results 📈")
    
    # Check if linked
    if not user['linked_user_id']:
        st.warning("⚠️ You are not linked to a mother's account.")
        st.info("Please contact your partner to get their invite code.")
        return
    
    # Get mother's information
    mother = db.get_user_by_id(user['linked_user_id'])
    
    st.write(f"Viewing assessment results for: **{mother['name']}**")
    
    st.markdown("---")
    
    # Get assessments
    assessments = db.get_all_assessments(mother['id'])
    shared_assessments = [a for a in assessments if a['consent_given']]
    
    if not shared_assessments:
        st.info("📭 No assessment results have been shared with you yet.")
        st.write("""
        Your partner needs to:
        1. Complete a weekly assessment
        2. Check the box to share results with you
        
        Once shared, you'll be able to see the results and receive guidance on how to support her.
        """)
        return
    
    # Display latest assessment
    latest = shared_assessments[0]
    
    st.subheader("Latest Assessment")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Score", f"{latest['score']}/30")
    
    with col2:
        st.markdown(f"**Risk Level**")
        st.markdown(f"<div style='background-color: {get_risk_color(latest['risk_level'])}; padding: 10px; border-radius: 5px; text-align: center; font-weight: bold;'>{latest['risk_level']}</div>", unsafe_allow_html=True)
    
    with col3:
        st.metric("Date", format_datetime(latest['created_at'])[:12])
    
    st.markdown("---")
    
    # Mother's summary
    if latest['summary']:
        st.subheader("Emotional Summary")
        st.info(latest['summary'])
    
    st.markdown("---")
    
    # Generate partner guidance
    st.subheader("Guidance for You")
    
    if 'partner_guidance' not in st.session_state:
        st.session_state.partner_guidance = {}
    
    guidance_key = f"guidance_{latest['id']}"
    
    if guidance_key not in st.session_state.partner_guidance:
        with st.spinner("Generating personalized guidance..."):
            guidance = get_partner_guidance(
                latest['summary'] or "Assessment completed",
                latest['score'],
                latest['risk_level']
            )
            st.session_state.partner_guidance[guidance_key] = guidance
    
    st.write(st.session_state.partner_guidance[guidance_key])
    
    # Action items based on risk level
    st.markdown("---")
    st.subheader("Recommended Actions")
    
    if latest['risk_level'] == "Normal":
        st.success("""
        ✅ Continue providing emotional and practical support
        - Maintain open communication
        - Help with daily tasks
        - Encourage self-care
        - Stay attentive to any changes
        """)
    elif latest['risk_level'] == "Mild":
        st.info("""
        💙 Increase your support and monitoring
        - Check in more frequently about her feelings
        - Help reduce stressors
        - Encourage rest and self-care
        - Consider suggesting a check-up with her healthcare provider
        """)
    elif latest['risk_level'] == "Moderate":
        st.warning("""
        ⚠️ Professional support may be beneficial
        - Encourage her to contact her healthcare provider
        - Offer to attend appointments with her
        - Increase practical and emotional support
        - Watch for worsening symptoms
        - Consider therapy or counseling
        """)
    else:  # High
        st.error("""
        🚨 Professional help is strongly recommended
        - Contact her healthcare provider immediately
        - Offer to attend appointments with her
        - Watch for signs of crisis (thoughts of self-harm)
        - Provide constant support and monitoring
        - Don't leave her alone if you're concerned about safety
        - Call emergency services if immediate danger
        """)
    
    # Previous assessments
    if len(shared_assessments) > 1:
        st.markdown("---")
        st.subheader("Previous Assessments")
        
        for assessment in shared_assessments[1:]:
            with st.expander(f"Assessment from {format_datetime(assessment['created_at'])[:12]} - Score: {assessment['score']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Score:** {assessment['score']}/30")
                    st.write(f"**Risk Level:** {assessment['risk_level']}")
                with col2:
                    st.write(f"**Date:** {format_datetime(assessment['created_at'])}")
                
                if assessment['summary']:
                    st.write("**Summary:**")
                    st.write(assessment['summary'])
    
    st.markdown("---")
    st.caption("💡 Remember: These results are meant to guide your support, not to diagnose. Always encourage professional help when needed.")
