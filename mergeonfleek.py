import streamlit as st
from pypdf import PdfWriter, PdfReader

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
            for page in reader.pages:
                writer.add_page(page)
        output_pdf = "merged_onfleek.pdf"
        with open(output_pdf, "wb") as fout:
            writer.write(fout)
        with open(output_pdf, "rb") as fout:
            st.success("Done! Download your flawless PDF below.")
            st.download_button(
                label="Download Merged PDF",
                data=fout,
                file_name="merged_onfleek.pdf",
                mime="application/pdf"
            )
else:
    st.info("Upload two or more PDFs to get started!")
