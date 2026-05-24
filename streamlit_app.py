import os
import streamlit as st
import streamlit.components.v1 as components

# Define the absolute path to the folder containing your index.html, css, and js
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Create a custom component that serves the entire directory
render_my_frontend = components.declare_component("my_frontend", path=parent_dir)

# Render it
st.set_page_config(layout="wide")
render_my_frontend()
