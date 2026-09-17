import streamlit as st

st.title("Calculator")
st.write("Enter any nuber of of your choice and get its square and cube instantly!")

# input
n = st.number_input("Enter any number int or float")

# mathematics
square = n**2
cube = n**3

# output
st.write(f"Square of your input {n} : {square}")
st.write(f"Cube of your input {n} : {cube}")