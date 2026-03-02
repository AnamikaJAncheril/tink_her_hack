import os
from dotenv import load_dotenv

load_dotenv()


SYSTEM_PROMPT = """You are a compassionate postpartum emotional support assistant.

Your role is to:
- Validate feelings and provide emotional support
- Listen with empathy and understanding
- Offer gentle encouragement and reassurance
- Be culturally sensitive and respectful
- Use a calm, warm, and nurturing tone

Important guidelines:
- You do NOT diagnose medical conditions
- You do NOT replace professional healthcare
- If distress appears severe, gently encourage seeking professional help
- Respect the mother's experiences and emotions
- Provide hope and positive reinforcement

Remember: You are here to support, not to judge or diagnose."""

def get_mother_response(user_input: str, chat_history: list = None) -> str:
    """
    Get AI response for mother's emotional support chat.
    
    Args:
        user_input: The mother's message
        chat_history: List of previous messages (optional)
    
    Returns:
        AI response string
    """
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        # Add chat history if provided
        if chat_history:
            messages.extend(chat_history)
        
        # Add current user input
        messages.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"I apologize, but I'm having trouble connecting right now. Please try again in a moment. (Error: {str(e)})"

def generate_assessment_summary(score: int, risk_level: str) -> str:
    """
    Generate an emotional summary based on assessment results.
    
    Args:
        score: Assessment score
        risk_level: Risk level (Normal, Mild, Moderate, High)
    
    Returns:
        Summary string
    """
    try:
        prompt = f"""Based on a postpartum assessment with a score of {score} (risk level: {risk_level}), 
        provide a brief, compassionate summary (2-3 sentences) that:
        1. Acknowledges the mother's current emotional state
        2. Offers gentle encouragement
        3. If risk level is Moderate or High, gently suggests considering professional support
        
        Keep the tone warm, supportive, and non-judgmental."""
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Your assessment has been recorded. Please consider discussing these feelings with a healthcare provider if you're experiencing distress."
