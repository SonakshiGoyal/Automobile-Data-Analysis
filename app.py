import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu
# Custom imports 
from pages import univariate, bivariate, regression,dataset, prediction # import your pages here

st.set_page_config(
   page_title="CarScrutiny",
   page_icon="CarScrutiny logo.png",
   layout="wide",
   initial_sidebar_state="expanded",
)
col1,col2=st.columns([0.1,0.9])
with col1:
   st.image("CarScrutiny logo.png",width=140)

selected=NULL
with col2:
   #main navigation bar
   selected = option_menu(
      menu_title = "CarScrutiny APP - Autombile Data Analysis",
      options= ["View Dataset","Univariate Analysis", "Bivariate Analysis", "Regression Analysis","Price Prediction"],
      icons=["clipboard-data", "bar-chart-line-fill", "graph-up","graph-up-arrow","qr-code-scan"],
      default_index = 0,
      menu_icon="cast",
      orientation = "horizontal",
      styles = {
         "container": {"background-color": "aqua"},
      }
   )

#data cleaning
data=pd.read_csv("cars_engage_2022.csv")
automobileData = data.replace('?',np.NAN)                         #replacing data containing "?" with NAN

# dropping the rows with NaN in "Make" column
automobileData.dropna(subset=["Make"], axis=0, inplace = True)
automobileData.reset_index(drop = True, inplace = True)

#Replace"NaN" of some columns with the mean of their columns
columns = ["Displacement(in cc)","Fuel_Tank_Capacity (in litres)","Height (in mm)","Width(in mm)","City_Mileage (in km/litre)","Highway_Mileage (in km/litre)","ARAI_Certified_Mileage (in km/litre)","Kerb_Weight (in kg)","Ground_Clearance(in mm)","Wheelbase (in mm)","Boot_Space (in litres)"]

for column in columns:    
    avg = automobileData[column].astype("float").mean(axis = 0)
    automobileData[column].replace(np.nan, avg, inplace = True)

#replace "NaN" of some columns with the mode of column
columns = ["Cylinders","Valves_Per_Cylinder","Drivetrain","Cylinder_Configuration","Emission_Norm","Engine_Location","Fuel_System","Body_Type","Doors","Gears","Seating_Capacity"]

for column in columns:
  automobileData[column].replace(np.nan, automobileData[column].value_counts().idxmax(), inplace = True)

automobileData=automobileData.drop(['Unnamed: 0'],axis=1)


if(selected=='View Dataset'):
   dataset.app(automobileData)

elif(selected=='Univariate Analysis'):
   univariate.app(automobileData)

elif(selected=="Bivariate Analysis"):
   bivariate.app(automobileData)

elif(selected=="Regression Analysis"):
   regression.app(automobileData)

elif(selected=="Price Prediction"):
   prediction.app(automobileData)

