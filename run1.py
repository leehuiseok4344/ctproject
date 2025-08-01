import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="AI HTML Viewer", layout="wide")
st.title("🌐 AI X Project Platform")

# HTML 파일 경로 (run1.py와 같은 폴더)
html_file = os.path.join(os.path.dirname(__file__), "AI.html")

# 파일 읽기 및 Streamlit에서 표시
try:
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # HTML을 Streamlit에서 그대로 렌더링
    components.html(html_content, height=1200, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ 'AI.html' 파일을 찾을 수 없습니다. 경로와 파일명을 확인하세요.")