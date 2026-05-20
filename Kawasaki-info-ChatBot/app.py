import streamlit as st
import pandas as pd
import os
from chatbot import search_bikes

# ---- SAFE PATH (WORKS ON STREAMLIT CLOUD) ----
BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "data", "kawasaki_bikes.csv")

df = pd.read_csv(CSV_PATH)

# ---- UI ----
st.set_page_config(page_title="Kawasaki Showroom", layout="wide")

st.title("🏍 Kawasaki AI Bike Showroom")

user_input = st.text_input("Search or Compare bikes (e.g. Ninja vs R1)")

# ---- SEARCH / COMPARE LOGIC ----
if user_input:

    query = user_input.lower()

    # 🆚 COMPARE MODE
    if "vs" in query:

        bike1, bike2 = query.split("vs")

        bike1 = bike1.strip()
        bike2 = bike2.strip()

        b1 = df[df["model"].str.lower().str.contains(bike1)]
        b2 = df[df["model"].str.lower().str.contains(bike2)]

        if not b1.empty and not b2.empty:

            compare_df = df[df["model"].isin(
                [b1.iloc[0]["model"], b2.iloc[0]["model"]]
            )]

            st.subheader("🆚 Comparison Result")
            st.dataframe(compare_df.set_index("model"), use_container_width=True)

        else:
            st.error("One or both bikes not found")

    # 🔍 NORMAL SEARCH
    else:
        results = search_bikes(user_input)

        st.subheader("🔍 Search Results")
        st.dataframe(results, use_container_width=True)

# ---- FULL TABLE (OPTIONAL VIEW) ----
st.subheader("📊 Full Bike Database")
st.dataframe(df, use_container_width=True)
