import streamlit as st
from rembg import remove
from PIL import Image
import io

# --- Page Config ---
st.set_page_config(
    page_title="Background Remover",
    page_icon="🌲",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS: Black & Golden Transparent Glass Forest ---
st.markdown("""
<style>
/* Hide menu and footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Background & text */
body {
    background: linear-gradient(to bottom right, #0a0a0a, #1a1a1a);
    color: gold;
    font-family: 'Arial', sans-serif;
}

/* Glassy app container */
.stApp {
    background: rgba(0,0,0,0.5);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 0 30px rgba(255,215,0,0.3);
}

/* Headings */
h1, h2, h3, h4 {
    color: gold;
    text-align: center;
    text-shadow: 0 0 8px rgba(255,215,0,0.6);
}

/* Buttons */
.stButton>button {
    background-color: rgba(255,215,0,0.9);
    color: #0a0a0a;
    height: 3em;
    width: 100%;
    border-radius: 12px;
    font-weight: bold;
    font-size: 16px;
    transition: 0.3s;
    box-shadow: 0 0 15px rgba(255,215,0,0.5);
}

.stButton>button:hover {
    background-color: rgba(255,215,0,1);
}

/* File uploader input text */
.stFileUploader>div>div>input {
    color: gold;
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🌲 Background Remover")
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
