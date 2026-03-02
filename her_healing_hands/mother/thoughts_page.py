import streamlit as st
from ai.mother_ai import get_mother_response

def show_thoughts_page(user):
    """Display emotional support chat page."""
    st.title("Share Your Thoughts 📝")
    st.write("I'm here to listen and support you. Share whatever is on your mind.")
    
    # Display chat history
    chat_container = st.container()
    
    with chat_container:
        if not st.session_state.chat_history:
            st.info("👋 Hello! I'm here to provide emotional support. Feel free to share your thoughts, feelings, or concerns. Everything you share is private and confidential.")
        else:
            for message in st.session_state.chat_history:
                if message['role'] == 'user':
                    with st.chat_message("user"):
                        st.write(message['content'])
                else:
                    with st.chat_message("assistant"):
                        st.write(message['content'])
    
    # Chat input
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({
            'role': 'user',
            'content': user_input
        })
        
        # Get AI response
        with st.spinner("Thinking..."):
            response = get_mother_response(user_input, st.session_state.chat_history[:-1])
        
        # Add assistant response to history
        st.session_state.chat_history.append({
            'role': 'assistant',
            'content': response
        })
        
        st.rerun()
    
    # Clear chat button
    st.markdown("---")
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()
    
    # Disclaimer
    st.caption("⚠️ This chat provides emotional support but is not a substitute for professional medical advice. If you're experiencing severe distress, please contact a healthcare provider or crisis helpline.")
