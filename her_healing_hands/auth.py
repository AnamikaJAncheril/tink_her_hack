import bcrypt
import secrets
import string
from typing import Optional, Tuple
import database as db

def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def verify_password(password: str, password_hash: str) -> bool:
    """Verify a password against its hash."""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

def generate_invite_code() -> str:
    """Generate a unique invite code like HH-8F4K29."""
    chars = string.ascii_uppercase + string.digits
    code = ''.join(secrets.choice(chars) for _ in range(6))
    return f"HH-{code}"

def register_user(name: str, email: str, password: str, role: str, invite_code: Optional[str] = None) -> Tuple[bool, str]:
    """
    Register a new user.
    Returns (success, message).
    """
    # Validate inputs
    if not name or not email or not password:
        return False, "All fields are required."
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    
    # Check if email already exists
    existing_user = db.get_user_by_email(email)
    if existing_user:
        return False, "Email already registered."
    
    # Handle role-specific logic
    link_code = None
    mother_id = None
    
    if role == "Mother":
        # Generate unique invite code
        link_code = generate_invite_code()
        # Ensure uniqueness
        while db.get_user_by_link_code(link_code):
            link_code = generate_invite_code()
    
    elif role == "Partner":
        # Validate invite code
        if not invite_code:
            return False, "Invite code is required for partners."
        
        mother = db.get_user_by_link_code(invite_code)
        if not mother:
            return False, "Invalid invite code."
        
        if mother['role'] != "Mother":
            return False, "Invalid invite code."
        
        mother_id = mother['id']
    
    # Hash password
    password_hash = hash_password(password)
    
    # Create user
    user_id = db.create_user(name, email, password_hash, role, link_code)
    
    if not user_id:
        return False, "Registration failed. Please try again."
    
    # Link users if partner
    if role == "Partner" and mother_id:
        db.link_users(user_id, mother_id)
    
    return True, "Registration successful!"

def login_user(email: str, password: str) -> Tuple[bool, Optional[dict], str]:
    """
    Login a user.
    Returns (success, user_dict, message).
    """
    if not email or not password:
        return False, None, "Email and password are required."
    
    user = db.get_user_by_email(email)
    
    if not user:
        return False, None, "Invalid email or password."
    
    if not verify_password(password, user['password_hash']):
        return False, None, "Invalid email or password."
    
    return True, user, "Login successful!"
