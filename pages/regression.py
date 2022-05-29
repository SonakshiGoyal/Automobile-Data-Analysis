import streamlit as st
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from streamlit_option_menu import option_menu

def app(automobileData):
    html_temp = """
    <div style="background-color:#8A2BE2 ;padding:10px">
    <h3 style="color:white;text-align:center;">Regression Analysis </h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    choice=['Correlation analysis','Multiple Linear Regression','Polynomial Linear Regression','Random Forest Regression']
    with st.sidebar:
        x_var = option_menu(
        menu_title = "Select option to analyse:",
        options= choice,
        default_index = 0,
        orientation = "vertical",
        styles = {
            "container": {"background-color": "lightblue"},
        }
        )

    if (x_var=="Correlation analysis"):
      st.markdown("#### Correlation analysis:")
      st.write("**The Pearson Coefficient for:**")
      pearson_coef, p_value = stats.pearsonr(automobileData['Displacement(in cc)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write(" **1)Displacement vs price** is", pearson_coef, " with a P-value of P =", p_value)  
      pearson_coef, p_value = stats.pearsonr(automobileData['Fuel_Tank_Capacity (in litres)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write("**2)Fuel_Tank_Capacity vs price** is", pearson_coef, " with a P-value of P =", p_value) 
      pearson_coef, p_value = stats.pearsonr(automobileData['Height (in mm)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write("**3)height vs price** is", pearson_coef, " with a P-value of P =", p_value)  
      pearson_coef, p_value = stats.pearsonr(automobileData['Length(in mm)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write("**4)length vs price** is", pearson_coef, " with a P-value of P =", p_value ) 
      pearson_coef, p_value = stats.pearsonr(automobileData['Width(in mm)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write( "**5)width vs price** is", pearson_coef, " with a P-value of P =", p_value)  
      pearson_coef, p_value = stats.pearsonr(automobileData['City_Mileage (in km/litre)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write("**6)city mileage vs price** is", pearson_coef, " with a P-value of P =", p_value) 
      pearson_coef, p_value = stats.pearsonr(automobileData['Highway_Mileage (in km/litre)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write("**7)highway mileage vs price** is", pearson_coef, " with a P-value of P =", p_value ) 
      pearson_coef, p_value = stats.pearsonr(automobileData['ARAI_Certified_Mileage (in km/litre)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write("**8)ARAI mileage vs price** is", pearson_coef, " with a P-value of P =", p_value) 
      pearson_coef, p_value = stats.pearsonr(automobileData['Ground_Clearance(in mm)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write( "**9)ground clearnace vs price** is", pearson_coef, " with a P-value of P =", p_value )
      pearson_coef, p_value = stats.pearsonr(automobileData['Wheelbase (in mm)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write( "**10)wheelbase vs price** is", pearson_coef, " with a P-value of P =", p_value )
      pearson_coef, p_value = stats.pearsonr(automobileData['Boot_Space (in litres)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write( "**11)boot space vs price** is", pearson_coef, " with a P-value of P =", p_value )
      pearson_coef, p_value = stats.pearsonr(automobileData['Kerb_Weight (in kg)'], automobileData['Ex-Showroom_Price(in lakhs)'])
      st.write( "**12)kerb weight vs price** is", pearson_coef, " with a P-value of P =", p_value )

      output=""" 
      1)Since the p-value is < 0.001, the correlation between displacement and price is statistically significant, and the linear relationship is quite strong (~0.863, close to 1).\n
      2)Since the p-value is < 0.001, the correlation between fuel tank capacity and price is statistically significant, and the linear relationship is moderately strong (~0.634).\n
      3)Since the p-value is < 0.001, the correlation between width and price is statistically significant, and the linear relationship is moderately strong (~0.538).\n
      4)Since the p-value is < 0.001, the correlation between ARAI mileage and price is statistically significant, and the coefficient of ~ -0.501 shows that the relationship is negative and moderately strong.\n
      """
      st.write("**Findings:**")
      st.write(output)

    if (x_var=="Multiple Linear Regression"):
      st.markdown("### Regression Model using price predictor variables:")
      new_data = automobileData[['Displacement(in cc)', 'Fuel_Tank_Capacity (in litres)', 'Width(in mm)', 'ARAI_Certified_Mileage (in km/litre)' ]]
      x_train, x_test, y_train, y_test = train_test_split(new_data, automobileData['Ex-Showroom_Price(in lakhs)'], test_size=0.20, random_state=1)

      lm = LinearRegression()
      lm.fit(x_train, y_train)

      st.write("The R_squared value for Multiple Linear Regression Model is: ", lm.score(x_test, y_test))
      predicted = lm.predict(x_test)

      plt.figure(figsize=(12, 4))

      fig, ax = plt.subplots()
      ax1=sns.distplot(automobileData['Ex-Showroom_Price(in lakhs)'], hist=False, color="r", label="Actual Value",ax=ax)
      sns.distplot(predicted, hist=False, color="b", label="predicted Values" , ax=ax1)
      st.write(fig)
      plt.title('Actual vs predicted Values for Price')
      plt.xlabel('Price (in lakhs)')
      plt.ylabel('Proportion of Cars')

      output="""
      It can be said that ~ 78% of the variation of the price is explained by this multiple linear regression model."""
      st.write("**Findings:**")
      st.write(output)

    elif (x_var=="Polynomial Linear Regression"):
      st.markdown("### Regression Model using price predictor variables:")
      new_data = automobileData[['Displacement(in cc)', 'Fuel_Tank_Capacity (in litres)', 'Width(in mm)', 'ARAI_Certified_Mileage (in km/litre)' ]]
      x_train, x_test, y_train, y_test = train_test_split(new_data, automobileData['Ex-Showroom_Price(in lakhs)'], test_size=0.20, random_state=1)
      Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]
      pipe=Pipeline(Input)
      pipe.fit(x_train,y_train)
      st.write("The R_squared value for Polynomial Linear Regression Model is: ", pipe.score(x_test, y_test))
      predicted = pipe.predict(x_test)

      plt.figure(figsize=(12, 4))

      fig, ax = plt.subplots()
      ax1 = sns.distplot(automobileData['Ex-Showroom_Price(in lakhs)'], hist=False, color="r", label="Actual Value")
      sns.distplot(predicted, hist=False, color="b", label="predicted Values" , ax=ax1)
      st.write(fig)

      plt.title('Actual vs predicted Values for Price')
      plt.xlabel('Price (in lakhs)')
      plt.ylabel('Proportion of Cars')

      output="""
      It can be that ~ 65% of the variation of the price is explained by this polynomial regression model."""
      st.write("**Findings:**")
      st.write(output)

    elif (x_var=="Random Forest Regression"):
      st.markdown("### Regression Model using price predictor variables:")
      new_data = automobileData[['Displacement(in cc)', 'Fuel_Tank_Capacity (in litres)', 'Width(in mm)', 'ARAI_Certified_Mileage (in km/litre)' ]]
      x_train, x_test, y_train, y_test = train_test_split(new_data, automobileData['Ex-Showroom_Price(in lakhs)'], test_size=0.20, random_state=1)
      Rf = RandomForestRegressor()
      Rf.fit(x_train, y_train)
      st.write("The R_squared value for Random Forest Regression Model is: ", Rf.score(x_test, y_test))
      predicted = Rf.predict(x_test)

      plt.figure(figsize=(12, 4))

      fig, ax = plt.subplots()
      ax1 = sns.distplot(automobileData['Ex-Showroom_Price(in lakhs)'], hist=False, color="r", label="Actual Value")
      sns.distplot(predicted, hist=False, color="b", label="predicted Values" , ax=ax1)
      st.write(fig)

      plt.title('Actual vs predicted Values for Price')
      plt.xlabel('Price (in lakhs)')
      plt.ylabel('Proportion of Cars')

      output="""
      It can be said that ~ 93% of the variation of the price is explained by this random forest model."""
      st.write("**Findings:**")
      st.write(output)
      st.write("__**Thus random forest model performs the best prediction, the fitted values are very close to the actual values.**__")

