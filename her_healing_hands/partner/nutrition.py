import streamlit as st

def show_nutrition_page():
    """Display nutrition information for postpartum mothers."""
    st.title("Postpartum Nutrition 🍲")
    
    st.write("Proper nutrition is crucial for postpartum recovery and breastfeeding. Here's how you can support your partner's nutritional needs.")
    
    st.markdown("---")
    
    # Why Nutrition Matters
    with st.expander("🌟 Why Nutrition Matters", expanded=True):
        st.markdown("""
        **Postpartum Recovery:**
        - Helps heal the body after childbirth
        - Restores nutrient stores depleted during pregnancy
        - Supports energy levels and reduces fatigue
        - Aids in hormonal balance
        
        **For Breastfeeding:**
        - Provides nutrients for breast milk production
        - Maintains mother's health while nursing
        - Supports baby's growth and development
        
        **Mental Health:**
        - Proper nutrition supports mood regulation
        - Helps combat postpartum depression
        - Improves energy and cognitive function
        """)
    
    # Key Nutrients
    with st.expander("🥗 Essential Nutrients"):
        st.markdown("""
        **Protein:**
        - Lean meats, fish, eggs, beans, lentils
        - Helps tissue repair and milk production
        - Aim for protein at every meal
        
        **Iron:**
        - Red meat, spinach, fortified cereals
        - Replenishes blood loss during delivery
        - Prevents anemia and fatigue
        
        **Calcium:**
        - Dairy products, leafy greens, fortified foods
        - Supports bone health
        - Important for breastfeeding mothers
        
        **Omega-3 Fatty Acids:**
        - Fatty fish (salmon, sardines), walnuts, flaxseeds
        - Supports brain health and mood
        - Important for baby's development
        
        **Vitamin D:**
        - Sunlight, fortified milk, fatty fish
        - Supports immune system and bone health
        - Often deficient postpartum
        
        **B Vitamins:**
        - Whole grains, eggs, leafy greens
        - Supports energy production
        - Important for nervous system
        
        **Fiber:**
        - Fruits, vegetables, whole grains
        - Prevents constipation
        - Supports digestive health
        """)
    
    # Meal Ideas
    with st.expander("🍽️ Meal Ideas"):
        st.markdown("""
        **Breakfast:**
        - Oatmeal with berries and nuts
        - Greek yogurt with granola and fruit
        - Scrambled eggs with whole grain toast and avocado
        - Smoothie with spinach, banana, and protein powder
        
        **Lunch:**
        - Quinoa bowl with grilled chicken and vegetables
        - Lentil soup with whole grain bread
        - Salmon salad with mixed greens
        - Turkey and avocado wrap
        
        **Dinner:**
        - Baked fish with roasted vegetables and brown rice
        - Chicken stir-fry with lots of vegetables
        - Beef and vegetable stew
        - Pasta with lean meat sauce and side salad
        
        **Snacks:**
        - Nuts and dried fruit
        - Hummus with vegetables
        - Cheese and whole grain crackers
        - Hard-boiled eggs
        - Fresh fruit with nut butter
        """)
    
    # Hydration
    with st.expander("💧 Hydration"):
        st.markdown("""
        **Why It's Important:**
        - Essential for milk production
        - Prevents dehydration and fatigue
        - Supports overall health
        
        **How Much:**
        - Aim for 8-10 glasses of water daily
        - More if breastfeeding
        - Drink when thirsty
        
        **Tips:**
        - Keep water bottle nearby at all times
        - Drink a glass with each feeding session
        - Limit caffeine and sugary drinks
        - Herbal teas count toward hydration
        """)
    
    # How Partners Can Help
    with st.expander("🤝 How You Can Help"):
        st.markdown("""
        **Meal Preparation:**
        - Cook nutritious meals
        - Prepare healthy snacks in advance
        - Keep easy-to-eat foods accessible
        
        **Grocery Shopping:**
        - Stock the kitchen with healthy options
        - Buy pre-cut vegetables and fruits
        - Get easy-to-prepare protein sources
        
        **Reminders:**
        - Remind her to eat regularly
        - Bring her snacks during feeding times
        - Keep water within reach
        
        **Make It Easy:**
        - Prepare one-handed snacks
        - Use meal delivery services if needed
        - Accept help from family and friends
        - Batch cook and freeze meals
        """)
    
    # Foods to Limit
    with st.expander("⚠️ Foods to Limit or Avoid"):
        st.markdown("""
        **If Breastfeeding:**
        - Limit caffeine (1-2 cups coffee per day)
        - Avoid alcohol or wait 2-3 hours after drinking
        - Watch for foods that may upset baby (dairy, spicy foods)
        - Limit processed and high-sugar foods
        
        **For Everyone:**
        - Minimize junk food and empty calories
        - Limit high-mercury fish
        - Avoid excessive caffeine
        - Reduce processed foods
        """)
    
    st.markdown("---")
    st.info("💡 Every mother's nutritional needs are different. Consult with a healthcare provider or nutritionist for personalized advice.")
