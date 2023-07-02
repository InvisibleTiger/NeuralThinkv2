import streamlit as st
import search   

input = st.text_input('URL')
if st.button('Summarize'):
    st.text(search.summarize(input))