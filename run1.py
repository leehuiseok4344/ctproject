import streamlit as st
# title msg#1
st.title("this is Hui World!!")

with open('./index.html', 'r', encoding='utf-8') as f:
    html = f.read() 
    f.close()