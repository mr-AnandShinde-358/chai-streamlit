import streamlit as st
import requests


st.title("Live currency converter")
amount =st.number_input("Enter the amount in INR",min_value=1)

target_currency =st.selectbox("Conver to:",["USD","EUR","GBP","JPY"])
if st.button("Convert"):
    url="https://api.exchangerate-api.com/v4/latest/INR"
    response=requests.get(url)

    if(response.status_code==200):
        data = response.json()
        rate =data["rates"][target_currency]
        conveted = rate * amount
        st.success(f"{amount} INR = {conveted:.2f} {target_currency}")
    else:
        st.error("Failed to Featch conversion rate")