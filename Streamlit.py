import streamlit as st
import numpy as np
import pandas as pd

def load_data():
    data = pd.read_csv("international_matches.csv")
    return data

st.title("H3HITEMA")

if st.checkbox("Afficher les données"):
    st.subheader("See Matches")
    st.write(load_data())


#/Users/joker/Library/Python/3.9/bin/streamlit hello            

