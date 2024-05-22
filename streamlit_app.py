import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(page_title="QR Code Generator", page_icon="🔗", layout="centered")

# App title
st.title("QR Code Generator")

# Sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "About"],
                           icons=["house", "info-circle"], menu_icon="cast", default_index=0)

if selected == "Home":
    st.subheader("Enter URL to generate QR Code")

    # URL input
    url = st.text_input("URL", placeholder="Enter the URL here")

    # Button to generate QR code
    if st.button("Generate QR Code"):
        if url:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")

            # Convert PIL image to a format that can be displayed in Streamlit
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_str = buffered.getvalue()

            # Display the QR code
            st.image(img_str, caption="Generated QR Code", use_column_width=True)
        else:
            st.warning("Please enter a URL")

elif selected == "About":
    st.subheader("About")
    st.write("""
        Created By Ragunathan S - 
        Enter a URL to generate a QR Code.
        Happy Day.
    """)

# Footer
st.markdown("""
    <style>
        footer {
            visibility: hidden;
        }
        footer:after {
            content:'Created with Streamlit';
            visibility: visible;
            display: block;
            position: relative;
            color: #4CAF50;
            padding: 1rem;
            top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)
