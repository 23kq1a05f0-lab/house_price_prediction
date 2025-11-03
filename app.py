import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# ------------------------------------------------------
# 🌆 Page Configuration
# ------------------------------------------------------
st.set_page_config(
    page_title="🏡 AI House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------
# 💅 Custom CSS for Modern Aesthetic
# ------------------------------------------------------
st.markdown("""
<style>
/* Background Gradient */
body {
    background: linear-gradient(135deg, #d9a7c7 0%, #fffcdc 100%);
    font-family: 'Poppins', sans-serif;
}

/* Main container glass effect */
.main {
    background: rgba(255, 255, 255, 0.8);
    padding: 3rem;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(12px);
}

/* Header */
h1 {
    text-align: center;
    color: #2c3e50;
    font-weight: 700;
    margin-bottom: 1rem;
}

/* Description text */
h3, p {
    text-align: center;
    color: #555;
}

/* Input labels */
label, .stSelectbox label {
    font-weight: 600 !important;
    color: #333 !important;
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #ff416c, #ff4b2b);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    transform: scale(1.03);
}

/* Result Card */
.result-card {
    text-align: center;
    padding: 2rem;
    background: rgba(255,255,255,0.75);
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    animation: fadeIn 1s ease-in-out;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------
# 📂 Load and Train Model
# ------------------------------------------------------
df = pd.read_csv("house_data.csv")
le = LabelEncoder()
df['City'] = le.fit_transform(df['City'])

X = df[['Sqft', 'Bedrooms', 'Bathrooms', 'City']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------------------------------
# 🧠 Sidebar - Dataset Insights
# ------------------------------------------------------
st.sidebar.title("📊 City Insights")
avg_price = df.groupby('City')['Price'].mean().reset_index()
avg_price['City'] = le.inverse_transform(avg_price['City'])
for i, row in avg_price.iterrows():
    st.sidebar.write(f"🏙 **{row['City']}** — ₹{row['Price']:,.0f}")

st.sidebar.markdown("---")
st.sidebar.caption("Data-driven insights powered by AI 🧠")

# ------------------------------------------------------
# 🏠 Main App Layout
# ------------------------------------------------------
st.title("🏡 AI-Powered House Price Prediction (2025 Edition)")
st.markdown("""
### 🌟 Experience the Future of Real Estate Valuation  
Enter your property details below and get **instant, AI-driven price estimation** for your home!
""")

# Two-column input layout
col1, col2 = st.columns(2)
with col1:
    sqft = st.number_input("📏 Area (Sqft):", min_value=500, max_value=5000, step=50)
    bedrooms = st.number_input("🛏 Bedrooms:", min_value=1, max_value=10, step=1)
with col2:
    bathrooms = st.number_input("🚿 Bathrooms:", min_value=1, max_value=10, step=1)
    city = st.selectbox("🏙 Select City:", le.classes_)

# Predict Button
predict_btn = st.button("🔮 Predict House Price")

# ------------------------------------------------------
# 🎯 Prediction Result
# ------------------------------------------------------
if predict_btn:
    city_code = le.transform([city])[0]
    input_data = pd.DataFrame([[sqft, bedrooms, bathrooms, city_code]],
                              columns=['Sqft', 'Bedrooms', 'Bathrooms', 'City'])
    predicted_price = model.predict(input_data)[0]

    st.markdown("---")
    st.markdown(
        f"""
        <div class="result-card">
            <h2>💰 Estimated House Price</h2>
            <h1 style="color:#0072ff;">₹{predicted_price:,.2f}</h1>
            <p>📍 City: <b>{city}</b></p>
            <p>🏠 Configuration: {bedrooms} BHK | {bathrooms} Bath | {sqft} Sqft</p>
        </div>
        """,
        unsafe_allow_html=True
    )
