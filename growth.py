import streamlit as st
import pandas as pd

import seaborn as sns

# Streamlit App
st.set_page_config(page_title="Pro Streamlit App", layout="wide")

st.title("📊 Pro-Level Streamlit Dashboard")

# Sidebar Input
st.sidebar.header("Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())

    # Numeric Columns Selection
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    selected_col = st.sidebar.selectbox("Select a column for analysis", numeric_cols)

    if selected_col:
        st.write(f"### Statistics for {selected_col}", df[selected_col].describe())

        # Histogram
        fig, ax = plt.subplots()
        sns.histplot(df[selected_col], kde=True, bins=30, ax=ax)
        st.pyplot(fig)

        # Box Plot
        fig, ax = plt.subplots()
        sns.boxplot(x=df[selected_col], ax=ax)
        st.pyplot(fig)

else:
    st.warning("Upload a CSV file to proceed.")
