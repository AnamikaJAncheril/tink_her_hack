# 🚀 Groq API Setup Guide - FREE & FAST!

## Why Groq?

- ✅ **Completely FREE** - No credit card required
- ✅ **SUPER FAST** - 10x faster than other APIs
- ✅ **High quality** - Uses Llama 3 model
- ✅ **Easy setup** - Just 3 steps
- ✅ **Generous limits** - 30 requests/minute free tier

---

## 🎯 Quick Setup (3 Steps)

### Step 1: Get Your FREE API Key

1. Go to: **https://console.groq.com/keys**
2. Sign in (or create account with Google/GitHub)
3. Click **"Create API Key"**
4. Give it a name (e.g., "Her Healing Hands")
5. Copy the key (starts with `gsk_...`)

**That's it! No credit card needed!**

---

### Step 2: Add Key to .env File

Open your `.env` file:
```cmd
notepad .env
```

Delete everything and add:
```
GROQ_API_KEY=gsk_...your-key-here
```

Save and close (Ctrl+S).

---

### Step 3: Install Groq Package

```cmd
pip install groq
```

---

## ✅ Test Your Setup

```cmd
python test_api.py
```

You should see:
```
✓ API key found: gsk_...
Testing API connection...
✓ API connection successful!
```

---

## 🎯 Run the App

```cmd
streamlit run app.py
```

---

## 🆚 Groq vs Others

| Feature | Groq | OpenAI | Gemini |
|---------|------|--------|--------|
| **Cost** | FREE | Paid | FREE |
| **Speed** | 10x faster | Normal | Normal |
| **Credit Card** | Not required | Required | Not required |
| **Free Tier** | 30 req/min | None | 60 req/min |
| **Quality** | Excellent | Excellent | Excellent |

---

## 📊 What You Get FREE

**Free Tier Limits:**
- 30 requests per minute
- 14,400 requests per day
- Unlimited for personal use

**For this app, that means:**
- ✅ Unlimited chat messages
- ✅ Unlimited assessments
- ✅ Unlimited partner guidance
- ✅ Perfect for production use

---

## 🔧 Troubleshooting

### Issue: "API key not found"
**Solution:**
```cmd
notepad .env
```
Make sure it says:
```
GROQ_API_KEY=gsk_...
```

### Issue: "Module not found"
**Solution:**
```cmd
pip install groq
```

### Issue: "API connection failed"
**Possible causes:**
1. Check you copied the entire key
2. Verify key is active at https://console.groq.com/keys
3. Wait 1-2 minutes after creating key

---

## 📝 Complete Setup Commands

```cmd
# 1. Install Groq package
pip install groq

# 2. Create .env file
notepad .env
# Add: GROQ_API_KEY=your-key-here
# Save and close

# 3. Test API
python test_api.py

# 4. Run app
streamlit run app.py
```

---

## 🎉 Benefits of Groq

1. **Lightning Fast** - Responses in <1 second
2. **No Cost** - Completely free forever
3. **No Billing** - Never asks for credit card
4. **Reliable** - 99.9% uptime
5. **Easy** - Simple setup

---

## 🔗 Useful Links

- **Get API Key:** https://console.groq.com/keys
- **Documentation:** https://console.groq.com/docs
- **Playground:** https://console.groq.com/playground

---

## ✅ Checklist

- [ ] Got API key from Groq Console
- [ ] Added key to `.env` file
- [ ] Installed `groq` package
- [ ] Ran `python test_api.py` successfully
- [ ] Ready to run `streamlit run app.py`

---

## 💡 Pro Tips

1. **Keep your API key private** - Don't share it
2. **Free tier is generous** - Perfect for this app
3. **Super fast responses** - Users will love it
4. **Multiple projects** - Can create multiple keys
5. **Monitor usage** - Check at https://console.groq.com

---

## 🚀 Ready to Go!

Your app now uses Groq - FREE and FAST!

```cmd
streamlit run app.py
```

Enjoy! 🌸
