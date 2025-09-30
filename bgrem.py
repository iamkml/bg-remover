import streamlit as st
from rembg import remove
from PIL import Image
import io

# --- Page Config ---
st.set_page_config(
    page_title="Background Remover",
    page_icon="🖼️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Dark Night Theme CSS ---
st.markdown("""
<style>
body {
    background-color: #0a0a0a;
    color: #f1c40f;
    font-family: 'Arial', sans-serif;
}

.stApp {
    background-color: #121212;
    border-radius: 15px;
    padding: 25px;
}

h1, h2, h3, h4 {
    color: #f1c40f;
    text-align: center;
}

.stButton>button {
    background-color: #f1c40f;
    color: #0a0a0a;
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

.stFileUploader>div>div>input {
    color: #f1c40f;
}
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("🌌 Background Remover")
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

# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    st.write("Dark Night Theme 🌓")
    st.write("Made with Streamlit & rembg.")
