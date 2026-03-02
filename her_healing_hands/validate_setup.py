#!/usr/bin/env python3
"""
Validation script to check if Her Healing Hands is properly set up.
Run this before starting the application.
"""

import sys
import os

def check_python_version():
    """Check if Python version is 3.10+"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 10:
        print("✓ Python version:", f"{version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print("✗ Python 3.10+ required. Current:", f"{version.major}.{version.minor}.{version.micro}")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    required = ['streamlit', 'groq', 'dotenv', 'bcrypt']
    missing = []
    
    for package in required:
        try:
            if package == 'dotenv':
                __import__('dotenv')
            else:
                __import__(package)
            print(f"✓ {package} installed")
        except ImportError:
            print(f"✗ {package} not installed")
            missing.append(package)
    
    if missing:
        print("\nInstall missing packages with:")
        print("pip install -r requirements.txt")
        return False
    return True

def check_env_file():
    """Check if .env file exists and has API key"""
    if not os.path.exists('.env'):
        print("✗ .env file not found")
        print("  Create .env file from .env.example")
        print("  Add your Groq API key")
        return False
    
    print("✓ .env file exists")
    
    # Check if API key is set
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv('GROQ_API_KEY')
    if not api_key or api_key == 'your_groq_api_key_here':
        print("✗ GROQ_API_KEY not set in .env")
        print("  Add your actual Groq API key to .env")
        return False
    
    print("✓ GROQ_API_KEY is set")
    return True

def check_file_structure():
    """Check if all required files exist"""
    required_files = [
        'app.py',
        'database.py',
        'auth.py',
        'utils.py',
        'ai/groq_client.py',
        'ai/mother_ai.py',
        'ai/partner_ai.py',
        'mother/dashboard.py',
        'mother/happy_page.py',
        'mother/thoughts_page.py',
        'mother/assessment_page.py',
        'partner/dashboard.py',
        'partner/care_guide.py',
        'partner/nutrition.py',
        'partner/symptoms.py',
        'partner/results_page.py'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} missing")
            all_exist = False
    
    return all_exist

def main():
    """Run all validation checks"""
    print("=" * 60)
    print("Her Healing Hands - Setup Validation")
    print("=" * 60)
    print()
    
    print("Checking Python version...")
    python_ok = check_python_version()
    print()
    
    print("Checking dependencies...")
    deps_ok = check_dependencies()
    print()
    
    print("Checking environment configuration...")
    env_ok = check_env_file()
    print()
    
    print("Checking file structure...")
    files_ok = check_file_structure()
    print()
    
    print("=" * 60)
    if python_ok and deps_ok and env_ok and files_ok:
        print("✓ All checks passed! Ready to run the application.")
        print("\nStart the app with:")
        print("  streamlit run app.py")
        print("\nOr use the run script:")
        print("  Windows: run.bat")
        print("  Linux/Mac: ./run.sh")
    else:
        print("✗ Some checks failed. Please fix the issues above.")
        sys.exit(1)
    print("=" * 60)

if __name__ == "__main__":
    main()
