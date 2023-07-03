import streamlit as st
import search
import time   

input = st.text_input('URL')

if st.button('Summarize'):
    with st.spinner('Summarizing...'):
        time.sleep(15)
        print('Summarizing...')
    st.success(search.summarize(input))
    with st.spinner('Please wait for 60 seconds before you can summarize again...'):
        time.sleep(60)
        print('Please wait for 60 seconds before you can summarize again...')