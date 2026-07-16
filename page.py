import streamlit as st

# ---------------------------------
# 페이지 설정
# ---------------------------------
st.set_page_config(
    page_title="Jessica Detective Agency",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 사이드바 숨기기
st.markdown("""
<style>
[data-testid="stSidebar"]{
    display:none;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

.block-container{
    padding-top:0rem;
    padding-bottom:0rem;
    padding-left:0rem;
    padding-right:0rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# 메인 CSS
# ---------------------------------

st.markdown("""

<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Orbitron:wght@500;700&family=Noto+Sans+KR:wght@300;500;700&display=swap');

html,body{

background:#050505;

overflow-x:hidden;

}

.main{

background:#050505;

}

/* ---------------- Hero ---------------- */

.hero{

height:100vh;

display:flex;

flex-direction:column;

justify-content:center;

align-items:center;

background:
radial-gradient(circle at center,
rgba(117,0,255,.22),
transparent 60%),
linear-gradient(#050505,#050505);

text-align:center;

}

/* 로고 */

.logo{

font-size:18px;

letter-spacing:6px;

color:white;

font-family:'Orbitron';

margin-bottom:30px;

}

/* 큰 제목 */

.title{

font-size:96px;

font-family:'Cinzel';

font-weight:700;

color:white;

letter-spacing:10px;

margin-bottom:10px;

}

/* 부제목 */

.subtitle{

font-size:30px;

font-family:'Orbitron';

color:#7B2CFF;

letter-spacing:8px;

margin-bottom:40px;

}

/* 설명 */

.desc{

font-size:22px;

font-family:'Noto Sans KR';

color:#dddddd;

margin-bottom:50px;

}

/* 버튼 */

.mainButton{

background:#7B2CFF;

padding:18px 60px;

border-radius:50px;

font-size:22px;

font-weight:bold;

color:white;

text-decoration:none;

transition:.4s;

box-shadow:0 0 25px #7B2CFF;

}

.mainButton:hover{

background:white;

color:#7B2CFF;

box-shadow:0 0 60px #7B2CFF;

}

/* 카드 */

.cards{

display:flex;

justify-content:center;

gap:30px;

margin-top:90px;

flex-wrap:wrap;

}

.card{

width:250px;

padding:30px;

border-radius:25px;

background:rgba(255,255,255,.05);

backdrop-filter:blur(20px);

border:1px solid rgba(255,255,255,.15);

transition:.4s;

}

.card:hover{

transform:translateY(-12px);

border:1px solid #7B2CFF;

box-shadow:0 0 35px rgba(123,44,255,.7);

}

.icon{

font-size:55px;

margin-bottom:15px;

}

.cardTitle{

font-size:26px;

font-weight:bold;

color:white;

margin-bottom:15px;

font-family:'Noto Sans KR';

}

.cardText{

font-size:16px;

color:#cccccc;

line-height:1.6;

font-family:'Noto Sans KR';

}

</style>

""", unsafe_allow_html=True)

# ---------------------------------
# HTML
# ---------------------------------

st.markdown("""

<div class="hero">

<div class="logo">

JESSICA

</div>

<div class="title">

DETECTIVE

</div>

<div class="subtitle">

AGENCY

</div>

<div class="desc">

진실은 언제나 흔적을 남깁니다.<br>

당신의 의뢰는 안전하게 보호됩니다.

</div>

<a href="#" class="mainButton">

의뢰하기

</a>

<div class="cards">

<div class="card">

<div class="icon">🔍</div>

<div class="cardTitle">

사람 찾기

</div>

<div class="cardText">

실종자 및 연락이 끊긴 사람을 찾기 위한<br>

합법적인 조사 서비스를 제공합니다.

</div>

</div>

<div class="card">

<div class="icon">📁</div>

<div class="cardTitle">

사실 조사

</div>

<div class="cardText">

공개 자료와 증거를 바탕으로<br>

사실관계를 분석합니다.

</div>

</div>

<div class="card">

<div class="icon">💻</div>

<div class="cardTitle">

디지털 분석

</div>

<div class="cardText">

디지털 자료와 기록에 대한<br>

분석 및 상담을 제공합니다.

</div>

</div>

<div class="card">

<div class="icon">🏢</div>

<div class="cardTitle">

기업 조사

</div>

<div class="cardText">

기업 및 계약 관련 공개 정보를<br>

조사하고 정리합니다.

</div>

</div>

</div>

</div>

""", unsafe_allow_html=True)
