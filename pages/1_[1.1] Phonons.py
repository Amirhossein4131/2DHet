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
st.sidebar.markdown("### Select MLIPs to display")
all_labels = ["DFT","MACE OMAT SMALL"]
selected_labels = []
for label in all_labels:
    if st.sidebar.checkbox(label, value=True):
        selected_labels.append(label)

# --- Define materials and their YAML files ---

materials = {
    "Mono-layer WSe2": {
        "band_files": ["./phonon_data/1-WSe2/band-mono-vasp.yaml", "./phonon_data/1-WSe2/band-mono-omat-small.yaml"],
        "colors": ["black", "blue"],
        "labels": ["DFT", "MACE OMAT SMALL"]
    },
        "Mono-layer MoS2": {
        "band_files": ["./phonon_data/2-MoS2/band-mono-vasp.yaml", "./phonon_data/2-MoS2/band-mono-omat-small.yaml"],
        "colors": ["black", "blue"],
        "labels": ["DFT", "MACE OMAT SMALL"]
    },
        "Mono-layer MoSe2": {
        "band_files": ["./phonon_data/3-MoSe2/band-mono-vasp.yaml", "./phonon_data/3-MoSe2/band-mono-omat-small.yaml"],
        "colors": ["black", "blue"],
        "labels": ["DFT", "MACE OMAT SMALL"]
    },
        "Mono-layer MoTe2": {
        "band_files": ["./phonon_data/4-MoTe2/band-mono-vasp.yaml", "./phonon_data/4-MoTe2/band-mono-omat-small.yaml"],
        "colors": ["black", "blue"],
        "labels": ["DFT", "MACE OMAT SMALL"]
    },
        "Mono-layer WS2": {
        "band_files": ["./phonon_data/5-WS2/band-mono-vasp.yaml", "./phonon_data/5-WS2/band-mono-omat-small.yaml"],
        "colors": ["black", "blue"],
        "labels": ["DFT", "MACE OMAT SMALL"]
    },
        "Mono-layer WTe2": {
        "band_files": ["./phonon_data/6-WTe2/band-mono-vasp.yaml", "./phonon_data/6-WTe2/band-mono-omat-small.yaml"],
        "colors": ["black", "blue"],
        "labels": ["DFT", "MACE OMAT SMALL"]
    },
        "Mono-layer TaS2": {
        "band_files": ["./phonon_data/7-TaS2/band-mono-vasp.yaml", "./phonon_data/7-TaS2/band-mono-omat-small.yaml"],
        "colors": ["black", "blue"],
        "labels": ["DFT", "MACE OMAT SMALL"]
    }
}

# --- Expanders for each material ---
for material_name, data in materials.items():
    with st.expander(f"{material_name}", expanded=False):
        # Filter the datasets based on sidebar selection
        filtered_files = []
        filtered_colors = []
        filtered_labels = []
        for f, c, l in zip(data["band_files"], data["colors"], data["labels"]):
            if l in selected_labels:
                filtered_files.append(f)
                filtered_colors.append(c)
                filtered_labels.append(l)

        if filtered_files:
            fig = create_phonon_figure(
                band_files=filtered_files,
                colors=filtered_colors,
                labels=filtered_labels
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Please select at least one dataset to display.")
