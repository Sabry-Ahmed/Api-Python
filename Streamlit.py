import streamlit as st
import numpy as np
import pandas as pd

def load_data():
    data = pd.read_csv("international_matches.csv")
    return data

st.title("International matches")

if st.checkbox("Show data"):
    st.subheader("H3hitema")
    st.write(load_data())


#/Users/joker/Library/Python/3.9/bin/streamlit hello            

