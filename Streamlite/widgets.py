import streamlit as st
import pandas as pd

# give title
st.title("Streamlit text Input")


# create form or input box
name=st.text_input("Enter Your name Here...")

# use slider
age = st.slider("Select your age" ,0, 100, 25)
# st.write(f"Your age is {age}")

if name and age:
    st.write(f"Hello Mr. { name} and your age is {age}")
    
    
    
# selct box
options=["python", "java","javaScript","C++"]
choice =st.selectbox("Choose your favourite langiuage", options)
if choice:
    st.write(f"your favourite language is {choice}")


# display one more df
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [25, 30, 22, 35, 28],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

# file upload button
uploaded_files = st.file_uploader("Choose a csv file", type='csv')
if uploaded_files:
    df = pd.read_csv(uploaded_files)
    st.write(df)