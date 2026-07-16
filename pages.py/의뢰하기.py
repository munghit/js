import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="의뢰하기 | Jessica Detective Agency",
    page_icon="🕵️",
    layout="centered"
)

# 디자인 CSS
st.markdown("""
<style>
    [data-testid="stSidebar"] { display: none; }
    
    /* 전체 배경 */
    .stApp { background-color: #050505 !important; }
    
    /* 제목 */
    .title {
        font-family: 'Cinzel', serif;
        color: white;
        text-align: center;
        font-size: 50px;
        margin-top: 50px;
        margin-bottom: 50px;
    }
    
    /* 라벨 색상 */
    label { color: #FFD369 !important; font-weight: bold !important; }
    
    /* 버튼 스타일 */
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, rgba(255,255,255,.15), rgba(255,255,255,.03));
        border: 1px solid #FFD369;
        color: #FFD369;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# 페이지 내용
st.markdown('<div class="title">REQUEST</div>', unsafe_allow_html=True)

with st.form("request_form"):
    name = st.text_input("의뢰인 성함")
    contact = st.text_input("연락처 (이메일 또는 전화번호)")
    category = st.selectbox("의뢰 유형", ["사람 찾기", "사실 조사", "디지털 분석", "기업 조사", "기타"])
    details = st.text_area("상세 내용", height=200, placeholder="의뢰하실 내용을 상세히 적어주세요.")
    
    submitted = st.form_submit_button("의뢰 제출하기")
    
    if submitted:
        if name and details:
            st.success("의뢰가 안전하게 접수되었습니다.")
        else:
            st.error("성함과 상세 내용을 모두 입력해주세요.")

# 홈으로 돌아가기 버튼
if st.button("홈으로 돌아가기"):
    st.switch_page("main.py")
