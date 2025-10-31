import streamlit as st

# ------------------- Page configuration -------------------
st.set_page_config(
    page_title="Gym Store | Products", 
    page_icon="💪", 
    layout="wide")

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

# Product Showcase
st.title("💪 Our Products")
st.markdown("<div class='subtitle'> Choose from our best-selling fitness essentials!</div>", unsafe_allow_html=True)

# ----------------- Display products in columns -----------------
cols = st.columns(2)
products = {
    "Dumbells":[
    {"name": "Dumbell Weight 16kg", "image": "assets/dumbell.jpeg","price": "$60.99"},
    {"name": "Dumbell Weight 12kg", "image": "assets/dumbell-1.jpeg","price": "$25.99"},
    {"name": "Dumbell Weight 14kg", "image": "assets/dumbell-5.jpeg","price": "$53.99"},
    {"name": "Dumbell Weight 20kg", "image": "assets/dumbell-2.jpeg","price": "$75.99"},
    {"name": "Dumbell Weight 42kg", "image": "assets/dumbell-4.jpeg","price": "$119.99"},
    {"name": "Dumbell Complete Sets", "image": "assets/dumbell-6.jpeg","price": "$200.99"},
    ],

    "Machines": [   
    {"name": "Cardio Complete Machines", "image": "assets/cardio-1.jpeg","price": "$59.99"},
    {"name": "Cardio Cycle", "image": "assets/cardio-2.jpeg","price": "$69.99"},
    {"name": "Cardio Running", "image": "assets/cardio-3.jpeg","price": "$80.99"},
    ],

    "Protein Supplements":[
    {"name": "Protein Powder", "image": "assets/protein1.jpeg","price": "$29.99"},
    {"name": "Protein Bar", "image": "assets/protein2.jpeg","price": "$19.99"},
    {"name": "Protein Shake", "image": "assets/protein3.jpeg","price": "$10.99"},
    {"name": "Protein Cookies", "image": "assets/protein4.jpeg","price": "$18.99"},
    ],

}

# Sidebar for product categories
st.sidebar.title("Product Categories")
category = st.sidebar.selectbox("Select a category:", list(products.keys()))
# selected_products = products[category]
# products = [(prod["name"], prod["image"], prod["price"])]

if category:
        selected_products = products[category]
        st.write(f"*Showing {category}*")
        st.markdown("---")

cols = st.columns(2)
# ----------------- Iterate through products and display them ---------------
for i, Product in enumerate(selected_products):
    with cols[i % 2]:
# Online image with fixed width for uniform size
        st.image(Product["image"], width=230, caption=Product["name"])  # width=230 for square uniform size

# st.markdown(f"### {clothing['name']}")
        st.markdown(f"${Product['price']}")
        st.button(f"Add to Cart 🛒", key=Product["name"])
        st.markdown("---")

# ------------------- Footer -------------------
st.markdown("""
    <div class='footer'>© 2025 Gym Store | Designed with 🏋️‍♂️ by <b>Sheikh Hamza</b></div>
""", unsafe_allow_html=True)        