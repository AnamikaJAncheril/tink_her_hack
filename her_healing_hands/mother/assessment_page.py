import streamlit as st
import database as db
from utils import calculate_risk_level, get_risk_color
from ai.mother_ai import generate_assessment_summary

# Edinburgh Postnatal Depression Scale questions
QUESTIONS = [
    {
        "text": "I have been able to laugh and see the funny side of things",
        "options": ["As much as I always could", "Not quite so much now", "Definitely not so much now", "Not at all"]
    },
    {
        "text": "I have looked forward with enjoyment to things",
        "options": ["As much as I ever did", "Rather less than I used to", "Definitely less than I used to", "Hardly at all"]
    },
    {
        "text": "I have blamed myself unnecessarily when things went wrong",
        "options": ["No, never", "Not very often", "Yes, some of the time", "Yes, most of the time"]
    },
    {
        "text": "I have been anxious or worried for no good reason",
        "options": ["No, not at all", "Hardly ever", "Yes, sometimes", "Yes, very often"]
    },
    {
        "text": "I have felt scared or panicky for no very good reason",
        "options": ["No, not at all", "No, not much", "Yes, sometimes", "Yes, quite a lot"]
    },
    {
        "text": "Things have been getting on top of me",
        "options": ["No, I have been coping as well as ever", "No, most of the time I have coped quite well", "Yes, sometimes I haven't been coping as well as usual", "Yes, most of the time I haven't been able to cope at all"]
    },
    {
        "text": "I have been so unhappy that I have had difficulty sleeping",
        "options": ["No, not at all", "Not very often", "Yes, sometimes", "Yes, most of the time"]
    },
    {
        "text": "I have felt sad or miserable",
        "options": ["No, not at all", "Not very often", "Yes, quite often", "Yes, most of the time"]
    },
    {
        "text": "I have been so unhappy that I have been crying",
        "options": ["No, never", "Only occasionally", "Yes, quite often", "Yes, most of the time"]
    },
    {
        "text": "The thought of harming myself has occurred to me",
        "options": ["Never", "Hardly ever", "Sometimes", "Yes, quite often"]
    }
]

def show_assessment_page(user):
    """Display weekly assessment page."""
    st.title("Weekly Assessment 📊")
    st.write("This assessment helps track your emotional well-being. Please answer honestly based on how you've felt in the past 7 days.")
    
    st.info("📋 Edinburgh Postnatal Depression Scale (EPDS)")
    
    # Initialize answers in session state
    if 'assessment_answers' not in st.session_state:
        st.session_state.assessment_answers = {}
    
    # Display questions
    with st.form("assessment_form"):
        for i, question in enumerate(QUESTIONS):
            st.markdown(f"**{i+1}. {question['text']}**")
            answer = st.radio(
                f"Question {i+1}",
                options=range(len(question['options'])),
                format_func=lambda x, opts=question['options']: opts[x],
                key=f"q_{i}",
                label_visibility="collapsed"
            )
            st.session_state.assessment_answers[i] = answer
            st.markdown("---")
        
        # Consent checkbox
        st.subheader("Sharing Preferences")
        consent = st.checkbox(
            "I consent to share my assessment results with my partner",
            help="Your partner will only see your results if they are linked to your account and you give consent."
        )
        
        # Submit button
        submitted = st.form_submit_button("Submit Assessment", type="primary", use_container_width=True)
        
        if submitted:
            # Calculate score
            score = sum(st.session_state.assessment_answers.values())
            risk_level = calculate_risk_level(score)
            
            # Generate AI summary
            with st.spinner("Generating your personalized summary..."):
                summary = generate_assessment_summary(score, risk_level)
            
            # Save to database
            db.save_assessment(user['id'], score, risk_level, summary, consent)
            
            # Clear answers
            st.session_state.assessment_answers = {}
            
            # Show results
            st.success("✅ Assessment completed!")
            st.balloons()
            
            # Display results
            st.markdown("---")
            st.subheader("Your Results")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Score", f"{score}/30")
            with col2:
                st.markdown(f"**Risk Level:** <span style='background-color: {get_risk_color(risk_level)}; padding: 5px 15px; border-radius: 5px;'>{risk_level}</span>", unsafe_allow_html=True)
            
            st.markdown("---")
            st.write("**Personalized Summary:**")
            st.info(summary)
            
            if score >= 15:
                st.warning("⚠️ Your score indicates you may be experiencing significant distress. Please consider reaching out to a healthcare provider for support.")
            
            if consent:
                st.success("✓ Your results will be shared with your partner.")
            else:
                st.info("Your results are private and will not be shared.")
    
    # Show previous assessments
    st.markdown("---")
    st.subheader("Previous Assessments")
    
    assessments = db.get_all_assessments(user['id'])
    
    if not assessments:
        st.info("You haven't completed any assessments yet.")
    else:
        for assessment in assessments:
            with st.expander(f"Assessment from {assessment['created_at'][:10]} - Score: {assessment['score']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Score:** {assessment['score']}/30")
                    st.write(f"**Risk Level:** {assessment['risk_level']}")
                with col2:
                    st.write(f"**Shared:** {'Yes' if assessment['consent_given'] else 'No'}")
                
                if assessment['summary']:
                    st.write("**Summary:**")
                    st.write(assessment['summary'])
