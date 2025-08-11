import streamlit as st

st.title("chai Maker App")


if st.button("Make Chai"):
    st.success("Your chai is being brewed")

add_masala = st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your chai")

tea_type = st.radio("Pick your chai base: ",["Milk","Water","Almond Milk"])

st.write(f"your selected {tea_type}")

favour = st.selectbox("Choose flavour:",["Adrak","kesar","tulshi"])

st.write(f"selected Flavor {favour}")

sugar = st.slider("Sigar level (spoon)",0,5,2)

st.write(f"Selected sugar spoon {sugar}")

cups= st.number_input("How many cups",min_value=1,max_value=10,step=1)
st.write(f"cup you orders {cups}")

name = st.text_input("Enter your name")

if name :
    st.write(f"Welcome {name}! your coppy on the way")

