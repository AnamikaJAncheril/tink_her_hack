import streamlit as st

def show_care_guide():
    """Display support and care guide for partners."""
    st.title("How to Support Your Partner 🤝")
    
    st.write("Being a supportive partner during the postpartum period is essential. Here's a comprehensive guide to help you.")
    
    st.markdown("---")
    
    # Emotional Support
    with st.expander("💙 Emotional Support", expanded=True):
        st.markdown("""
        **Listen Actively:**
        - Give her your full attention when she talks
        - Don't interrupt or try to "fix" everything immediately
        - Validate her feelings: "That sounds really hard" or "I understand why you feel that way"
        
        **Be Patient:**
        - Hormonal changes can affect mood and emotions
        - Recovery takes time - both physical and emotional
        - Don't take mood swings personally
        
        **Show Appreciation:**
        - Acknowledge the hard work she's doing
        - Express gratitude for her efforts
        - Remind her she's doing a great job
        
        **Encourage Self-Care:**
        - Help her find time to rest
        - Support her in activities she enjoys
        - Remind her that taking care of herself helps her take care of the baby
        """)
    
    # Practical Support
    with st.expander("🏠 Practical Support"):
        st.markdown("""
        **Household Tasks:**
        - Take over cooking, cleaning, and laundry
        - Grocery shopping and meal planning
        - Keep the home organized and comfortable
        
        **Baby Care:**
        - Share nighttime duties when possible
        - Change diapers, give baths, soothe the baby
        - Learn about baby care alongside your partner
        
        **Manage Visitors:**
        - Set boundaries with family and friends
        - Limit visiting hours if needed
        - Protect her rest time
        
        **Handle Logistics:**
        - Schedule and attend medical appointments
        - Manage paperwork and administrative tasks
        - Take care of errands
        """)
    
    # Communication
    with st.expander("💬 Communication Tips"):
        st.markdown("""
        **What to Say:**
        - "How are you feeling today?"
        - "What can I do to help?"
        - "You're doing an amazing job"
        - "I'm here for you"
        - "It's okay to not be okay"
        
        **What to Avoid:**
        - "You should be happy - you have a healthy baby"
        - "Other mothers seem to handle this better"
        - "Just snap out of it"
        - "You're overreacting"
        - Comparing her to others
        
        **Check-In Regularly:**
        - Ask about her feelings daily
        - Create a safe space for honest conversation
        - Be open about your own feelings too
        """)
    
    # Warning Signs
    with st.expander("⚠️ When to Seek Professional Help"):
        st.markdown("""
        **Seek immediate help if she:**
        - Expresses thoughts of harming herself or the baby
        - Shows signs of psychosis (hallucinations, delusions)
        - Is unable to care for herself or the baby
        - Has severe anxiety or panic attacks
        - Shows extreme mood swings
        
        **Contact:**
        - Her healthcare provider
        - Mental health professional
        - Crisis hotline
        - Emergency services if immediate danger
        
        **Remember:** Seeking help is a sign of strength, not weakness.
        """)
    
    # Self-Care for Partners
    with st.expander("🧘 Taking Care of Yourself"):
        st.markdown("""
        **You Matter Too:**
        - Your mental health is important
        - It's okay to feel overwhelmed
        - Ask for help when you need it
        
        **Stay Connected:**
        - Maintain relationships with friends and family
        - Join partner support groups
        - Talk to other new parents
        
        **Take Breaks:**
        - Accept help from others
        - Take time for activities you enjoy
        - Rest when possible
        
        **Seek Support:**
        - Talk to a therapist if needed
        - Don't try to handle everything alone
        - Remember: you can't pour from an empty cup
        """)
    
    st.markdown("---")
    st.info("💡 Remember: Every mother's experience is unique. What works for one may not work for another. The most important thing is to be present, patient, and supportive.")
