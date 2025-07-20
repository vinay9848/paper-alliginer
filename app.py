# app.py

import streamlit as st
import os
from aligner import align_question_paper
from utils import extract_text_from_pdf, save_as_docx

st.set_page_config(page_title="Hindi Question Aligner", layout="centered")

st.title("📄 Hindi Question Paper Auto-Aligner")

uploaded_file = st.file_uploader("Upload Non-Aligned Question Paper (PDF)", type=["pdf"])

if uploaded_file:
    with open("input.pdf", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("🔍 Extracting text from PDF..."):
        raw_text = extract_text_from_pdf("input.pdf")

    st.subheader("📄 Raw Extracted Text")
    st.text_area("Non-Aligned Text", raw_text, height=300)

    aligned_text = align_question_paper(raw_text)

    st.subheader("✅ AI Aligned Question Paper")
    st.text_area("Aligned Text", aligned_text, height=300)

    docx_path = "aligned_output.docx"
    save_as_docx(aligned_text, docx_path)

    with open(docx_path, "rb") as f:
        st.download_button("⬇ Download DOCX", f, file_name="aligned_paper.docx")

    # Optional: Create PDF for download if needed
    st.info("PDF download coming soon (Streamlit + PDF packages)")
