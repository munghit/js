import streamlit as st

st.set_page_config(
    page_title="Jessica Detective Agency",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    /* 기본 UI 숨기기 */
    [data-testid="stSidebar"] { display: none; }
    #MainMenu { visibility: hidden; }
    header { visibility: hidden; }
    
    /* 배경 및 폰트 */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Orbitron:wght@500;700&family=Noto+Sans+KR:wght@300;500;700&display=swap');
    .stApp { background-color: #050505 !important; }

    .hero { 
        display: flex; flex-direction: column; justify-content: center; 
        align-items: center; text-align: center; padding-top: 100px;
    }
    .title { font-family: 'Cinzel'; font-size: 80px; color: white; margin-bottom: 10px; }
    .subtitle { font-family: 'Orbitron'; color: #9b55ff; font-size: 30px; margin-bottom: 20px; }
    .desc { font-family: 'Noto Sans KR'; color: #ddd; font-size: 18px; margin-bottom: 40px; }

    /* 버튼 스타일 (강제 노출) */
    div.stButton > button {
        background-color: #FFD369 !important;
        color: black !important;
        font-weight: 800 !important;
        width: 250px !important;
        height: 60px !important;
        border-radius: 50px !important;
        border: none !important;
        font-size: 18px !important;
    }
</style>
""", unsafe_allow_html=True)

# 화면 구성
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<div class="title">DETECTIVE</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AGENCY</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">진실은 언제나 흔적을 남깁니다.<br>당신의 의뢰는 안전하게 보호됩니다.</div>', unsafe_allow_html=True)

# 버튼 (마크다운 밖에서 실행해야 확실히 보임)
if st.button("🔐 의뢰하기"):
    st.switch_page("pages/1_의뢰하기.py")

st.markdown('</div>', unsafe_allow_html=True)
