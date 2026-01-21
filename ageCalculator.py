import streamlit as st
st.title("Let's calculate your age dear user")
name = st.text_input("You name please")
if name:
    st.write(f"Welcome {name} ji, let's check your age")
dob = st.date_input("Enter your Date Of Birth")
if dob:
    age = 2026 - dob.year
    st.success(f"Your age is {age} years!")
