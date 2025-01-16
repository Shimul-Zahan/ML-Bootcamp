import streamlit as st
import pandas as pd
import numpy as np

# First title of the application
st.title("My First Streamlite Application")

# display a simple text
st.write("hey this is a simple text")

# create simple df and print it
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column' : [10,20,30,40]
})

# display the df
st.write("here is the DataFrame")
st.write(df)


# create a line chart
chart_data= pd.DataFrame(
    np.random.randn(20,3), columns=["first", "second", "third"]  # 20, 3 means 20 rows and 3 columns
)
st.line_chart(chart_data)