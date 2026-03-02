"""
Partner AI support module - uses Groq API.
This module provides guidance for partners supporting postpartum mothers.
"""

from ai.groq_client import get_partner_guidance

# Re-export function for backward compatibility
__all__ = ['get_partner_guidance']

def get_general_support_content() -> str:
    """Get general support guidelines for partners."""
    return """
    ### How to Support Your Partner During Postpartum
    
    **Emotional Support:**
    - Listen without judgment
    - Validate her feelings
    - Be patient and understanding
    - Offer reassurance and encouragement
    - Avoid minimizing her experiences
    
    **Practical Support:**
    - Help with household chores
    - Take care of the baby so she can rest
    - Prepare meals or arrange food delivery
    - Handle visitors and set boundaries
    - Attend medical appointments together
    
    **Communication:**
    - Ask how she's feeling regularly
    - Express your love and appreciation
    - Be open about your own feelings
    - Work together as a team
    - Seek help together if needed
    
    **Self-Care:**
    - Take care of your own mental health
    - Ask for help from family and friends
    - Take breaks when needed
    - Stay connected with your support network
    
    **When to Seek Professional Help:**
    - If she expresses thoughts of self-harm
    - If symptoms worsen or don't improve
    - If she has difficulty bonding with the baby
    - If daily functioning is significantly impaired
    - If you're concerned about her safety
    """
