import streamlit as st
from rembg import remove
from PIL import Image
import io

# --- Page Config ---
st.set_page_config(
    page_title="Background Remover",
    page_icon="🎨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS: Black & Golden Theme ---
st.markdown("""
<style>
/* Hide menu and footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Background & text */
body {
    background-color: #000000;
    color: gold;
    font-family: 'Arial', sans-serif;
}

/* App container */
.stApp {
    background-color: #0d0d0d;
    border-radius: 15px;
    padding: 25px;
}

/* Headings */
h1, h2, h3, h4 {
    color: gold;
    text-align: center;
}

/* Buttons */
.stButton>button {
    background-color: gold;
    color: black;
    height: 3em;
    width: 100%;
    border-radius: 10px;
    font-weight: bold;
    font-size: 16px;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #d4ac0d;
}

/* File uploader input text */
.stFileUploader>div>div>input {
    color: gold;
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🎨 Background Remover")
st.write("Upload an image and remove its background instantly!")

# --- File Uploader ---
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open uploaded image
    input_image = Image.open(uploaded_file)
    
    # Display original
    st.subheader("📥 Original Image")
    st.image(input_image, use_column_width=True)

    # Remove background
    with st.spinner("Removing background..."):
        output_image = remove(input_image)

    st.subheader("✅ Background Removed")
    st.image(output_image, use_column_width=True)

    # Convert to bytes for download
    img_bytes = io.BytesIO()
    output_image.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()

    st.download_button(
        label="📥 Download Transparent Image",
        data=img_bytes,
        file_name="output.png",
        mime="image/png"
    )
