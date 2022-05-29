import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

def app(automobileData):
    html_temp = """
    <div style="background-color:#8A2BE2 ;padding:10px">
    <h3 style="color:white;text-align:center;">Univariate Analysis </h3>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("### Finding the most used car specifications:")

    x=automobileData.drop(['Model', 'Variant'], axis=1)
    choice=[]
    for i in x.columns:
        choice.append(i)
    with st.sidebar:
        x_var = option_menu(
        menu_title = "Select the variable to be predicted (x)",
        options= choice,
        default_index = 0,
        orientation = "vertical",
        styles = {
            "container": {"background-color": "lightblue"},
        }
        )

    if(x_var=="Make"):
        dict = {}                                                                    #making a dictionary to store data
        for make in automobileData['Make'].unique():
            dict[make] = sum(automobileData['Make']==make)
            statistics = sorted(dict.items(), key=lambda x: x[1], reverse=True)[:20]
        fig=plt.figure(figsize=(70,40))
        x=list(automobileData['Make'].unique())
        y=list(automobileData['Make'].value_counts(sort=False))
        plt.title("Make frequency diagram",size=50)
        plt.ylabel('Percentage of vehicles',size=50)
        plt.xlabel('Make',size=50)
        plt.yticks(fontsize=50)
        plt.xticks(range(len(statistics)),[val[0] for val in statistics],fontsize=50)
        plt.bar(range(len(statistics)), [val[1] for val in statistics], align='center',color='maroon')
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Among all the car producing companies, top variant producers are Maruti Suzuki, followed by Hyundai, followed by Mahindra.")
        

    elif(x_var=="Ex-Showroom_Price(in lakhs)"):
        arr = automobileData[["Ex-Showroom_Price(in lakhs)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=30)
        plt.title("Price frequency diagram")
        plt.xlabel("Ex showroom price(in lakhs)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most vehicles are in price range 2 lakhs to 100 lakhs.")

    elif(x_var=="Displacement(in cc)"):
        arr = automobileData[["Displacement(in cc)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Displacement frequency diagram")
        plt.xlabel("Displacement(in cc)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most vehicles have displacement in range 800 to 2500 cc")

    elif(x_var=="Cylinders"):
        arr = automobileData[["Cylinders"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Cylinders frequency diagram")
        plt.xlabel("No. of Cylinders")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most of the cars use 4 cylinders.")

    elif(x_var=="Valves_Per_Cylinder"):
        arr = automobileData[["Valves_Per_Cylinder"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Valves per Cylinder frequency diagram")
        plt.xlabel("Valves per Cylinder")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most of the cars have 4-5 valves/cylinder.")

    elif(x_var=="Drivetrain"):
        fig=plt.figure(figsize=(70,40))
        x=list(automobileData['Drivetrain'].unique())
        y=list(automobileData['Drivetrain'].value_counts(sort=False,normalize=True))
        plt.title("DriveTrain frequency diagram",size=50)
        plt.ylabel('Percentage of vehicles',size=50)
        plt.xlabel('DriveTrain',size=50)
        plt.yticks(fontsize=30)
        plt.xticks(fontsize=30)
        plt.bar(x,y,color='maroon')
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("More than 70% of the vehicles have Front Wheel Drivetrain frequency.")

    elif(x_var=="Cylinder_Configuration"):
        fig=plt.figure(figsize=(70,40))
        x=list(automobileData['Cylinder_Configuration'].unique())
        y=list(automobileData['Cylinder_Configuration'].value_counts(sort=False,normalize=True))
        plt.title("Cylinder Configuration frequency diagram",size=50)
        plt.ylabel('Percentage of vehicles',size=50)
        plt.xlabel('Cylinder Configuration',size=50)
        plt.yticks(fontsize=30)
        plt.xticks(fontsize=30)
        plt.bar(x,y,color='maroon')
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("90% of the cars have inline cylinder configuration.")

    elif(x_var=="Emission_Norm"):
        fig=plt.figure(figsize=(70,40))
        x=list(automobileData['Emission_Norm'].unique())
        y=list(automobileData['Emission_Norm'].value_counts(sort=False,normalize=True))
        plt.title("Emission_Norm frequency diagram",size=50)
        plt.ylabel('Percentage of vehicles',size=50)
        plt.xlabel('Emission_Norm',size=50)
        plt.yticks(fontsize=30)
        plt.xticks(fontsize=30)
        plt.bar(x,y,color='maroon')
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Around 70% vehicles follow BS IV Emission norm.")

    elif(x_var=="Engine_Location"):
        fig=plt.figure(figsize=(70,40))
        x=list(automobileData['Engine_Location'].unique())
        y=list(automobileData['Engine_Location'].value_counts(sort=False,normalize=True))
        plt.title("Engine_Location frequency diagram",size=50)
        plt.ylabel('Percentage of vehicles',size=50)
        plt.xlabel('Engine_Location',size=50)
        plt.yticks(fontsize=30)
        plt.xticks(fontsize=30)
        plt.bar(x,y,color='maroon')
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most produced vehicles have engine location: front-transverse around 65%, followed by front-longitudinal 30% .")

    elif(x_var=="Fuel_System"):
        fig=plt.figure(figsize=(70,40))
        x=list(automobileData['Fuel_System'].unique())
        y=list(automobileData['Fuel_System'].value_counts(sort=False,normalize=True))
        plt.title("Fuel_System frequency diagram",size=50)
        plt.ylabel('Percentage of vehicles',size=50)
        plt.xlabel('Fuel_System',size=50)
        plt.yticks(fontsize=30)
        plt.xticks(fontsize=30)
        plt.bar(x,y,color='maroon')
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Almost all the cars have injection fuel system .")

    elif(x_var=="Fuel_Tank_Capacity (in litres)"):
        arr = automobileData[["Fuel_Tank_Capacity (in litres)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Fuel_Tank_Capacity (in litres) frequency diagram")
        plt.xlabel("Fuel_Tank_Capacity (in litres)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most vehicles have fuel tank capacity in the range of 35-70 litres .")

    elif(x_var=="Fuel_Type"):
        fig=plt.figure(figsize=(70,40))
        x=list(automobileData['Fuel_Type'].unique())
        y=list(automobileData['Fuel_Type'].value_counts(sort=False,normalize=True))
        plt.title("Fuel_Type frequency diagram",size=50)
        plt.ylabel('Percentage of vehicles',size=50)
        plt.xlabel('Fuel_Type',size=50)
        plt.yticks(fontsize=30)
        plt.xticks(fontsize=30)
        plt.bar(x,y,color='maroon')
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Almost 50% cars use petrol, followed by 45% diesel .")
    
    elif(x_var=="Height (in mm)"):
        arr = automobileData[["Height (in mm)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Height (in mm) frequency diagram")
        plt.xlabel("Height (in mm)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most vehicles have height in range 1500-2000 mm .")

    elif(x_var=="Length(in mm)"):
        arr = automobileData[["Length(in mm)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Length(in mm) frequency diagram")
        plt.xlabel("Length(in mm)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most vehicles have length in range 3500-5000 mm .")

    elif(x_var=="Width(in mm)"):
        arr = automobileData[["Width(in mm)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Width(in mm) frequency diagram")
        plt.xlabel("Width(in mm)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most vehicles have width in range 1500-2000 mm .")

    elif(x_var=="Body_Type"):
        fig=plt.figure(figsize=(70,40))
        x=list(automobileData['Body_Type'].unique())
        y=list(automobileData['Body_Type'].value_counts(sort=False,normalize=True))
        plt.title("Body_Type frequency diagram",size=50)
        plt.ylabel('Percentage of vehicles',size=50)
        plt.xlabel('Body_Type',size=50)
        plt.yticks(fontsize=30)
        plt.xticks(fontsize=30)
        plt.bar(x,y,color='maroon')
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most vehicles are of body style SUV 36% followed by hatchback and sedan, 26% and 25% respectively .")

    elif(x_var=="Doors"):
        arr = automobileData[["Doors"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Doors frequency diagram")
        plt.xlabel("Doors")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most of the cars have 5 doors .")

    elif(x_var=="City_Mileage (in km/litre)"):
        arr = automobileData[["City_Mileage (in km/litre)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("City_Mileage (in km/litre) frequency diagram")
        plt.xlabel("City_Mileage (in km/litre)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most cars have City Mileage between 0-2500 km/litre.")

    elif(x_var=="Highway_Mileage (in km/litre)"):
        arr = automobileData[["Highway_Mileage (in km/litre)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Highway_Mileage (in km/litre) frequency diagram")
        plt.xlabel("Highway_Mileage (in km/litre)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most cars have Highway Mileage between 15-20 km/litre.")

    elif(x_var=="ARAI_Certified_Mileage (in km/litre)"):
        arr = automobileData[["ARAI_Certified_Mileage (in km/litre)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("ARAI_Certified_Mileage (in km/litre) frequency diagram")
        plt.xlabel("ARAI_Certified_Mileage (in km/litre)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most cars have ARAI Certified Mileage between 10-25 km/litre.")

    elif(x_var=="Kerb_Weight (in kg)"):
        arr = automobileData[["Kerb_Weight (in kg)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Kerb_Weight (in kg) frequency diagram")
        plt.xlabel("Kerb_Weight (in kg)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most cars have Kerb Weight between 1000-1500 kg.")

    elif(x_var=="Gears"):
        arr = automobileData[["Gears"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Gears frequency diagram")
        plt.xlabel("Gears")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most of the cars have 5 gears .")

    elif(x_var=="Ground_Clearance(in mm)"):
        arr = automobileData[["Ground_Clearance(in mm)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Ground_Clearance(in mm)")
        plt.xlabel("Ground_Clearance(in mm)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most cars have Ground Clearance between 150-200 mm.")

    elif(x_var=="Seating_Capacity"):
        arr = automobileData[["Seating_Capacity"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Seating_Capacity frequency diagram")
        plt.xlabel("Seating_Capacity")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("The seating capacity varies between 5-8 .")

    elif(x_var=="Wheelbase (in mm)"):
        arr = automobileData[["Wheelbase (in mm)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Wheelbase (in mm) frequency diagram")
        plt.xlabel("Wheelbase (in mm)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most cars have Wheelbase between 2500-3000 mm.")

    elif(x_var=="Boot_Space (in litres)"):
        arr = automobileData[["Boot_Space (in litres)"]]
        fig, ax = plt.subplots()
        ax.hist(arr,bins=10)
        plt.title("Boot_Space (in litres) frequency diagram")
        plt.xlabel("Boot_Space (in litres)")
        plt.ylabel("No. of vehicles")
        st.pyplot(fig)

        st.write("**Findings:**")
        st.write("Most cars have Boot space between 250-500 litres.")



    

