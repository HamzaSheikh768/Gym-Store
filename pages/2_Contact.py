import streamlit as st

# ------------- Page configuration -----------------
st.set_page_config(
    page_title="Gym Store | Contact", 
    page_icon="📞", 
    layout="centered"
)

# ---------- Custom Style ----------
st.markdown("""
    <style>
        .subtitle { 
            font-size: 1.3rem; 
            color: gray; /*  gray color */
            margin-bottom: 2rem;
        }
        .footer { 
            text-align: center; 
            font-size: 0.9rem; 
            color: gray; /* Gray color */
            margin-top: 3rem; 
        }
    </style>
""", unsafe_allow_html=True)

st.title("📞 Contact Us")
st.markdown("<div class='subtitle'>Reach out with any questions or feedback.</div>", unsafe_allow_html=True)

# ------------ Contact Form -----------------
with st.form("contact_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send Message")

# ---------- Form submission handling --------------
if submitted:
    st.success(f"✅ Thank you, {name}! Your message has been sent successfully.")

st.markdown("---")
st.markdown("📍 **Address:** 123 Gym Store Street, Karachi, Pakistan")  
st.markdown("📧 **Email:** official@gymstore.com")  
st.markdown("📞 **Phone:** +92 300 1234567")  

# ---------- Footer ----------
st.markdown("""
    <div class='footer'>© 2025 Gym Store | Designed with 🏋️‍♂️ by <b>Sheikh Hamza</b></div>
""", unsafe_allow_html=True)