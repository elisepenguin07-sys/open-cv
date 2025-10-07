import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header("Post-COVID Conditions")
df = pd.read_csv("Post-COVID_Conditions.csv")

st.subheader("Missing Data")
st.write("To understand which data are harder to collect, we will first identify the most challenging ones.")
