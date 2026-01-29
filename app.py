import streamlit as st
from PIL import Image
import os
import matplotlib.pyplot as plt

from infer import get_invoice_data

st.set_page_config(page_title="Invoice OCR", layout="centered")

st.title("🧾 Invoice OCR & Tax Visualization")

uploaded_file = st.file_uploader(
    "Upload the invoice image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:
    # -------- Show image --------
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_container_width=True)

    # -------- Save image --------
    save_dir = "uploaded_images"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, uploaded_file.name)
    image.save(save_path)

    # -------- OCR Extraction --------
    with st.spinner("Extracting invoice data..."):
        invoice_data = get_invoice_data(save_path)

    st.success("Analysis completed ✅")

    # -------- Show extracted data --------
    st.subheader("Extracted Invoice Data")
    st.json(invoice_data.model_dump())

    # -------- Bar Plot --------
    st.subheader("Tax Amount per Item")

    if invoice_data.items:
        items = [item.description for item in invoice_data.items]
        taxes = [item.taxes for item in invoice_data.items]

        fig, ax = plt.subplots()
        ax.bar(items, taxes)
        ax.set_xlabel("Item")
        ax.set_ylabel("Tax Amount")
        ax.set_title("Tax Amount per Invoice Item")

        st.pyplot(fig)
    else:
        st.warning("No items found in the invoice.")
