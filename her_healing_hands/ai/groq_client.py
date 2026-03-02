"""
Groq API client for Her Healing Hands application.
Provides AI responses for mother support and partner guidance.
"""

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# System prompts
MOTHER_SYSTEM_PROMPT = """You are a compassionate postpartum emotional support assistant.

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

PARTNER_SYSTEM_PROMPT = """You are an educational postpartum support assistant for partners.

Your role is to:
- Explain how to emotionally and practically support a postpartum mother
- Provide respectful, empathetic, and clear advice
- Help partners understand postpartum challenges
- Suggest practical ways to help
- Encourage open communication and patience

Important guidelines:
- You do NOT diagnose medical conditions
- You do NOT replace professional healthcare
- Be respectful and non-judgmental
- Focus on actionable support strategies
- Emphasize the importance of professional help when needed

Remember: You are educating partners to be better supporters."""


def get_ai_response(prompt: str, system_prompt: str = MOTHER_SYSTEM_PROMPT) -> str:
    """
    Get AI response from Groq API.
    
    Args:
        prompt: User's message or question
        system_prompt: System prompt to set AI behavior
    
    Returns:
        AI response string
    """
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"I apologize, but I'm having trouble connecting right now. Please try again in a moment. (Error: {str(e)})"


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
        messages = [{"role": "system", "content": MOTHER_SYSTEM_PROMPT}]
        
        # Add chat history if provided
        if chat_history:
            messages.extend(chat_history[-5:])  # Last 5 messages for context
        
        # Add current user input
        messages.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            model="llama3-8b-8192",
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
    prompt = f"""Based on a postpartum assessment with a score of {score} (risk level: {risk_level}), 
provide a brief, compassionate summary (2-3 sentences) that:
1. Acknowledges the mother's current emotional state
2. Offers gentle encouragement
3. If risk level is Moderate or High, gently suggests considering professional support

Keep the tone warm, supportive, and non-judgmental."""
    
    return get_ai_response(prompt, MOTHER_SYSTEM_PROMPT)


def get_partner_guidance(summary: str, score: int, risk_level: str) -> str:
    """
    Generate guidance for partner based on mother's assessment.
    
    Args:
        summary: Mother's emotional summary
        score: Assessment score
        risk_level: Risk level
    
    Returns:
        Partner guidance string
    """
    prompt = f"""The mother has completed a postpartum assessment with the following results:
- Score: {score}
- Risk Level: {risk_level}
- Summary: {summary}

Provide practical guidance for the partner (3-4 paragraphs) that includes:
1. What this assessment means
2. Specific ways to provide emotional support
3. Practical actions they can take
4. When to encourage professional help

Be compassionate, clear, and actionable."""
    
    return get_ai_response(prompt, PARTNER_SYSTEM_PROMPT)
