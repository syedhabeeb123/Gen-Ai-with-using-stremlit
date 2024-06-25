import os
import streamlit as st
import pickle
import time
import langchain
from langchain import OpenAI
import google.generativeai as genai
#api key
genai.configure(api_key="AIzaSyAfApyeIY7GYJ4lR6fwg9G60n7wW9Izaro")

st.title("Welcom to Text to Text App")

text = st.text_input("Enter any text")
if st.button("GET RSPONSE"):
# generativeai model
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content([text])
    st.markdown(response.text)