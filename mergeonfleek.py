import streamlit as st
from pypdf import PdfWriter, PdfReader
from io import BytesIO

st.set_page_config(page_title="MergeOnFleek", page_icon="🦄")
st.title("🦄 MergeOnFleek")
st.caption("Put your PDFs together, lookin’ flawless.")

soft_pink_css = """
    <style>
    body {
        background-color: #ffe4ec !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: #ffe4ec !important;
    }
    [data-testid="stHeader"] {
        background-color: rgba(255, 228, 236, 0.0);
    }
    [data-testid="stSidebar"] {
        background-color: #ffe4ec !important;
    }
    </style>
"""
st.markdown(soft_pink_css, unsafe_allow_html=True)

uploaded_files = st.file_uploader(
    "Upload PDFs to merge (in order):",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("✨ Merge PDFs ✨"):
        writer = PdfWriter()
        for uploaded in uploaded_files:
            reader = PdfReader(uploaded)
            if reader.is_encrypted:
                try:
                    reader.decrypt("")
                except Exception:
                    st.error(f"File '{uploaded.name}' is encrypted and cannot be processed.")
                    continue
            for page in reader.pages:
                writer.add_page(page)
        output_pdf = BytesIO()
        writer.write(output_pdf)
        output_pdf.seek(0)
        st.success("Done! Download your flawless PDF below.")
        st.download_button(
            label="Download Merged PDF",
            data=output_pdf,
            file_name="merged_onfleek.pdf",
            mime="application/pdf"
        )
else:
    st.info("Upload two or more PDFs to get started!")
