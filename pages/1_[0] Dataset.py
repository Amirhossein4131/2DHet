import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

def load_dataset():
    return pd.read_csv("dataset/dataset.csv")

def show_dataset_page():
    st.title("📊 2D Materilas Dataset")


    df = load_dataset()

    # st.markdown("### 🔥 Interactive Table (AgGrid)")
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_pagination(enabled=True, paginationPageSize=20)
    gb.configure_default_column(resizable=True, sortable=True, filter=True, cellStyle={"textAlign": "center"})
    gb.configure_selection("single")
    grid_options = gb.build()

    AgGrid(
        df,
        gridOptions=grid_options,
        fit_columns_on_grid_load=True,
        theme="blue",  # light, dark, blue, material, fresh
        height=590
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

st.markdown("""
<div class='description'>
    The dataset comprises 1922 unique structures, 
    including 92,562 atoms, collected over 56 ps during the active learning workflow.
</div>
""", unsafe_allow_html=True)


if __name__ == "__main__":
    show_dataset_page()
