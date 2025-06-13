import streamlit as st
from PIL import Image
from rembg import remove
import io

def main():
    st.title("🖼️ Background Remover Web App")
    st.write("Upload an image and remove its background using AI!")

    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Load image
        original_image = Image.open(uploaded_file).convert("RGBA")
        st.subheader("📌 Original Image")
        st.image(original_image, use_column_width=True)

        if st.button("Remove Background"):
            with st.spinner("Removing background..."):
                img_bytes = io.BytesIO()
                original_image.save(img_bytes, format="PNG")
                result_bytes = remove(img_bytes.getvalue())
                result_image = Image.open(io.BytesIO(result_bytes)).convert("RGBA")

                st.subheader("✅ Result Image (Background Removed)")
                st.image(result_image, use_column_width=True)

                # Download link
                st.download_button(
                    label="💾 Download Image",
                    data=result_bytes,
                    file_name="no_background.png",
                    mime="image/png"
                )

if __name__ == "__main__":
    main()
