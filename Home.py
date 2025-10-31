import streamlit as st

# ------------------- Page configuration -------------------
st.set_page_config(
    page_title="Gym Store",
    page_icon="🏋️‍♂️",
    layout="wide"
)

# ---------- Custom Style Home, Products ----------
st.markdown("""
    <style>
        .main { 
            background-color: #f8f9fa; /* Light gray background */
            padding: 2rem; 
            margin: 0 auto;
            }
        .title { 
            font-size: 3rem; 
            font-weight: 800; 
            color: #1e3d59; /* Dark blue color */
            text-align: center; 
            margin-bottom: 0.3rem; 
        }
        .subtitle { 
            font-size: 1.3rem; 
            color: #444; /* Moderate dark gray color */
            text-align: center; /* Centered text */
            margin-bottom: 2rem; 
        }
        .paragraph { 
            font-size: 1.1rem; 
            color: white; /* White color */
            text-align: justify; /* Justified text */
            line-height: 1.7; 
        }   
        .footer { 
            text-align: center; 
            font-size: 0.9rem; 
            color: gray; /* Gray color */
            margin-top: 3rem; 
        }
        .stImage img { 
            border-radius: 15px; 
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("<div class='title'>🏋️‍♂️ Gym Store</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Premium Fitness Accessories, Supplements & Protein</div>", unsafe_allow_html=True)

# ---------- Hero Section ----------
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
        <p class='paragraph'>
        Welcome to <b>Gym Store</b> — your trusted destination for quality gym equipment, nutrition, and accessories.  
        Whether you're training at home or the gym, we provide the tools to help you stay fit, strong, and motivated.  
        Explore our curated products and exclusive offers designed to elevate your fitness experience.
        </p>
        <p>Trendy. Comfortable. Affordable.</p>
    """, unsafe_allow_html=True)

with col2:
     st.image("assets/claudio-schwarz-x67Pxo51O5I-unsplash.jpg")
# ---------- Featured Categories ----------
st.title("🏆 Featured Categories")
col3, col4, col5 = st.columns(3)
with col3:
    st.image("assets/sati-yqc77vmpNaM-unsplash.jpg")
    st.caption("💪 Fitness Equipment")
with col4:
    st.image("assets/aleksander-saks-_a6dW14spss-unsplash.jpg")
    st.caption("🥗 Nutrition & Supplements")
with col5:
    st.image("assets/aleksander-saks-JUVMefHzC6U-unsplash.jpg")
    st.caption("👕 Gym Accessories")

# ---------- Footer ----------
st.markdown("""
    <div class='footer'>© 2025 Gym Store | Designed with 🏋️‍♂️ by <b>Sheikh Hamza</b></div>
""", unsafe_allow_html=True)
