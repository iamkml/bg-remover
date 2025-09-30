import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Background Remover", page_icon="🖼️", layout="centered")

st.title("🖼️ Background Remover")
st.write("Upload an image and remove its background instantly!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    input_image = Image.open(uploaded_file)
    
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
