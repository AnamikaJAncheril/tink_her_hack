<p align="center"><img src="./assets/logo.jpeg" alt="Her Healing Hands" width="200"></p>

# Her Healing Hands 🌸

## Basic Details

### Team Name: [Your Team Name]

### Team Members
- Member 1: [Name] - [College]
- Member 2: [Name] - [College]
- Member 3: [Name] - [College]

### Hosted Project Link
[mention your project hosted link here]

### Project Description
Her Healing Hands is a comprehensive postpartum support application that provides emotional support and guidance for new mothers and their partners during the critical postpartum period. The platform features AI-powered chat support, mental health assessments, and educational resources.

### The Problem Statement
Postpartum depression affects 1 in 7 new mothers, yet many lack access to immediate emotional support and resources. Partners often feel helpless, not knowing how to provide proper support. The stigma around postpartum mental health prevents many from seeking help.

### The Solution
Her Healing Hands provides a safe, private platform where mothers can track their emotional well-being, journal happy moments, receive AI-powered emotional support, and complete validated mental health assessments (EPDS). Partners get educational resources and can view assessment results (with consent) to better understand and support their loved ones.

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: Python 3.10+
- Frameworks used: Streamlit
- Libraries used: Groq (AI), bcrypt (security), python-dotenv (configuration)
- Tools used: VS Code, Git, SQLite
- AI Model: Llama 3 (via Groq API)

---

## Features

List the key features of your project:

- **Dual Portal System**: Separate interfaces for mothers and partners with role-based access
- **AI-Powered Emotional Support**: Compassionate AI chat using Groq's Llama 3 model for mothers
- **Edinburgh Postnatal Depression Scale (EPDS)**: Validated 10-question assessment for postpartum depression screening
- **Happiness Journal**: Private space for mothers to record positive moments and reflections
- **Partner Education Hub**: Comprehensive guides on postpartum care, nutrition, and symptom recognition
- **Secure Authentication**: bcrypt password hashing and invite code system for partner linking
- **Assessment Sharing**: Mothers can choose to share assessment results with their partners
- **Beautiful UI**: Calming pastel theme (lavender/blush) designed for emotional wellness

---

## Implementation

### For Software:

#### Installation

```bash
# Clone the repository
git clone [your-repo-url]
cd her_healing_hands

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
# Create .env file and add your Groq API key
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

#### Get Free Groq API Key

1. Visit https://console.groq.com/keys
2. Sign up for a free account
3. Generate an API key
4. Copy the key to your `.env` file

#### Run

```bash
# Make sure virtual environment is activated
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![Login Page](docs/screenshots/login.png)
*Welcoming login and registration interface with pastel theme*

![Mother Dashboard](docs/screenshots/mother-dashboard.png)
*Mother's main dashboard showing navigation to journal, chat, and assessments*

![AI Chat Support](docs/screenshots/ai-chat.png)
*Compassionate AI-powered emotional support chat for mothers*

![EPDS Assessment](docs/screenshots/assessment.png)
*Edinburgh Postnatal Depression Scale assessment interface*

![Partner Dashboard](docs/screenshots/partner-dashboard.png)
*Partner's educational hub with care guides and resources*

![Assessment Results](docs/screenshots/results.png)
*Partner view of mother's assessment results (with consent)*

#### Diagrams

**System Architecture:**

```
┌─────────────────────────────────────────────────────────┐
│                    Streamlit Frontend                    │
│  ┌──────────────┐              ┌──────────────┐        │
│  │   Mother     │              │   Partner    │        │
│  │   Portal     │              │   Portal     │        │
│  └──────┬───────┘              └──────┬───────┘        │
└─────────┼──────────────────────────────┼───────────────┘
          │                              │
          ├──────────────┬───────────────┤
          │              │               │
┌─────────▼─────┐ ┌──────▼──────┐ ┌─────▼──────┐
│  Auth Module  │ │  Database   │ │ AI Module  │
│   (bcrypt)    │ │  (SQLite)   │ │  (Groq)    │
└───────────────┘ └─────────────┘ └────────────┘
                        │
              ┌─────────┴─────────┐
              │   Tables:         │
              │   - users         │
              │   - assessments   │
              │   - happy_entries │
              └───────────────────┘
```

*The application uses a modular architecture with separate authentication, database, and AI modules. Streamlit handles the frontend with role-based routing.*

**Application Workflow:**

```
User Registration/Login
         │
         ├─→ Mother Role
         │   ├─→ Dashboard
         │   ├─→ Happiness Journal (CRUD entries)
         │   ├─→ AI Chat Support (Groq API)
         │   ├─→ EPDS Assessment (10 questions)
         │   └─→ Share Results (Generate invite code)
         │
         └─→ Partner Role
             ├─→ Dashboard
             ├─→ Educational Resources
             │   ├─→ Care Guide
             │   ├─→ Nutrition Guide
             │   └─→ Symptom Recognition
             └─→ View Results (Enter invite code)
```

*User flow showing the dual-portal system and key features for each role*

---

## API Documentation

### Groq AI Integration

**Base Configuration:**
- Model: `llama3-8b-8192`
- Temperature: 0.7
- Max Tokens: 500

**Key Functions:**

**`get_mother_response(user_input, chat_history)`**
- **Description:** Generates compassionate emotional support responses for mothers
- **Parameters:**
  - `user_input` (string): Mother's message
  - `chat_history` (list): Previous conversation context (last 5 messages)
- **System Prompt:** Configured for empathetic postpartum support
- **Returns:** AI-generated supportive response

**`generate_assessment_summary(score, risk_level)`**
- **Description:** Creates personalized summary based on EPDS assessment results
- **Parameters:**
  - `score` (integer): Total EPDS score (0-30)
  - `risk_level` (string): Normal/Mild/Moderate/High
- **Returns:** Compassionate 2-3 sentence summary with appropriate guidance

**`get_partner_guidance(summary, score, risk_level)`**
- **Description:** Generates actionable guidance for partners
- **Parameters:**
  - `summary` (string): Mother's assessment summary
  - `score` (integer): Assessment score
  - `risk_level` (string): Risk level
- **Returns:** 3-4 paragraph guide with practical support strategies

---

## Database Schema

**users table:**
```sql
- id (INTEGER PRIMARY KEY)
- email (TEXT UNIQUE)
- password_hash (TEXT)
- role (TEXT) -- 'mother' or 'partner'
- invite_code (TEXT UNIQUE) -- for partner linking
- created_at (TIMESTAMP)
```

**assessments table:**
```sql
- id (INTEGER PRIMARY KEY)
- user_id (INTEGER FOREIGN KEY)
- score (INTEGER)
- risk_level (TEXT)
- responses (TEXT) -- JSON array of answers
- summary (TEXT) -- AI-generated summary
- created_at (TIMESTAMP)
```

**happy_entries table:**
```sql
- id (INTEGER PRIMARY KEY)
- user_id (INTEGER FOREIGN KEY)
- content (TEXT)
- created_at (TIMESTAMP)
```

---

## Security Features

- **Password Hashing:** bcrypt with salt rounds for secure password storage
- **Session Management:** Streamlit session state for user authentication
- **Role-Based Access:** Separate portals with permission checks
- **Invite Code System:** Secure 8-character codes for partner linking
- **Data Privacy:** Assessment sharing requires explicit consent
- **Environment Variables:** Sensitive API keys stored in `.env` file

---

## Project Demo

### Video
[Add your demo video link here - YouTube, Google Drive, etc.]

*Demo showcases: User registration, mother's happiness journal, AI chat interaction, EPDS assessment completion, partner education resources, and assessment result sharing*

### Additional Demos
- Live Demo: [Your hosted link]
- APK Download: N/A (Web application)

---

## AI Tools Used (For Transparency)

**Tool Used:** Kiro AI Assistant

**Purpose:** Development assistance and code generation

**Key Contributions:**
- Generated initial project structure and boilerplate code
- Created database schema and CRUD operations
- Implemented AI integration with Groq API
- Developed authentication system with bcrypt
- Built Streamlit UI components and styling
- Migrated from OpenAI to Groq API
- Debugging and error resolution
- Documentation generation

**Key Prompts Used:**
- "Build a complete production-ready Streamlit web application for postpartum support"
- "Refactor entire project to remove all Gemini and OpenAI integrations and replace with Groq API"
- "Fix Streamlit session state error in happiness journal page"
- "Create comprehensive README in TinkerHub format"

**Percentage of AI-generated code:** Approximately 85%

**Human Contributions:**
- Project concept and requirements definition
- Feature specifications and user flow design
- Testing and quality assurance
- API key configuration
- Logo and branding assets
- Deployment decisions

*Note: This project demonstrates effective human-AI collaboration, where AI accelerated development while human oversight ensured quality and alignment with project goals.*

---

## Team Contributions

- [Name 1]: Project planning, requirements gathering, UI/UX design, testing
- [Name 2]: Backend development, database design, API integration
- [Name 3]: Frontend development, documentation, deployment

---

## Future Enhancements

- Mobile app version (React Native/Flutter)
- Multi-language support
- Professional therapist directory integration
- Community forum for peer support
- Mood tracking with data visualization
- Push notifications for check-ins
- Export assessment history as PDF
- Integration with healthcare providers

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**MIT License** - Permissive license allowing commercial use, modification, distribution, and private use.

---

## Acknowledgments

- Edinburgh Postnatal Depression Scale (EPDS) - Cox, J.L., Holden, J.M., and Sagovsky, R. (1987)
- Groq for providing fast AI inference
- Streamlit for the amazing web framework
- TinkerHub for organizing this hackathon

---

Made with ❤️ at TinkerHub
