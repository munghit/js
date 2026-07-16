import streamlit as st

st.set_page_config(page_title="Jessica Detective Agency", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
/* 기본 스트림릿 초기화 */
[data-testid="stSidebar"], header, footer, #MainMenu { display: none !important; }

/* 배경색과 디자인 효과 완벽 복구 */
.stApp {
    background: radial-gradient(ellipse at 50% 10%, rgba(123,44,255,.4), transparent 45%),
                radial-gradient(ellipse at 50% 70%, rgba(90,0,180,.25), transparent 55%),
                linear-gradient(180deg, #050505, #100020, #050505);
    background-attachment: fixed;
}

/* 폰트 및 히어로 섹션 */
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Orbitron:wght@500;700&family=Noto+Sans+KR:wght@300;500;700&display=swap');
.hero { display:flex; flex-direction:column; align-items:center; text-align:center; padding-top: 150px; }
.logo{ font-family:'Orbitron'; font-size:22px; letter-spacing:12px; color:#FFD369; margin-bottom:20px; }
.title{ font-family:'Cinzel'; font-size:100px; letter-spacing:18px; color:white; text-shadow:0 0 25px rgba(255,255,255,.5); }
.subtitle{ font-family:'Orbitron'; font-size:38px; letter-spacing:12px; color:#9b55ff; margin-top:20px; margin-bottom:20px; }
.desc{ font-family:'Noto Sans KR'; font-size:22px; color:#ddd; margin-bottom: 40px; }

/* 버튼을 중앙으로 보내는 Flex 컨테이너 */
.btn-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-bottom: 60px;
}
div.stButton > button {
    width: 280px !important; height: 65px !important;
    background: linear-gradient(135deg, #4A1291, #1A0033) !important;
    color: #E2D5F5 !important; border: 2px solid #7B2CFF !important;
    font-weight: 700 !important; border-radius: 50px !important;
    font-size: 19px !important;
}

/* 카드 */
.cards { display:flex; justify-content:center; gap:30px; flex-wrap:wrap; }
.card { width:250px; padding:35px; border-radius:25px; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.18); }
</style>
""", unsafe_allow_html=True)

# 메인 콘텐츠
st.markdown("""
<div class="hero">
    <div class="logo">JESSICA</div>
    <div class="title">DETECTIVE</div>
    <div class="subtitle">AGENCY</div>
    <div class="desc">진실은 언제나 흔적을 남깁니다.<br>당신의 의뢰는 안전하게 보호됩니다.</div>
</div>
""", unsafe_allow_html=True)

# 버튼 (CSS로 중앙 배치)
st.markdown('<div class="btn-wrapper">', unsafe_allow_html=True)
if st.button("🔐 의뢰하기"):
    st.switch_page("pages/1_의뢰하기.py")
st.markdown('</div>', unsafe_allow_html=True)

# 카드 섹션
st.markdown("""
<div class="cards">
    <div class="card">사람 찾기</div>
    <div class="card">사실 조사</div>
    <div class="card">디지털 분석</div>
    <div class="card">기업 조사</div>
</div>
""", unsafe_allow_html=True)
