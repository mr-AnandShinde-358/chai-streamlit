import streamlit as st

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interative app")
st.write("choose your fav. variety of chai")

chai = st.selectbox("Your fav chai: ", ["Masala chai","Lemon Tea","Adrak chai","Kesar chai"])

st.write(f"You choose {chai}. Excellent choice")

st.success("You chai has been brewed")

# Assigment : choose your fav programing langauge

prlang = st.selectbox("choose your fav programing langauge: ", ["JavaScript","Python","Java","C","C++"])

st.write(f"You choose {prlang}! it's super")