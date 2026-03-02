# Testing Guide - Her Healing Hands

## Pre-Testing Setup

1. **Validate Setup**
   ```bash
   python validate_setup.py
   ```

2. **Start Application**
   ```bash
   streamlit run app.py
   ```

3. **Open Browser**
   - Application should open at `http://localhost:8501`

## Test Scenarios

### Scenario 1: Mother Registration & Basic Flow

**Step 1: Register as Mother**
1. Click "Register" tab
2. Enter:
   - Name: "Sarah Johnson"
   - Email: "sarah@example.com"
   - Password: "test123"
   - Role: "Mother"
3. Click "Register"
4. Verify success message
5. Note: Invite code will be generated

**Step 2: Login as Mother**
1. Click "Login" tab
2. Enter credentials
3. Click "Login"
4. Verify redirect to dashboard

**Step 3: View Dashboard**
1. Verify invite code is displayed
2. Check metrics (should show 0 entries, 0 assessments)
3. Verify partner status shows "✗"

**Step 4: Add Happy Entry**
1. Click "💛 What Makes You Happy"
2. Enter: "My baby smiled at me today!"
3. Click "Save Entry"
4. Verify success message
5. Verify entry appears below

**Step 5: Chat Support**
1. Click "📝 Share Your Thoughts"
2. Type: "I'm feeling overwhelmed with all the changes"
3. Press Enter
4. Verify AI response appears
5. Verify response is compassionate and supportive

**Step 6: Take Assessment**
1. Click "📊 Weekly Assessment"
2. Answer all 10 questions
3. Check "Share with partner" checkbox
4. Click "Submit Assessment"
5. Verify:
   - Success message
   - Balloons animation
   - Score displayed
   - Risk level shown with color
   - AI summary generated

**Step 7: Return to Dashboard**
1. Click "🏠 Dashboard"
2. Verify updated metrics
3. Verify latest assessment appears
4. Note the invite code for partner registration

### Scenario 2: Partner Registration & Linking

**Step 1: Logout**
1. Click "🚪 Logout" in sidebar

**Step 2: Register as Partner**
1. Click "Register" tab
2. Enter:
   - Name: "John Johnson"
   - Email: "john@example.com"
   - Password: "test123"
   - Role: "Partner"
   - Invite Code: [Use code from mother's dashboard]
3. Click "Register"
4. Verify success message

**Step 3: Login as Partner**
1. Enter credentials
2. Click "Login"
3. Verify redirect to partner dashboard

**Step 4: View Partner Dashboard**
1. Verify connection status shows mother's name
2. Check metrics
3. Verify latest risk level is displayed

**Step 5: Explore Support Guide**
1. Click "🤝 How to Support"
2. Expand each section
3. Verify content is comprehensive and helpful

**Step 6: View Nutrition Info**
1. Click "🍲 Nutrition"
2. Expand sections
3. Verify meal ideas and tips are present

**Step 7: View Symptoms Info**
1. Click "⚠️ Postpartum Symptoms"
2. Expand "Baby Blues vs. Postpartum Depression"
3. Verify warning signs are clear
4. Check emergency resources

**Step 8: View Assessment Results**
1. Click "📈 Assessment Results"
2. Verify:
   - Score is displayed
   - Risk level shown with color
   - Mother's summary appears
   - AI-generated partner guidance loads
   - Recommended actions based on risk level
   - Previous assessments section

### Scenario 3: Privacy & Consent Testing

**Step 1: Login as Mother**
1. Logout from partner account
2. Login as mother

**Step 2: Take Assessment Without Consent**
1. Go to "📊 Weekly Assessment"
2. Answer questions
3. DO NOT check "Share with partner"
4. Submit assessment

**Step 3: Login as Partner**
1. Logout and login as partner
2. Go to "📈 Assessment Results"
3. Verify:
   - Only assessments with consent are shown
   - New assessment is NOT visible

**Step 4: Verify Privacy**
1. Confirm partner cannot see non-consented results
2. Verify appropriate message is displayed

### Scenario 4: Invalid Invite Code

**Step 1: Logout**
1. Logout from any account

**Step 2: Try Invalid Code**
1. Click "Register"
2. Enter new details
3. Select "Partner"
4. Enter invalid code: "HH-INVALID"
5. Click "Register"
6. Verify error message: "Invalid invite code"

### Scenario 5: Multiple Assessments

**Step 1: Login as Mother**
1. Login with mother credentials

**Step 2: Take Multiple Assessments**
1. Complete 3 different assessments
2. Vary the consent checkbox
3. Verify each saves correctly

**Step 3: View History**
1. Check dashboard shows count
2. Expand previous assessments
3. Verify all are listed chronologically

**Step 4: Partner View**
1. Login as partner
2. View assessment results
3. Verify only consented assessments appear
4. Check previous assessments section

### Scenario 6: Edge Cases

**Test 1: Empty Fields**
- Try registering with empty fields
- Verify validation messages

**Test 2: Duplicate Email**
- Try registering with existing email
- Verify error message

**Test 3: Short Password**
- Try password less than 6 characters
- Verify error message

**Test 4: Chat Without Input**
- Try sending empty message in chat
- Verify it doesn't crash

**Test 5: Assessment Without Answers**
- Try submitting assessment without answering
- Verify all questions are answered

## Expected Results Summary

### Mother Portal
- ✓ Registration with invite code generation
- ✓ Login and authentication
- ✓ Dashboard with metrics
- ✓ Happy journal entries save and display
- ✓ AI chat provides supportive responses
- ✓ Assessment calculates score correctly
- ✓ Risk levels display with correct colors
- ✓ AI summaries generate
- ✓ Consent checkbox controls sharing

### Partner Portal
- ✓ Registration with invite code validation
- ✓ Account linking works
- ✓ Dashboard shows connection status
- ✓ Educational content is comprehensive
- ✓ Assessment results respect consent
- ✓ AI guidance generates for assessments
- ✓ Recommended actions match risk level
- ✓ Privacy is maintained

### Security
- ✓ Passwords are hashed
- ✓ Invalid credentials rejected
- ✓ Session management works
- ✓ Consent controls access
- ✓ Invite codes validate correctly

## Performance Checks

1. **Page Load Times**
   - All pages should load within 2 seconds
   - AI responses within 5 seconds

2. **Database Operations**
   - Saves should be instant
   - Queries should be fast

3. **UI Responsiveness**
   - Buttons should respond immediately
   - Forms should validate quickly

## Browser Compatibility

Test on:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Known Limitations

1. Chat history is session-based (not persisted)
2. Logo requires manual placement in assets/
3. Single language support (English)
4. No email verification
5. No password reset functionality

## Troubleshooting Common Issues

**Issue**: AI responses fail
- **Solution**: Check OpenAI API key in .env
- **Solution**: Verify API credits available

**Issue**: Database errors
- **Solution**: Delete her_healing_hands.db and restart

**Issue**: Import errors
- **Solution**: Run `pip install -r requirements.txt`

**Issue**: Styling issues
- **Solution**: Clear Streamlit cache: `streamlit cache clear`

## Success Criteria

All tests should pass with:
- ✓ No errors in console
- ✓ All features working as expected
- ✓ Privacy controls functioning
- ✓ AI responses appropriate
- ✓ Database operations successful
- ✓ UI displaying correctly
