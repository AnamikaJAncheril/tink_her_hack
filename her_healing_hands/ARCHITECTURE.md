# Her Healing Hands - Architecture Diagram

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     STREAMLIT WEB APP                        │
│                        (app.py)                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ├─────────────────┐
                              ▼                 ▼
                    ┌──────────────┐   ┌──────────────┐
                    │ MOTHER PORTAL│   │PARTNER PORTAL│
                    └──────────────┘   └──────────────┘
                              │                 │
        ┌─────────────────────┼─────────────────┼──────────────┐
        │                     │                 │              │
        ▼                     ▼                 ▼              ▼
┌──────────────┐    ┌──────────────┐   ┌──────────────┐  ┌──────────────┐
│ AUTHENTICATION│    │   DATABASE   │   │  AI MODULES  │  │    UTILS     │
│   (auth.py)   │    │(database.py) │   │   (ai/*.py)  │  │  (utils.py)  │
└──────────────┘    └──────────────┘   └──────────────┘  └──────────────┘
        │                     │                 │              │
        │                     ▼                 ▼              │
        │            ┌──────────────┐   ┌──────────────┐      │
        │            │    SQLite    │   │  OpenAI API  │      │
        │            │   Database   │   │   (GPT-4o)   │      │
        │            └──────────────┘   └──────────────┘      │
        │                                                      │
        └──────────────────────────────────────────────────────┘
```

## Component Breakdown

### 1. Entry Point (app.py)
```
app.py
├── Page Configuration
├── Database Initialization
├── Session State Management
├── Login/Register UI
├── Mother Portal Router
└── Partner Portal Router
```

### 2. Authentication Layer (auth.py)
```
auth.py
├── register_user()
│   ├── Validate inputs
│   ├── Hash password (bcrypt)
│   ├── Generate invite code (Mother)
│   ├── Validate invite code (Partner)
│   └── Create user in database
│
├── login_user()
│   ├── Validate credentials
│   ├── Verify password hash
│   └── Return user object
│
└── Helper Functions
    ├── hash_password()
    ├── verify_password()
    └── generate_invite_code()
```

### 3. Database Layer (database.py)
```
database.py
├── init_db()
│   ├── Create users table
│   ├── Create assessments table
│   └── Create happy_entries table
│
├── User Operations
│   ├── create_user()
│   ├── get_user_by_email()
│   ├── get_user_by_id()
│   ├── get_user_by_link_code()
│   └── link_users()
│
├── Assessment Operations
│   ├── save_assessment()
│   ├── get_latest_assessment()
│   └── get_all_assessments()
│
└── Journal Operations
    ├── save_happy_entry()
    └── get_happy_entries()
```

### 4. Mother Portal
```
mother/
├── dashboard.py
│   ├── Display invite code
│   ├── Show metrics
│   ├── Recent activity
│   └── Quick actions
│
├── happy_page.py
│   ├── New entry form
│   ├── Save to database
│   └── Display past entries
│
├── thoughts_page.py
│   ├── Chat interface
│   ├── Call mother_ai.py
│   ├── Display conversation
│   └── Session-based history
│
└── assessment_page.py
    ├── Display EPDS questions
    ├── Collect answers
    ├── Calculate score
    ├── Determine risk level
    ├── Generate AI summary
    ├── Consent checkbox
    └── Save to database
```

### 5. Partner Portal
```
partner/
├── dashboard.py
│   ├── Connection status
│   ├── Metrics overview
│   ├── Latest assessment preview
│   └── Quick actions
│
├── care_guide.py
│   ├── Emotional support tips
│   ├── Practical help guide
│   ├── Communication advice
│   └── Warning signs
│
├── nutrition.py
│   ├── Nutrition importance
│   ├── Essential nutrients
│   ├── Meal ideas
│   └── Partner help tips
│
├── symptoms.py
│   ├── Baby blues vs PPD
│   ├── Physical symptoms
│   ├── Emotional symptoms
│   ├── Warning signs
│   └── Resources
│
└── results_page.py
    ├── Check linking status
    ├── Verify consent
    ├── Display assessment
    ├── Generate AI guidance
    └── Show recommendations
```

### 6. AI Integration
```
ai/
├── mother_ai.py
│   ├── SYSTEM_PROMPT (compassionate support)
│   ├── get_mother_response()
│   │   ├── Build message history
│   │   ├── Call OpenAI API
│   │   └── Return response
│   └── generate_assessment_summary()
│       ├── Create prompt from score
│       ├── Call OpenAI API
│       └── Return summary
│
└── partner_ai.py
    ├── SYSTEM_PROMPT (educational guidance)
    ├── get_partner_guidance()
    │   ├── Build context from assessment
    │   ├── Call OpenAI API
    │   └── Return guidance
    └── get_general_support_content()
        └── Return static content
```

### 7. Utilities (utils.py)
```
utils.py
├── Risk Assessment
│   ├── calculate_risk_level()
│   └── get_risk_color()
│
├── Formatting
│   └── format_datetime()
│
├── UI Components
│   ├── apply_custom_css()
│   └── show_logo()
│
└── Session Management
    ├── init_session_state()
    └── logout()
```

## Data Flow Diagrams

### User Registration Flow
```
User Input
    │
    ▼
Register Form (app.py)
    │
    ▼
auth.register_user()
    │
    ├─── Validate inputs
    ├─── Hash password
    ├─── Generate/validate invite code
    │
    ▼
database.create_user()
    │
    ▼
SQLite Database
    │
    ▼
Success/Error Message
```

### Assessment Flow (Mother)
```
Mother completes EPDS
    │
    ▼
assessment_page.py
    │
    ├─── Collect 10 answers
    ├─── Calculate score (0-30)
    ├─── Determine risk level
    ├─── Check consent
    │
    ▼
mother_ai.generate_assessment_summary()
    │
    ▼
OpenAI API (GPT-4o)
    │
    ▼
database.save_assessment()
    │
    ▼
SQLite Database
    │
    ▼
Display Results
```

### Assessment View Flow (Partner)
```
Partner clicks "Assessment Results"
    │
    ▼
results_page.py
    │
    ├─── Check if linked
    ├─── Get mother's assessments
    ├─── Filter by consent
    │
    ▼
Display latest assessment
    │
    ▼
partner_ai.get_partner_guidance()
    │
    ▼
OpenAI API (GPT-4o)
    │
    ▼
Display guidance + recommendations
```

### Chat Flow (Mother)
```
Mother sends message
    │
    ▼
thoughts_page.py
    │
    ├─── Add to chat history
    │
    ▼
mother_ai.get_mother_response()
    │
    ├─── Build context
    ├─── Include history
    │
    ▼
OpenAI API (GPT-4o)
    │
    ▼
Display response
    │
    ▼
Update session state
```

## Database Schema

### Entity Relationship Diagram
```
┌─────────────────┐
│     USERS       │
├─────────────────┤
│ id (PK)         │
│ name            │
│ email (UNIQUE)  │
│ password_hash   │
│ role            │
│ link_code       │
│ linked_user_id  │◄─────┐
│ created_at      │      │
└─────────────────┘      │
        │                │
        │ 1              │ 1
        │                │
        │ Mother         │ Partner
        │                │
        │ 1              │
        │                │
        │ *              │
        ▼                │
┌─────────────────┐      │
│  ASSESSMENTS    │      │
├─────────────────┤      │
│ id (PK)         │      │
│ mother_id (FK)  │──────┘
│ score           │
│ risk_level      │
│ summary         │
│ consent_given   │
│ created_at      │
└─────────────────┘
        │
        │ Mother
        │
        │ 1
        │
        │ *
        ▼
┌─────────────────┐
│  HAPPY_ENTRIES  │
├─────────────────┤
│ id (PK)         │
│ mother_id (FK)  │
│ content         │
│ created_at      │
└─────────────────┘
```

## Security Architecture

### Authentication Flow
```
User Credentials
    │
    ▼
auth.login_user()
    │
    ├─── Get user from database
    ├─── Verify password hash (bcrypt)
    │
    ▼
Session State
    │
    ├─── logged_in = True
    ├─── user = {user_data}
    │
    ▼
Portal Access Granted
```

### Privacy Controls
```
Assessment Created
    │
    ├─── consent_given = True/False
    │
    ▼
Partner Requests Results
    │
    ├─── Check linked_user_id
    ├─── Filter by consent_given
    │
    ▼
Display Only Consented Results
```

## Technology Stack

### Frontend
```
Streamlit
├── UI Components
├── Session Management
├── Form Handling
└── Routing
```

### Backend
```
Python 3.10+
├── SQLite (Database)
├── bcrypt (Password Hashing)
├── OpenAI SDK (AI Integration)
└── python-dotenv (Config)
```

### External Services
```
OpenAI API
└── GPT-4o Model
    ├── Mother Support Chat
    ├── Assessment Summaries
    └── Partner Guidance
```

## Deployment Architecture

### Local Development
```
Developer Machine
├── Python Environment
├── SQLite Database (local file)
├── .env (API keys)
└── Streamlit Server (localhost:8501)
```

### Production (Example: Streamlit Cloud)
```
Streamlit Cloud
├── Git Repository
├── Python Environment (auto)
├── Secrets Management
├── HTTPS (auto)
└── Public URL
```

## Session State Management

```
st.session_state
├── logged_in (Boolean)
├── user (Dict)
│   ├── id
│   ├── name
│   ├── email
│   ├── role
│   ├── link_code
│   └── linked_user_id
├── chat_history (List)
│   └── [{role, content}, ...]
├── page (String)
└── assessment_answers (Dict)
```

## Error Handling

```
User Action
    │
    ▼
Try Operation
    │
    ├─── Success → Continue
    │
    └─── Error
         │
         ├─── Validation Error → User Message
         ├─── Database Error → Log + User Message
         ├─── API Error → Fallback Message
         └─── Unknown Error → Generic Message
```

## Performance Considerations

### Caching Strategy
- Session-based chat history
- Database connection pooling (future)
- Static content caching

### Optimization Points
- Lazy loading of AI responses
- Efficient database queries
- Minimal API calls
- Streamlit caching decorators (future)

## Scalability Path

### Current (Single Instance)
```
User → Streamlit App → SQLite → OpenAI API
```

### Future (Scaled)
```
Users → Load Balancer → Multiple App Instances
                              │
                              ├→ PostgreSQL (shared)
                              └→ OpenAI API (rate limited)
```

## Module Dependencies

```
app.py
├── database
├── auth
├── utils
├── mother.*
└── partner.*

mother/thoughts_page.py
└── ai.mother_ai

partner/results_page.py
└── ai.partner_ai

ai.*
├── openai
└── dotenv

auth
└── bcrypt

All modules
└── streamlit
```

---

**Architecture Version**: 1.0
**Last Updated**: Project Creation
**Status**: Production Ready
