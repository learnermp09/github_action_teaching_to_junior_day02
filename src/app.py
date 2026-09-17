import streamlit as st

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

st.title("Calculator")
st.write("Enter any number of your choice and get its square and cube instantly!")

n = st.number_input("Enter any number int or float")

st.write(f"Square of your input {n} : {square(n)}")
st.write(f"Cube of your input {n} : {cube(n)}")