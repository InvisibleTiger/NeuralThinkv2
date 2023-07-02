import streamlit as st
import search   

input = st.text_input('URL')

st.text(search.summarize(input))