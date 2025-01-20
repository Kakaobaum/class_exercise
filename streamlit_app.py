import streamlit as st
import os


# --- deploying readme on streamlit ---
# Path to the README.md file
readme_file = "README.md"

# Read and render the README content
if os.path.exists(readme_file):
    with open(readme_file, "r", encoding="utf-8") as file:
        readme_content = file.read()
    st.markdown(readme_content, unsafe_allow_html=True)
else:
    st.error("README.md file not found!")
# --- deploying readme on streamlit ---
