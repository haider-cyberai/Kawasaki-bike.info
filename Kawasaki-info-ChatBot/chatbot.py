import pandas as pd

# Load dataset
df = pd.read_csv("data/Kawasaki_bikes.csv")

def search_bikes(user_query):
    query = user_query.lower()

    results = []

    for _, row in df.iterrows():

        bike_info = " ".join(map(str, row.values)).lower()

        if query in bike_info:
            results.append(row)

    return results