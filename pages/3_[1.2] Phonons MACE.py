import streamlit as st
from utils.plot_phonon import create_phonon_figure


# --- Custom CSS for expanders ---
st.markdown("""
    <style>
        .big-title {
            font-size: 30px;
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



st.set_page_config(
    page_title="Phonons | 2D Heterostructures Explorer",
    page_icon="🎵",
    layout="wide",
)

# --- Page title ---
st.markdown("""
    <h1 style='text-align: center; font-size: 64px; color: #2E86C1;'>Phonons</h1>
""", unsafe_allow_html=True)

# --- Sidebar: select datasets (applied to all materials) ---
# st.sidebar.markdown("### Select MLIPs to display")
# all_labels = ["DFT","MACE OMAT SMALL", "MACE OMAT SMALL FT"]
# selected_labels = []
# for label in all_labels:
#     if st.sidebar.checkbox(label, value=True):
#         selected_labels.append(label)

# --- Define materials and their YAML files ---

materials = {
    "Mono-layer WSe2": "./phonon_figs/mono/phonon_WSe2_mono.png",
    "Mono-layer MoS2": "./phonon_figs/mono/phonon_MoS2_mono.png",
    "Mono-layer MoSe2": "./phonon_figs/mono/phonon_MoSe2_mono.png",
    "Mono-layer MoTe2": "./phonon_figs/mono/phonon_MoTe2_mono.png",
    "Mono-layer WS2": "./phonon_figs/mono/phonon_WS2_mono.png",
    "Mono-layer WTe2": "./phonon_figs/mono/phonon_WTe2_mono.png",
    "Bi-layer AB0 WSe2": "./phonon_figs/bi/phonon_WSe2_bi_AB0.png",
    "Bi-layer AB0 MoS2": "./phonon_figs/bi/phonon_MoS2_bi_AB0.png",
    "Bi-layer AB0 MoSe2": "./phonon_figs/bi/phonon_MoSe2_bi_AB0.png",
    "Bi-layer AB0 MoTe2": "./phonon_figs/bi/phonon_MoTe2_bi_AB0.png",
    "Bi-layer AB0 WS2": "./phonon_figs/bi/phonon_WS2_bi_AB0.png",
    "Bi-layer AB0 WTe2": "./phonon_figs/bi/phonon_WTe2_bi_AB0.png",
}


for material_name, png_path in materials.items():
    with st.expander(material_name, expanded=False):

        st.image(png_path, caption=material_name, use_container_width=True)
