import streamlit as st
import streamlit.components.v1 as htmlviewer
st.set_page_config(layout='wide', page_title='DNA sequencying!!!')

# title msg#1
st.title("this is sky webapp!!")

with open('./index.html', 'r', encoding='utf-8') as f:
    html = f.read() 
    f.close()

#html = '''
#<html>
#    <head>
#        <title> this is my html </title>
#    </head>

#    <body>
#        <h1>topic</h1>
#        <h2>SubTopic</h2>
#</body>
#</html>
#'''

# box#1(4),box#2(1)
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('content #1...'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('content..')
        st.video(url)

with st.expander('image content...'):
        imgfile = './images/gpt.jpg'
        st.image(imgfile)

with st.expander('content #2...'):
        st.write(html,unsafe_allow_html=True)
        htmlviewer.html(html, height=600)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by skykang', unsafe_allow_html=True)