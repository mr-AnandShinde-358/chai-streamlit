import streamlit as st

st.title("Chai Taste Poll")

cols1,cols2 = st.columns(2)

with cols1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/230489/pexels-photo-230489.jpeg",width=200)
    vote1=st.button("Vote Masala Chai")
with cols2:
    st.header("Adhark Chai")
    st.image("https://images.pexels.com/photos/905485/pexels-photo-905485.jpeg",width=200)
    vote2=st.button("Vote Adarak Chai")

if vote1 :
    st.success("Thanks for voting Masala chai")
elif vote2 :
    st.success("Thanks for voting Adhark chai")

name=st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("choose your tea",["Masala","kesar","Adarak"])

st.write(f"Welcome {name} and your {tea} chai is getting")

with st.expander("Show Chai Making instructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add Milk and Spices
    3. server hot
""")

st.markdown('### Welcome to chai App')

st.markdown('> Blockquote')

