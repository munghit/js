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

/* =========================
   Jessica 의뢰하기 버튼
========================= */

.mainButton{

display:flex !important;

width:280px !important;
height:80px !important;

align-items:center !important;
justify-content:center !important;

position:relative;

box-sizing:border-box;

margin:auto;

border-radius:18px;

background:

linear-gradient(
135deg,
rgba(255,255,255,0.15),
rgba(255,255,255,0.03)
);


border:1px solid rgba(255,211,105,0.9);


color:#FFD369 !important;

font-family:'Noto Sans KR', sans-serif;

font-size:22px !important;

font-weight:700;

letter-spacing:4px;


text-decoration:none !important;


overflow:hidden;


backdrop-filter:blur(20px);


box-shadow:

0 0 25px rgba(255,211,105,0.25);


transition:.5s;

}



/* 링크 기본 스타일 제거 */

.mainButton,
.mainButton:hover,
.mainButton:visited,
.mainButton:active{

text-decoration:none !important;

}



/* 글자 */

.mainButton span{

position:relative;

z-index:10;

display:block;

color:#FFD369 !important;

white-space:nowrap;

}



/* 지나가는 빛 */

.mainButton::before{


content:"";

position:absolute;


top:0;

left:-120%;


width:60%;

height:100%;


background:

linear-gradient(
120deg,
transparent,
rgba(255,255,255,0.8),
transparent
);


transform:skewX(-25deg);


animation:shine 3s infinite;


}




@keyframes shine{


0%{

left:-120%;

}


40%{

left:130%;

}


100%{

left:130%;

}


}





.mainButton:hover{


transform:translateY(-6px);


border-color:#7B2CFF;


box-shadow:

0 0 35px #7B2CFF,
0 0 80px rgba(123,44,255,.6);


}



.mainButton:hover span{


color:white !important;


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
