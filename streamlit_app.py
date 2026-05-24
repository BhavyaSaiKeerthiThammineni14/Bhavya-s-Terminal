import streamlit as st
import streamlit.components.v1 as components

# Set the page to wide mode to give your HTML room to breathe
st.set_page_config(layout="wide")

# Read your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Render the HTML in Streamlit
# You can adjust height and width as needed
components.html(html_code, height=800, scrolling=True)
