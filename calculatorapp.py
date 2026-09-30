from pathlib import Path
 
import streamlit as st
import streamlit.components.v1 as components
 
st.set_page_config(page_title="LoL Kalkulator", page_icon="⚔️", layout="wide")
 
# ukrywa menu i margines Streamlita, żeby było widać tylko kalkulator
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      .stApp {background: #0a0d13;}
    </style>
    """,
    unsafe_allow_html=True,
)
 
html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=2100, scrolling=True)
 
