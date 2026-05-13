import streamlit as st
import pickle
st.write("Hello ,let's find out the type of iris flower")
petal_length = st.number_input("Enter petal length")    # number input
petal_width = st.number_input("Enter petal width")    # number input
sepal_length = st.number_input("Enter sepal length")    # number input
sepal_width = st.number_input("Enter sepal width")    # number input    
if st.button("Predict"):
    with open(r"C:\\Users\\kobeb\\akira intership\\iris_model.pkl", "rb") as file:
        loaded_model = pickle.load(file)    
    result = loaded_model.predict([[petal_length, petal_width, sepal_length, sepal_width]])
    st.write(result)