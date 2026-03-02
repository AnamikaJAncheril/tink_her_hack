"""
Simple script to test Groq API connection.
Run this to verify your API key is working before starting the app.
"""

import os
from dotenv import load_dotenv
from groq import Groq

def test_api_connection():
    """Test if Groq API key is valid and working."""
    print("=" * 60)
    print("Testing Groq API Connection")
    print("=" * 60)
    print()
    
    # Load environment variables
    load_dotenv()
    
    # Check if API key exists
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        print("❌ ERROR: GROQ_API_KEY not found in .env file")
        print()
        print("Please:")
        print("1. Get a FREE API key from: https://console.groq.com/keys")
        print("2. Create .env file and add: GROQ_API_KEY=your-key-here")
        print()
        return False
    
    if api_key == "your_groq_api_key_here":
        print("❌ ERROR: Please replace the placeholder with your actual API key")
        print()
        print("Get your FREE key at: https://console.groq.com/keys")
        print()
        return False
    
    print(f"✓ API key found: {api_key[:20]}...")
    print()
    
    # Test API connection
    print("Testing API connection...")
    try:
        client = Groq(api_key=api_key)
        
        # Make a simple test call
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say 'API test successful' in one sentence."}
            ],
            max_tokens=50
        )
        
        result = response.choices[0].message.content
        
        print("✓ API connection successful!")
        print()
        print("Response from Groq:")
        print(f"  {result}")
        print()
        print("=" * 60)
        print("✅ All checks passed! Your API is working correctly.")
        print("=" * 60)
        print()
        print("You can now run the application:")
        print("  streamlit run app.py")
        print()
        return True
        
    except Exception as e:
        print(f"❌ ERROR: API connection failed")
        print()
        print(f"Error details: {str(e)}")
        print()
        print("Common issues:")
        print("1. Invalid API key")
        print("2. API key not activated yet (wait a few minutes)")
        print("3. Network connection issues")
        print()
        print("Please check:")
        print("- Your API key at: https://console.groq.com/keys")
        print("- Make sure you copied the entire key")
        print()
        return False

if __name__ == "__main__":
    test_api_connection()
