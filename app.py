import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Header
st.header("Welcome to the Streamlit App")

# Subheader
st.subheader("This is a basic example")

# Text
st.write("Streamlit makes it easy to create web apps for data science and machine learning.")

# Input widget
name = st.text_input("Enter your name:")

# Button
if st.button("Submit"):
    st.success(f"Hello, {name}! 👋")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("You can add filters or options here.")
