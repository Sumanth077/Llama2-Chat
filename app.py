import streamlit as st
from clarifai_utils.modules.css import ClarifaiStreamlitCSS

st.set_page_config(layout="wide")

ClarifaiStreamlitCSS.insert_default_css(st)

from langchain.llms import Clarifai

# Title & Sidebar Image

st.title("🦙Chat with Llama 2 (70B) Model")
st.sidebar.image("https://clarifai.com/favicon.svg", width=100)

# Get the Clarifai API Key

with st.sidebar:
    clarifai_pat = st.text_input("Clarifai API Key", type="password")


# Function to Generate Response

def generate(text):
    llm = Clarifai(pat=clarifai_pat, user_id='meta', app_id='Llama-2', model_id='llama2-70b-chat')
    st.info(llm(text))

# Form that takes text as imput and return the response from the Model
with st.form("my_form"):
    text = st.text_area("Enter text:", "How to Evaluate ML Models?")
    submitted = st.form_submit_button("Submit")
    if not clarifai_pat:
        st.info("Please add your Clarifai PAT to continue.")
    elif submitted:
        generate(text)
