import streamlit as st

st.set_page_config(page_title="Jessica Detective Agency", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"]{ display:none; }
#MainMenu{ visibility:hidden; }
footer{ visibility:hidden; }
header{ visibility:hidden; }
.block-container{ padding:0 !important; max-width: none !important; }

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Orbitron:wght@500;700&family=Noto+Sans+KR:wght@300;500;700&display=swap');
html,body{ background:#050505; }

.page{
    background: radial-gradient(ellipse at 50% 10%, rgba(123,44,255,.4), transparent 45%),
                radial-gradient(ellipse at 50% 70%, rgba(90,0,180,.25), transparent 55%),
                linear-gradient(180deg, #050505, #100020, #050505);
    background-attachment: fixed;
    min-height: 100vh;
    padding-bottom: 80px;
    width: 100%;
}
.hero{ height:75vh; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; }
.logo{ font-family:'Orbitron'; font-size:22px; letter-spacing:12px; color:#FFD369; margin-bottom:30px; }
.title{ font-family:'Cinzel'; font-size:100px; letter-spacing:18px; color:white; text-shadow:0 0 25px rgba(255,255,255,.5); }
.subtitle{ font-family:'Orbitron'; font-size:38px; letter-spacing:12px; color:#9b55ff; margin-top:20px; margin-bottom:40px; }
.desc{ font-family:'Noto Sans KR'; font-size:22px; line-height:1.8; color:#ddd; margin-bottom:40px; }

/* 🌟 버튼 중앙 강제 배치 */
.button-container {
    display: flex;
    justify-content: center;
    margin-bottom: 50px;
}
div.stButton > button {
    width: 280px !important; height: 65px !important;
    background: linear-gradient(135deg, #4A1291, #1A0033) !important;
    color: #E2D5F5 !important; border: 2px solid #7B2CFF !important;
    font-weight: 700 !important; border-radius: 50px !important;
    font-size: 19px !important;
}

.cards{ display:flex; justify-content:center; gap:30px; flex-wrap:wrap; }
.card{ width:250px; padding:35px; border-radius:25px; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.18); backdrop-filter:blur(20px); transition:.4s; }
.card:hover{ transform:translateY(-12px); border-color:#7B2CFF; box-shadow:0 0 40px rgba(123,44,255,.7); }
.icon{ font-size:55px; margin-bottom:20px; }
.cardTitle{ font-family:'Noto Sans KR'; font-size:25px; font-weight:700; color:white; margin-bottom:15px; }
.cardText{ font-family:'Noto Sans KR'; font-size:15px; line-height:1.7; color:#ccc; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page">
    <div class="hero">
        <div class="logo">JESSICA</div>
        <div class="title">DETECTIVE</div>
        <div class="subtitle">AGENCY</div>
        <div class="desc">진실은 언제나 흔적을 남깁니다.<br>당신의 의뢰는 안전하게 보호됩니다.</div>
""", unsafe_allow_html=True)

# 🌟 HTML 컨테이너로 감싸 중앙 정렬 강제
st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button("🔐 의뢰하기"):
    st.switch_page("pages/1_의뢰하기.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="cards">
        <div class="card"><div class="icon">🔍</div><div class="cardTitle">사람 찾기</div><div class="cardText">실종자 및 연락 두절 관련<br>상담 서비스를 제공합니다.</div></div>
        <div class="card"><div class="icon">📁</div><div class="cardTitle">사실 조사</div><div class="cardText">공개 자료 기반<br>사실관계를 분석합니다.</div></div>
        <div class="card"><div class="icon">💻</div><div class="cardTitle">디지털 분석</div><div class="cardText">디지털 자료 분석과<br>상담을 제공합니다.</div></div>
        <div class="card"><div class="icon">🏢</div><div class="cardTitle">기업 조사</div><div class="cardText">기업 관련 공개 정보를<br>분석합니다.</div></div>
    </div>
</div>
""", unsafe_allow_html=True)
