# data-analysis
import pandas as pd
import streamlit as st

st.header("YouTube Hot Music 2025")
df = pd.read_csv("youtube-top-100-songs-2025.csv")

st.subheader("Youtube Top 100 songs 2025")
st.write(df['title'])
