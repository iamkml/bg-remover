import streamlit as st
from rembg import remove
from PIL import Image
import io

# --- Page Config ---
st.set_page_config(
    page_title="Background Remover",
    page_icon="🎨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Glassy Golden-Black Theme ---
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #1a1a1a, #0d0d0d);
    color: gold;
}
.stApp {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 20px;
    padding: 20px;
}
h1, h2, h3, h4 {
    color: gold;
    text-align: center;
}
.stButton>button {
    background-color: gold;
    color: black;
    height: 3em;
    width: 100%;
    border-radius: 10px;
    font-weight: bold;
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

# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    st.write("This is a simple background remover app.")
    st.write("Made with Streamlit and rembg.")
