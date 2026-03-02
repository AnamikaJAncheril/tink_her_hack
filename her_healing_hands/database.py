import sqlite3
from datetime import datetime
from typing import Optional, List, Dict, Any

DB_NAME = "her_healing_hands.db"

def init_db():
    """Initialize database with required tables."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL,
            link_code TEXT,
            linked_user_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Assessments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mother_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            risk_level TEXT NOT NULL,
            summary TEXT,
            consent_given BOOLEAN NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (mother_id) REFERENCES users(id)
        )
    """)
    
    # HappyEntries table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS happy_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mother_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (mother_id) REFERENCES users(id)
        )
    """)
    
    conn.commit()
    conn.close()

def create_user(name: str, email: str, password_hash: str, role: str, link_code: Optional[str] = None) -> Optional[int]:
    """Create a new user and return user ID."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password_hash, role, link_code) VALUES (?, ?, ?, ?, ?)",
            (name, email, password_hash, role, link_code)
        )
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return user_id
    except sqlite3.IntegrityError:
        return None

def get_user_by_email(email: str) -> Optional[Dict[str, Any]]:
    """Get user by email."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
    """Get user by ID."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_user_by_link_code(link_code: str) -> Optional[Dict[str, Any]]:
    """Get user by link code."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE link_code = ?", (link_code,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def link_users(partner_id: int, mother_id: int):
    """Link partner and mother accounts."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET linked_user_id = ? WHERE id = ?", (mother_id, partner_id))
    cursor.execute("UPDATE users SET linked_user_id = ? WHERE id = ?", (partner_id, mother_id))
    conn.commit()
    conn.close()

def save_happy_entry(mother_id: int, content: str):
    """Save a happiness journal entry."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO happy_entries (mother_id, content) VALUES (?, ?)",
        (mother_id, content)
    )
    conn.commit()
    conn.close()

def get_happy_entries(mother_id: int) -> List[Dict[str, Any]]:
    """Get all happiness entries for a mother."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM happy_entries WHERE mother_id = ? ORDER BY created_at DESC",
        (mother_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def save_assessment(mother_id: int, score: int, risk_level: str, summary: str, consent_given: bool):
    """Save an assessment."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO assessments (mother_id, score, risk_level, summary, consent_given) VALUES (?, ?, ?, ?, ?)",
        (mother_id, score, risk_level, summary, consent_given)
    )
    conn.commit()
    conn.close()

def get_latest_assessment(mother_id: int) -> Optional[Dict[str, Any]]:
    """Get the latest assessment for a mother."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM assessments WHERE mother_id = ? ORDER BY created_at DESC LIMIT 1",
        (mother_id,)
    )
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_all_assessments(mother_id: int) -> List[Dict[str, Any]]:
    """Get all assessments for a mother."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM assessments WHERE mother_id = ? ORDER BY created_at DESC",
        (mother_id,)
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
