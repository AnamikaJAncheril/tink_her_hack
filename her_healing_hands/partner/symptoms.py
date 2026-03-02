import streamlit as st

def show_symptoms_page():
    """Display information about postpartum symptoms."""
    st.title("Postpartum Symptoms ⚠️")
    
    st.write("Understanding postpartum symptoms helps you recognize what's normal and when to seek help.")
    
    st.markdown("---")
    
    # Baby Blues vs PPD
    with st.expander("😢 Baby Blues vs. Postpartum Depression", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Baby Blues (Normal)**")
            st.markdown("""
            - Affects 70-80% of new mothers
            - Starts 2-3 days after delivery
            - Lasts up to 2 weeks
            
            **Symptoms:**
            - Mood swings
            - Crying spells
            - Anxiety
            - Difficulty sleeping
            - Feeling overwhelmed
            
            **What to Do:**
            - Rest as much as possible
            - Accept help from others
            - Talk about feelings
            - Usually resolves on its own
            """)
        
        with col2:
            st.markdown("**Postpartum Depression (Needs Help)**")
            st.markdown("""
            - Affects 10-20% of new mothers
            - Can start anytime in first year
            - Lasts longer than 2 weeks
            
            **Symptoms:**
            - Persistent sadness
            - Loss of interest in activities
            - Severe mood swings
            - Difficulty bonding with baby
            - Thoughts of self-harm
            
            **What to Do:**
            - Contact healthcare provider
            - Seek professional help
            - Consider therapy/medication
            - Join support groups
            """)
    
    # Common Physical Symptoms
    with st.expander("🩺 Physical Symptoms"):
        st.markdown("""
        **Normal Physical Changes:**
        - Fatigue and exhaustion
        - Breast engorgement or soreness
        - Vaginal bleeding (lochia) for 4-6 weeks
        - Cramping as uterus shrinks
        - Constipation
        - Hemorrhoids
        - Night sweats
        - Hair loss (3-6 months postpartum)
        
        **When to Call Doctor:**
        - Heavy bleeding (soaking pad in 1 hour)
        - Fever over 100.4°F
        - Severe abdominal pain
        - Foul-smelling discharge
        - Painful, red, swollen breasts
        - Severe headaches
        - Chest pain or difficulty breathing
        - Signs of infection at incision site
        """)
    
    # Emotional Symptoms
    with st.expander("💭 Emotional Symptoms"):
        st.markdown("""
        **Common Feelings:**
        - Overwhelmed by responsibilities
        - Anxious about baby's health
        - Worried about being a good mother
        - Frustrated with lack of sleep
        - Isolated or lonely
        - Loss of identity
        - Relationship strain
        
        **Concerning Signs:**
        - Persistent sadness or hopelessness
        - Severe anxiety or panic attacks
        - Inability to care for self or baby
        - Thoughts of harming self or baby
        - Feeling disconnected from baby
        - Extreme mood swings
        - Withdrawal from loved ones
        """)
    
    # Postpartum Anxiety
    with st.expander("😰 Postpartum Anxiety"):
        st.markdown("""
        **What It Is:**
        - Excessive worry and fear
        - Can occur with or without depression
        - Affects about 10% of new mothers
        
        **Symptoms:**
        - Constant worry about baby
        - Racing thoughts
        - Difficulty sleeping even when baby sleeps
        - Physical symptoms (rapid heartbeat, nausea)
        - Intrusive thoughts
        - Feeling on edge
        
        **How to Help:**
        - Encourage professional help
        - Practice relaxation techniques together
        - Help reduce stressors
        - Provide reassurance
        - Don't dismiss her concerns
        """)
    
    # Postpartum Psychosis
    with st.expander("🚨 Postpartum Psychosis (EMERGENCY)"):
        st.markdown("""
        **What It Is:**
        - Rare but serious condition (1-2 per 1,000)
        - Usually starts within 2 weeks of delivery
        - Requires immediate medical attention
        
        **Symptoms:**
        - Hallucinations (seeing/hearing things)
        - Delusions (false beliefs)
        - Severe confusion
        - Paranoia
        - Rapid mood swings
        - Bizarre behavior
        - Thoughts of harming self or baby
        
        **ACTION REQUIRED:**
        - Call emergency services immediately
        - Do not leave her alone
        - Remove access to weapons/medications
        - This is a medical emergency
        """)
    
    # Risk Factors
    with st.expander("⚠️ Risk Factors"):
        st.markdown("""
        **Higher Risk For:**
        - History of depression or anxiety
        - Previous postpartum depression
        - Family history of mental illness
        - Stressful life events
        - Lack of support system
        - Difficult pregnancy or delivery
        - Financial stress
        - Relationship problems
        - Sleep deprivation
        - Thyroid problems
        """)
    
    # How to Help
    with st.expander("🤝 How You Can Help"):
        st.markdown("""
        **Be Observant:**
        - Watch for warning signs
        - Take concerns seriously
        - Don't wait for symptoms to worsen
        
        **Provide Support:**
        - Listen without judgment
        - Help with baby care and household tasks
        - Encourage rest and self-care
        - Reduce stressors when possible
        
        **Seek Help:**
        - Contact healthcare provider if concerned
        - Help her make appointments
        - Attend appointments with her
        - Follow treatment recommendations
        
        **Stay Informed:**
        - Learn about postpartum conditions
        - Know warning signs
        - Have emergency contacts ready
        - Join partner support groups
        """)
    
    # Resources
    with st.expander("📞 Resources & Hotlines"):
        st.markdown("""
        **Crisis Support:**
        - National Suicide Prevention Lifeline: 988
        - Crisis Text Line: Text HOME to 741741
        - Postpartum Support International: 1-800-944-4773
        
        **Online Resources:**
        - Postpartum Support International: postpartum.net
        - National Maternal Mental Health Hotline: 1-833-943-5746
        
        **When to Call 911:**
        - Thoughts of harming self or baby
        - Psychosis symptoms
        - Severe medical emergency
        """)
    
    st.markdown("---")
    st.warning("⚠️ If you're concerned about your partner's health or safety, don't hesitate to seek professional help. Trust your instincts.")
