import streamlit as st
import database as db
from utils import format_datetime

def show_happy_page(user):
    """Display happiness journal page."""
    st.title("What Makes You Happy 💛")
    st.write("Take a moment to reflect on the things that bring you joy.")
    
    # New entry section
    with st.container():
        st.subheader("Add a New Entry")
        happy_content = st.text_area(
            "What made you happy today?",
            placeholder="Share a moment, thought, or anything that brought you joy...",
            height=150,
            key="happy_input"
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Save Entry", type="primary"):
                if happy_content.strip():
                    db.save_happy_entry(user['id'], happy_content.strip())
                    st.success("Your happy moment has been saved! 🌟")
                    st.session_state.happy_input = ""
                    st.rerun()
                else:
                    st.warning("Please write something before saving.")
    
    st.markdown("---")
    
    # Display past entries
    st.subheader("Your Happy Moments")
    
    entries = db.get_happy_entries(user['id'])
    
    if not entries:
        st.info("You haven't added any entries yet. Start by sharing what makes you happy!")
    else:
        st.write(f"You have {len(entries)} happy moments recorded. 🌸")
        
        for entry in entries:
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"**{format_datetime(entry['created_at'])}**")
                with col2:
                    st.markdown("💛")
                
                st.write(entry['content'])
                st.markdown("---")
