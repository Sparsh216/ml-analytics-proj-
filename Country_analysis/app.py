import streamlit as st
import pandas as pd
import helper

df=pd.read_csv("country_profile_variables.csv")
user_menu=st.sidebar.radio(
    "Select an option",
    (
        'Region-Analysis',
        'Country-Wise Analysis',
        'Global-Analysis',
        'GDP-Analysis'
    )
)


if user_menu == "Region-Analysis":
    re=helper.regionAna(df)
    st.dataframe(re)