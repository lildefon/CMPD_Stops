import streamlit as st 
import pandas as pd 

st.write('CMPD Traffic Stops')

@st.cache_data 
def load_data(csv):
    df=pd.read_csv(csv)
    return df




stops = pd.read_csv('Data/Officer_Traffic_Stops.csv')

st.dataframe(stops)

st.write('hi this is prathap')
st.header("Hii")