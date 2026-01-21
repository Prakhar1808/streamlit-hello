import streamlit as st

st.title("Got a Favourite Programming Language?")
st.subheader("Let's Choose your favourite Progg. Language")
st.text("Made using Streamlit on Neovim")
st.write("Check the selectbox below")

lang = st.selectbox("Choose your language:", ["Python","Rust","JavaScript","Cpp","Kotlin"])
st.write(f"You know what languages are upto the work idc if you use {lang}")
st.success(f"But it's cool that you know {lang}")
