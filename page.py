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

position:relative;

display:inline-flex;

align-items:center;

justify-content:center;

gap:15px;

padding:20px 75px;

border-radius:8px;

background:
linear-gradient(
135deg,
rgba(255,255,255,0.12),
rgba(255,255,255,0.03)
);

border:1px solid rgba(255,211,105,0.8);

color:#FFD369;

/* ⭐ 밑줄 제거 */
text-decoration:none !important;

font-family:'Orbitron';

font-size:18px;

letter-spacing:4px;

overflow:hidden;

transition:.5s;

backdrop-filter:blur(15px);

box-shadow:
0 0 20px rgba(255,211,105,.2);

}


/* 빛이 지나가는 효과 */

.mainButton::before{

content:"";

position:absolute;

top:0;

left:-120%;

width:100%;

height:100%;

background:

linear-gradient(
120deg,
transparent,
rgba(255,255,255,.6),
transparent
);

transition:.7s;

}



.mainButton:hover::before{

left:120%;

}



/* 마우스 올렸을 때 */

.mainButton:hover{

color:white;

border-color:#7B2CFF;

background:

rgba(123,44,255,.25);

box-shadow:

0 0 30px #7B2CFF,
0 0 70px rgba(123,44,255,.6);

transform:translateY(-5px);

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
