import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def prediction(disp,cap,width,mlg,automobileData):
    new_data = automobileData[['Displacement(in cc)', 'Fuel_Tank_Capacity (in litres)', 'Width(in mm)', 'ARAI_Certified_Mileage (in km/litre)' ]]
    x_train, x_test, y_train, y_test = train_test_split(new_data, automobileData['Ex-Showroom_Price(in lakhs)'], test_size=0.20, random_state=1)

    Rf = RandomForestRegressor()
    Rf.fit(x_train, y_train)
    predicted = Rf.predict([[disp,cap,width,mlg]])
    return predicted

def app(automobileData):
    html_temp = """
    <div style="background-color:#8A2BE2 ;padding:10px">
    <h3 style="color:white;text-align:center;">Car Price Prediction </h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("\n")
    st.write("**From the correlation analysis it was evident that Displacement, Fuel_Tank_Capacity , Width and ARAI_Certified_Mileage are most important predictor variables for price.** ")
    st.markdown("#### Enter the values of predictor variables: ")

    form=st.form(key = "my_form")

    displacement=form.number_input("Displacement",step=1)
    capacity=form.number_input("Fuel Tank Capacity",step=1)
    width=form.number_input("Width",step=1)
    mileage=form.number_input("ARAI CERTIFIED MILEAGE",step=0.1)
    submitted = form.form_submit_button("Predict")

    if submitted:
        price=prediction(displacement,capacity,width,mileage,automobileData)
        st.markdown('### Predicted Price: (in lakhs) ')
        st.markdown(price[0])