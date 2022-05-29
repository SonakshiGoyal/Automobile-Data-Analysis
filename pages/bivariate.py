import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

def app(automobileData):
    html_temp = """
    <div style="background-color:#8A2BE2 ;padding:10px">
    <h3 style="color:white;text-align:center;">Bivariate Analysis </h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("### Visualizing price w.r.t other variables: ")

    choice=['Correlation Heat Map','Make vs Price','Mileage vs price','Bodystyle vs Price','Emission norm vs Price','Drivetrain vs price','Fuel_Type vs price','Engine location vs Price','Displacement vs Price','Fuel Tank Capacity vs Price']
    with st.sidebar:
        x_var = option_menu(
        menu_title = "Select option to analyse:",
        options= choice,
        default_index = 0,
        orientation = "vertical",
        styles = {
            "container": {"background-color":"lightblue"},
        }
        )

    if (x_var=="Correlation Heat Map"):
      fig, ax = plt.subplots()
      sns.heatmap(automobileData.corr(), ax=ax,  annot=True, annot_kws={"fontsize":5},linewidths=.5)
      plt.figure(figsize=(400,200))
      st.write(fig)
      output="""
      1)Price is more correlated with displacement, width and fuel tank capacity of the car.\n
      2)Wheel base is highly correlated with length, fuel tank capacity and width of the car.\n
      3)Kerb weight is mostly correlated with fuel tank capacity, length, width and wheelbase which is expected as these adds up the weight of the car.\n
      4)ARAI Certified mileage, displacement and fuel tank capacity are negatively correlated."""
      st.write("**Findings:**")
      st.write(output)

    elif (x_var=="Make vs Price"):
      price=automobileData["Ex-Showroom_Price(in lakhs)"]
      company=automobileData["Make"]

      #Economy cars (<5 lakhs)
      price1=[]
      company1=[]

      #Premium cars(>=5 lakhs and <=10 lakhs)
      price2=[]
      company2=[]

      #Super Premium cars(>10 lakhs and <=30 lakhs)
      price3=[]
      company3=[]

      #Luxury cars(>30 lakhs and <=75 lakhs)
      price4=[]
      company4=[]

      #Super luxury cars(>75 lakhs)
      price5=[]
      company5=[]

      j=0
      for i in price:
        if(i<5):
          price1.append(i)
          company1.append(company[j])

        elif(i>=5 and i<=10):
          price2.append(i)
          company2.append(company[j])

        elif(i>10 and i<=30):
          price3.append(i)
          company3.append(company[j])

        elif(i>30 and i<=75):
          price4.append(i)
          company4.append(company[j])

        else:
          price5.append(i)
          company5.append(company[j])
  
        j=j+1

      #Economy cars box plot
      fig, ax = plt.subplots() 
      plt.rcParams['figure.figsize']=(40,22)
      sns.boxplot(x=company1, y=price1,ax=ax,showfliers=False).set_title("Economy Cars")
      st.write(fig)

      #Premium cars box plot
      fig, ax = plt.subplots() 
      plt.rcParams['figure.figsize']=(40,22)
      sns.boxplot(x=company2, y=price2,ax=ax,showfliers=False).set_title("Premium cars")
      st.write(fig)

      #Super Premium cars box plot
      fig, ax = plt.subplots() 
      plt.rcParams['figure.figsize']=(40,22)
      sns.boxplot(x=company3, y=price3,ax=ax,showfliers=False).set_title("Super Premium cars")
      st.write(fig)

      #Luxury cars box plot
      fig, ax = plt.subplots() 
      plt.rcParams['figure.figsize']=(40,22)
      sns.boxplot(x=company4, y=price4,ax=ax,showfliers=False).set_title("Luxury cars")
      st.write(fig)

      # Super luxury cars box plot
      fig, ax = plt.subplots() 
      plt.rcParams['figure.figsize']=(40,22)
      sns.boxplot(x=company5, y=price5,ax=ax,showfliers=False).set_title("Super luxury cars")
      st.write(fig)
     
      output="""
      1)Maruti Suzuki and Tata sell maximum cars in economic and premium range,costing upto 15 lakhs\n
      2)BMW, Ford and Audi are the maximum sellers of luxury cars,costing upto 100 lakhs\n
      3)Most of the car companies produce cars in range below 50 lakhs"""
      st.write("**Findings:**")
      st.write(output)

    elif(x_var=="Mileage vs price"):
      fig, ax = plt.subplots() 
      plt.figure(figsize=(8,8))
      sns.regplot(x='ARAI_Certified_Mileage (in km/litre)',y='Ex-Showroom_Price(in lakhs)',data=automobileData,ax=ax)
      plt.title("Displacement vs Price",fontsize=20)
      st.write(fig)

      output="""
      Mileage and price are almost linearly related and price increases as the mileage decreases. Maximum number of cars produced,have mileage in range 10 to 20 km/litre.
      """
      st.write("**Findings:**")
      st.write(output)

    elif (x_var=="Bodystyle vs Price"):
      fig, ax = plt.subplots() 
      plt.rcParams['figure.figsize']=(30,10)
      sns.boxplot(x="Body_Type", y="Ex-Showroom_Price(in lakhs)", data=automobileData,ax=ax,showfliers=False)
      st.write(fig)
      output="""
      1)Coupe and Convertible car models are in the medium-high price range.\n
      2)All other car type models fall under the economic price range.
      """
      st.write("**Findings:**")
      st.write(output)
  
    elif (x_var=="Emission norm vs Price"):
      fig, ax = plt.subplots() 
      plt.rcParams['figure.figsize']=(10,5)
      sns.boxplot(x="Emission_Norm", y="Ex-Showroom_Price(in lakhs)", data=automobileData,ax=ax,showfliers=False)
      st.write(fig)
      output="""
      1)BS III Emission Norm cars are very cheap.\n
      2)BS IV Emission Norm cars are the costliest followed by BS VI Emission Norm Cars.
      """
      st.write("**Findings:**")
      st.write(output)

    elif (x_var=="Drivetrain vs price"):
      fig, ax = plt.subplots() 
      plt.rcParams['figure.figsize']=(10,5)
      sns.boxplot(x="Drivetrain", y="Ex-Showroom_Price(in lakhs)", data=automobileData,ax=ax,showfliers=False)
      st.write(fig)
      output="""
      All Wheel drive cars are the costliest, followed by Rear Wheel Drive cars and the cheapest are Front Wheel Drive cars.
      """
      st.write("**Findings:**")
      st.write(output)

    elif (x_var=="Fuel_Type vs price"):
      fig, ax = plt.subplots() 
      plt.rcParams['figure.figsize']=(10,5)
      sns.boxplot(x="Fuel_Type", y="Ex-Showroom_Price(in lakhs)", data=automobileData,ax=ax,showfliers=False)
      st.write(fig)
      output="""
      1)Hybrid cars are the costliest cars.\n
      2)Petrol and diesel are moderately priced cars.\n
      3)Cars operating on CNG are the cheapest.\n
      """
      st.write("**Findings:**")
      st.write(output)

    elif (x_var=="Engine location vs Price"):
      fig, ax = plt.subplots() 
      plt.rcParams['figure.figsize']=(10,5)
      sns.boxplot(x="Engine_Location", y="Ex-Showroom_Price(in lakhs)", data=automobileData,ax=ax,showfliers=False)
      st.write(fig)
      output="""
      1)Rear, Transvere and Longitudinal engine location result in increased prices of the car.\n
      2)Front, Transverse engine location has cheap car prices.\n
      """
      st.write("**Findings:**")
      st.write(output)

    elif(x_var=="Displacement vs Price"):
      fig, ax = plt.subplots() 
      plt.figure(figsize=(8,8))
      sns.regplot(x='Displacement(in cc)',y='Ex-Showroom_Price(in lakhs)',data=automobileData,ax=ax)
      plt.title("Displacement vs Price",fontsize=20)
      st.write(fig)

      output="""
      Displacement and price are almost linearly related and price increases as the displacement increases. Maximum number of cars are produced in 1000 to 3000cc.
      """
      st.write("**Findings:**")
      st.write(output)

    elif(x_var=="Fuel Tank Capacity vs Price"):
      fig, ax = plt.subplots() 
      plt.figure(figsize=(8,8))
      sns.regplot(x='Fuel_Tank_Capacity (in litres)',y='Ex-Showroom_Price(in lakhs)',data=automobileData,ax=ax)
      plt.title("Fuel Tank Capacity (in litres) vs Price",fontsize=20)
      st.write(fig)

      output="""
      Capacity and price are moderately linearly related, price increases as the capacity increases.
      """
      st.write("**Findings:**")
      st.write(output)
    