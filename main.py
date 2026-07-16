import streamlit as st

st.set_page_config(page_title="Jessica Detective Agency", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
/* 스트림릿 기본값 강제 무시 */
[data-testid="stSidebar"]{ display:none; }
header, footer, #MainMenu { visibility:hidden; }
.block-container { padding: 0 !important; max-width: none !important; }

/* 전체 앱 배경을 다크 테마로 고정 */
.stApp { background-color: #050505 !important; }

/* 배경 그라데이션이 전체 화면에 꽉 차게 */
.full-bg {
    background: radial-gradient(ellipse at 50% 10%, rgba(123,44,255,.4), transparent 45%),
                radial-gradient(ellipse at 50% 70%, rgba(90,0,180,.25), transparent 55%),
                linear-gradient(180deg, #050505, #100020, #050505);
    background-attachment: fixed;
    min-height: 100vh;
    padding: 50px 0;
}

/* 히어로 영역 */
.hero { display:flex; flex-direction:column; align-items:center; text-align:center; margin-bottom: 50px; }
.logo{ font-family:'Orbitron'; font-size:22px; letter-spacing:12px; color:#FFD369; margin-bottom:20px; }
.title{ font-family:'Cinzel'; font-size:100px; letter-spacing:18px; color:white; text-shadow:0 0 25px rgba(255,255,255,.5); }
.subtitle{ font-family:'Orbitron'; font-size:38px; letter-spacing:12px; color:#9b55ff; margin-top:10px; margin-bottom:20px; }
.desc{ font-family:'Noto Sans KR'; font-size:22px; color:#ddd; margin-bottom: 30px; }

/* 버튼을 중앙으로 강제 이동시키는 절대 규칙 */
div[data-testid="column"] { display: flex; justify-content: center; }
div[data-testid="stButton"] button {
    width: 280px !important; height: 65px !important;
    background: linear-gradient(135deg, #4A1291, #1A0033) !important;
    color: #E2D5F5 !important; border: 2px solid #7B2CFF !important;
    font-size: 19px !important; font-weight: 700 !important;
    border-radius: 50px !important;
    margin: 0 auto !important;
}

/* 카드 영역 */
.cards{ display:flex; justify-content:center; gap:30px; flex-wrap:wrap; margin-top: 50px; }
.card{ width:250px; padding:35px; border-radius:25px; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.18); backdrop-filter:blur(20px); }
.cardTitle{ color:white; font-size:25px; font-weight:700; margin-bottom:15px; }
.cardText{ color:#ccc; font-size:15px; }
</style>
""", unsafe_allow_html=True)

# 페이지 구조 시작
st.markdown('<div class="full-bg">', unsafe_allow_html=True)

st.markdown("""
    <div class="hero">
        <div class="logo">JESSICA</div>
        <div class="title">DETECTIVE</div>
        <div class="subtitle">AGENCY</div>
        <div class="desc">진실은 언제나 흔적을 남깁니다.<br>당신의 의뢰는 안전하게 보호됩니다.</div>
    </div>
""", unsafe_allow_html=True)

# 100% 정중앙 버튼 배치를 위한 컬럼 활용
_, col, _ = st.columns([1, 2, 1])
with col:
    if st.button("🔐 의뢰하기"):
        st.switch_page("pages/1_의뢰하기.py")

st.markdown("""
    <div class="cards">
        <div class="card"><div class="cardTitle">사람 찾기</div><div class="cardText">실종자 및 연락 두절 관련 상담 서비스를 제공합니다.</div></div>
        <div class="card"><div class="cardTitle">사실 조사</div><div class="cardText">공개 자료 기반 사실관계를 분석합니다.</div></div>
        <div class="card"><div class="cardTitle">디지털 분석</div><div class="cardText">디지털 자료 분석과 상담을 제공합니다.</div></div>
        <div class="card"><div class="cardTitle">기업 조사</div><div class="cardText">기업 관련 공개 정보를 분석합니다.</div></div>
    </div>
</div>
""", unsafe_allow_html=True)
