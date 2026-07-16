import streamlit as st

st.set_page_config(
    page_title="Jessica Detective Agency",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="stSidebar"]{ display:none; }
#MainMenu{ visibility:hidden; }
footer{ visibility:hidden; }
header{ visibility:hidden; }
.block-container{ padding:0; }

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Orbitron:wght@500;700&family=Noto+Sans+KR:wght@300;500;700&display=swap');
html,body{ background:#050505; }

.page{
    background: radial-gradient(ellipse at 50% 10%, rgba(123,44,255,.4), transparent 45%),
                radial-gradient(ellipse at 50% 70%, rgba(90,0,180,.25), transparent 55%),
                linear-gradient(180deg, #050505, #100020, #050505);
    min-height:100vh; padding-bottom:80px;
}
.hero{ height:60vh; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; }
.logo{ font-family:'Orbitron'; font-size:22px; letter-spacing:12px; color:#FFD369; margin-bottom:20px; }
.title{ font-family:'Cinzel'; font-size:100px; letter-spacing:18px; color:white; text-shadow:0 0 25px rgba(255,255,255,.5); }
.subtitle{ font-family:'Orbitron'; font-size:38px; letter-spacing:12px; color:#9b55ff; margin-top:10px; margin-bottom:20px; }
.desc{ font-family:'Noto Sans KR'; font-size:22px; line-height:1.8; color:#ddd; margin-bottom: 30px;}

.cards{ display:flex; justify-content:center; gap:30px; flex-wrap:wrap; margin-top: 50px; }
.card{ width:250px; padding:35px; border-radius:25px; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.18); backdrop-filter:blur(20px); transition:.4s; }
.card:hover{ transform:translateY(-12px); border-color:#7B2CFF; box-shadow:0 0 40px rgba(123,44,255,.7); }
.icon{ font-size:55px; margin-bottom:20px; }
.cardTitle{ font-family:'Noto Sans KR'; font-size:25px; font-weight:700; color:white; margin-bottom:15px; }
.cardText{ font-family:'Noto Sans KR'; font-size:15px; line-height:1.7; color:#ccc; }

/* 버튼 디자인 */
div[data-testid="stButton"] button {
    width: 280px !important; height: 70px !important; border-radius: 18px !important;
    background: linear-gradient(135deg, rgba(255,255,255,.15), rgba(255,255,255,.03)) !important;
    border: 1px solid #FFD369 !important; color: #FFD369 !important;
    font-family: 'Noto Sans KR'; font-size: 20px !important; font-weight: 700 !important;
    letter-spacing: 2px !important; box-shadow: 0 0 15px rgba(255,211,105,.2);
}
</style>
""", unsafe_allow_html=True)

# 1. 페이지 전체 감싸기 시작
st.markdown('<div class="page">', unsafe_allow_html=True)

# 2. 히어로 영역
st.markdown("""
    <div class="hero">
        <div class="logo">JESSICA</div>
        <div class="title">DETECTIVE</div>
        <div class="subtitle">AGENCY</div>
        <div class="desc">진실은 언제나 흔적을 남깁니다.<br>당신의 의뢰는 안전하게 보호됩니다.</div>
    </div>
""", unsafe_allow_html=True)

# 3. 버튼 (여기가 중요: markdown 밖에서 생성해야 확실히 보임)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🔐 의뢰하기"):
        st.switch_page("pages/1_의뢰하기.py")

# 4. 카드 영역
st.markdown("""
    <div class="cards">
        <div class="card"><div class="icon">🔍</div><div class="cardTitle">사람 찾기</div><div class="cardText">실종자 및 연락 두절 관련<br>상담 서비스를 제공합니다.</div></div>
        <div class="card"><div class="icon">📁</div><div class="cardTitle">사실 조사</div><div class="cardText">공개 자료 기반<br>사실관계를 분석합니다.</div></div>
        <div class="card"><div class="icon">💻</div><div class="cardTitle">디지털 분석</div><div class="cardText">디지털 자료 분석과<br>상담을 제공합니다.</div></div>
        <div class="card"><div class="icon">🏢</div><div class="cardTitle">기업 조사</div><div class="cardText">기업 관련 공개 정보를<br>분석합니다.</div></div>
    </div>
</div>
""", unsafe_allow_html=True)
