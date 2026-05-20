import streamlit as st
from chatbot import search_bikes

st.title("🏍 Kawasaki Bike Chatbot")

user_input = st.text_input("Ask about Kawasaki bikes")

if user_input:

    results = search_bikes(user_input)

    if results:

        for bike in results:

            st.subheader(f"{bike['model']} ({bike['year']})")

            st.write(f"Engine: {bike['engine_cc']} cc")
            st.write(f"HP: {bike['hp']}")
            st.write(f"Torque: {bike['torque_nm']} Nm")
            st.write(f"Weight: {bike['weight_kg']} kg")
            st.write(f"Top Speed: {bike['top_speed_kmh']} km/h")
            st.write(f"Fuel Avg: {bike['fuel_avg_kmpl']} km/l")
            st.write(f"Gears: {bike['gears']}")
            st.write(f"Fuel Type: {bike['fuel_type']}")
            st.write(f"Price: ${bike['Price_usd']}")
            st.write(f"Color Options: {bike['Color']}")

    else:
        st.error("No matching bike found.")