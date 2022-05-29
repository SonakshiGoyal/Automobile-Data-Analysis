import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def app(automobileData):
    html_temp = """
    <div style="background-color:#8A2BE2 ;padding:10px">
    <h3 style="color:white;text-align:center;">Dataset after Cleaning </h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.dataframe(data=automobileData,width=1500,height=1000)