import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="HTML 파일 보기", layout="wide")

st.title("🌐 AI X PROJECT Platform")

# HTML 파일 불러오기
try:
    with open('external_site.html', 'r', encoding='utf-8') as f:  # 파일명에 맞춰 변경
        html_content = f.read()

    # HTML을 Streamlit에서 그대로 표시
    components.html(html_content, height=800, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ INDEX.html 파일을 찾을 수 없습니다. 경로와 이름을 확인하세요.")