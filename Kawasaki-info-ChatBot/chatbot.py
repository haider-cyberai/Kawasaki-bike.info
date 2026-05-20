from difflib import get_close_matches
import pandas as pd
df = pd.read_csv("data/kawasaki_bikes.csv")
def search_bikes(user_query):


    query = user_query.lower()
    results = df.copy()

    # fuzzy model match
    models = df["model"].str.lower().tolist()
    match = get_close_matches(query, models, n=1, cutoff=0.4)

    if match:
        results = df[df["model"].str.lower() == match[0]]

    return results
