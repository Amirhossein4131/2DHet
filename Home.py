# main.py
import streamlit as st

st.set_page_config(
    page_title="2D Heterostructures Explorer",
    page_icon="🧪",
    layout="wide",
)

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        .big-title {
            font-size: 72px;
            font-weight: 900;
            text-align: center;
            color: #2E86C1;
            margin-top: 40px;
        }
        .description {
            font-size: 20px;
            text-align: center;
            color: #333333;
            margin-top: 20px;
            margin-left: auto;
            margin-right: auto;
            max-width: 800px;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

# --- Main content ---
st.markdown("<div class='big-title'>2D Heterostructures Explorer</div>", unsafe_allow_html=True)

st.markdown("""
<div class='description'>
Machine Learning Interatomic Potentials (MLIPs) and Machine Learning Tight-Binding (MLTB) 
approaches are transforming the way we model and predict the properties of 2D materials 
and their heterostructures. By combining quantum accuracy with computational efficiency, 
these tools enable large-scale simulations of complex layered systems, accelerating the 
design and discovery of next-generation materials for electronics, catalysis, and energy storage.
</div>
""", unsafe_allow_html=True)
