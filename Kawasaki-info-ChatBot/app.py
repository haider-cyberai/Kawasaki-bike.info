import streamlit as st
import pandas as pd

import os
st.write(os.listdir())
st.write(os.listdir("data"))

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "data", "kawasaki_bikes.csv")

df = pd.read_csv(CSV_PATH)

st.title("🏍 Kawasaki AI Bike Chatbot")

user_input = st.text_input("Search bikes")

if user_input:

    query = user_input.lower()

    #COMPARE MODE
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

            st.dataframe(compare_df.set_index("model"))

        else:
            st.error("One or both bikes not found")
    query = user_input.lower()

    #FILTERS
    if "fastest" in query:
        df = df.sort_values("top_speed_kmh", ascending=False)

    elif "cheapest" in query:
        df = df.sort_values("Price_usd", ascending=True)

    elif "highest hp" in query:
        df = df.sort_values("hp", ascending=False)

    elif "lightest" in query:
        df = df.sort_values("weight_kg", ascending=True)

    # 📊 SHOW RESULT
    st.dataframe(df)
