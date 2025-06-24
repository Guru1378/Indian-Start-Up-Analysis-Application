import streamlit as st
import pandas as pd
import time

data = pd.read_csv("C:\\Users\\gurup\\OneDrive\\Desktop\\Streamlit_App\\Start_Up_Dashboard\\startup_funding.csv")
st.sidebar.title("Start-Up Dashboard")
st.sidebar.subheader("Filter by Category") 
options=st.sidebar.selectbox("Select Category", options=["overall analysis","Statup","Investor"])

if options == "overall analysis":
    st.title("Overall Analysis")
    st.write("This section provides an overall analysis of the start-up funding data.")
    st.dataframe(data.head())

    st.subheader("Basic Statistics")
    st.write(data.describe())
elif options == "Statup":
    st.title("Start-Up Analysis")
    st.write("This section provides insights into individual start-ups.")
    startup_name = st.sidebar.selectbox("Select Start-Up", data['Startup Name'].unique())
    startup_data = data[data['Startup Name'] == startup_name]
    
    if not startup_data.empty:
        st.subheader(f"Details for {startup_name}")
        st.write(startup_data)
        st.subheader("Funding History")
        st.line_chart(startup_data['Amount in USD'])
    else:
        st.write("No data available for the selected start-up.")  
elif options == "Investor":
    st.title("Investor Analysis")
    st.write("This section provides insights into individual investors.")
    investor_name = st.sidebar.selectbox("Select Investor", data['Investors Name'].unique())
    investor_data = data[data['Investors Name'] == investor_name]
    if not investor_data.empty:
        st.subheader(f"Details for {investor_name}")
        st.write(investor_data)
        st.subheader("Investment History")
        st.bar_chart(investor_data['Amount in USD'])
        st.line_chart(investor_data['Amount in USD'])
    else:
        st.write("No data available for the selected investor.")                                                      