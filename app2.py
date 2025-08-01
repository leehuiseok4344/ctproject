import streamlit as st

st.set_page_config(page_title="CT 문제 해결", layout="centered")

# 사이드바 메뉴
menu = st.sidebar.selectbox(
    "문제를 선택하세요",
    ["콘텐츠1: 이름으로 비밀번호 생성기", 
     "콘텐츠2: 주식 평단가 계산하기"]
     )

# -----------------------------
# 콘텐츠1: 이름으로 비밀번호 생성기
# -----------------------------
if menu == "콘텐츠1: 이름으로 비밀번호 생성기":
    st.markdown("""
    <div style="
        background: linear-gradient(90deg, #42a5f5, #478ed1);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: white;
        margin-bottom: 20px;
    ">
    🔐 이름으로 비밀번호 생성기
    </div>
    """, unsafe_allow_html=True)

    st.subheader("대상 및 교과: 고2 컴퓨터 시스템 일반")

    st.markdown("""
    **지문:**  
    암호화 복호화 내용을 공부하던 천재 해커 카피바라는 한 웹 사이트의 비밀번호 생성기를 만들고 싶었다.  
    다음과 같은 알고리즘을 통해 이름으로 비밀번호 생성기를 만들었다.
    """)

    # 규칙 박스
    st.markdown("""
    <div style="
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 10px;
        background-color: #f1f8e9;
        margin-bottom: 20px;
    ">
    <b>규칙</b><br>
    1️⃣ 입력된 이름에서 모음(a, e, i, o, u)을 제거<br>
    2️⃣ 남은 문자를 뒤집기<br>
    3️⃣ 마지막에 전체 길이를 붙이기
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**문제:** 'minji'라는 이름으로 비밀번호를 만들면 결과는?")

    # 보기 박스
    st.markdown("""
    <div style="
        border: 2px solid #2196F3;
        border-radius: 10px;
        padding: 10px;
        background-color: #e3f2fd;
        margin-top: 20px;
    ">
    <b>보기</b><br>
    A. jnm3<br>
    B. jnm5<br>
    C. jn3<br>
    D. jn2
    </div>
    """, unsafe_allow_html=True)

    # 정답 선택
    choices2 = ["A. jnm3", "B. jnm5", "C. jn3", "D. jn2"]
    selected2 = st.radio("정답 선택", choices2, index=None, key="answer2")

    if st.button("정답 확인", key="check2"):
        if selected2 == "A. jnm3":
            st.success("정답입니다! (minji → mnj → jnm + 길이 3 = jnm3)")
        else:
            st.error("틀렸습니다. 다시 선택해보세요!")

# -----------------------------
# 콘텐츠2: 주식 평단가 계산하기
# -----------------------------
elif menu == "콘텐츠2: 주식 평단가 계산하기":
    st.markdown("""
    <div style="
        background: linear-gradient(90deg, #ff9800, #f57c00);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: white;
        margin-bottom: 20px;
    ">
    📊 주식 평단가 계산하기
    </div>
    """, unsafe_allow_html=True)

    # ===== 1) 주식 평단가 계산 문제 =====

    st.markdown("""
    **문제:**  
    카피바라는 A주식을 3번에 걸쳐 매수했습니다. 아래 데이터를 기반으로 평단가를 계산하시오.
    """)

    st.table({
        "거래번호": [1, 2, 3],
        "매수가(원)": [50000, 55000, 53000],
        "수량(주)": [3, 2, 5]
    })

    st.markdown("""
    <div style="
        border: 2px solid #2196F3;
        border-radius: 10px;
        padding: 10px;
        background-color: #e3f2fd;
        margin-top: 20px;
    ">
   
    """, unsafe_allow_html=True)

    choices3 = ["① 52,750원", "② 53,500원", "③ 52,500원", "④ 54,000원"]
    selected3 = st.radio("정답 선택", choices3, index=None, key="answer3")

    if st.button("정답 확인", key="check3"):
        if selected3 == "③ 52,500원":
            st.success("정답입니다! (총매수금액 525,000원 ÷ 총수량 10주 = 52,500원)")
        else:
            st.error("틀렸습니다. 다시 선택해보세요!")

    st.markdown("---")

    # ===== 2) 주식 평단가 계산하기 =====
    st.subheader(" 직접 평단가 계산기 사용해보기")

    num_trades = st.number_input("매수 횟수 선택", min_value=1, max_value=10, value=3, step=1, key="num_trade")
    total_cost, total_qty = 0, 0

    st.write("### 매수 정보 입력")

    for i in range(int(num_trades)):
        col1, col2 = st.columns(2)
        with col1:
            price = st.number_input(f"{i+1}회차 매수가(원)", min_value=0, step=100, value=50000, key=f"price_{i}")
        with col2:
            qty = st.number_input(f"{i+1}회차 수량(주)", min_value=0, step=1, value=1, key=f"qty_{i}")

        total_cost += price * qty
        total_qty += qty

    if total_qty > 0:
        avg_price = total_cost / total_qty
        

        

