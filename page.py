import streamlit as st
import streamlit.components.v1 as components


# =========================
# 설정
# =========================

st.set_page_config(
    page_title="Jessica Detective Agency",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================
# 기본 제거
# =========================

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

padding:0;

}


</style>
""", unsafe_allow_html=True)



# =========================
# 전체 페이지 CSS
# =========================

st.markdown("""

<style>


@import url(
'https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Orbitron:wght@600&family=Noto+Sans+KR:wght@400;700&display=swap'
);



.page{


min-height:100vh;


background:


radial-gradient(
ellipse at 50% 15%,
rgba(123,44,255,.45),
transparent 40%
),


radial-gradient(
ellipse at 50% 55%,
rgba(100,0,200,.25),
transparent 55%
),


linear-gradient(
180deg,
#030303 0%,
#100020 45%,
#060008 100%
);



padding-bottom:120px;


}



/* HERO */


.hero{


height:650px;


display:flex;


flex-direction:column;


justify-content:center;


align-items:center;


text-align:center;


}




.logo{


font-family:'Orbitron';


font-size:22px;


letter-spacing:12px;


color:#FFD369;


margin-bottom:30px;


}





.title{


font-family:'Cinzel';


font-size:100px;


letter-spacing:18px;


color:white;


text-shadow:


0 0 30px rgba(255,255,255,.4);


}





.subtitle{


font-family:'Orbitron';


font-size:38px;


letter-spacing:12px;


color:#a56cff;


margin-top:20px;


margin-bottom:35px;


}




.desc{


font-family:'Noto Sans KR';


font-size:22px;


line-height:1.8;


color:#ddd;


}



/* 버튼 공간 */


.buttonArea{


display:flex;


justify-content:center;


margin-top:20px;


margin-bottom:100px;


}



/* 카드 */


.cards{


display:flex;


justify-content:center;


gap:35px;


flex-wrap:wrap;


padding:50px 0;


}




.card{


width:250px;


padding:35px;


border-radius:25px;


background:


rgba(255,255,255,.08);



border:

1px solid rgba(255,255,255,.18);



backdrop-filter:

blur(20px);



transition:.4s;


}





.card:hover{


transform:translateY(-12px);


border-color:#7B2CFF;


box-shadow:

0 0 40px rgba(123,44,255,.7);


}





.icon{


font-size:55px;


text-align:center;


}




.cardTitle{


color:white;


font-family:'Noto Sans KR';


font-size:25px;


font-weight:bold;


text-align:center;


margin:20px 0;


}




.cardText{


color:#ddd;


font-family:'Noto Sans KR';


text-align:center;


line-height:1.7;


}



</style>


""", unsafe_allow_html=True)




# =========================
# 전체 시작
# =========================


st.markdown("""
<div class="page">


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



</div>



<div class="buttonArea">

</div>


""", unsafe_allow_html=True)



# =========================
# 버튼
# =========================

components.html(
"""

<style>

body{

background:transparent;

margin:0;

display:flex;

justify-content:center;

align-items:center;

}



.caseButton{


width:280px;

height:80px;


display:flex;

align-items:center;

justify-content:center;



border-radius:18px;


position:relative;



background:

linear-gradient(
135deg,
rgba(255,255,255,.15),
rgba(255,255,255,.03)
);



border:1px solid #FFD369;


color:#FFD369;


font-family:'Noto Sans KR';


font-size:22px;


font-weight:bold;


letter-spacing:4px;



overflow:hidden;



box-shadow:

0 0 25px rgba(255,211,105,.3);



}



.caseButton:before{


content:"";


position:absolute;


left:-120%;


top:0;


width:70%;


height:100%;



background:

linear-gradient(
120deg,
transparent,
white,
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



</style>



<div class="caseButton">

🔐 의뢰하기

</div>


""",
height=120
)



# =========================
# 카드
# =========================

st.markdown("""

<div class="cards">


<div class="card">

<div class="icon">

🔍

</div>


<div class="cardTitle">

사람 찾기

</div>


<div class="cardText">

실종 및 연락 두절 관련<br>

상담 서비스를 제공합니다.

</div>


</div>




<div class="card">

<div class="icon">

📁

</div>


<div class="cardTitle">

사실 조사

</div>


<div class="cardText">

공개 자료 기반<br>

사실관계를 분석합니다.

</div>


</div>




<div class="card">

<div class="icon">

💻

</div>


<div class="cardTitle">

디지털 분석

</div>


<div class="cardText">

디지털 자료 분석과<br>

상담을 제공합니다.

</div>


</div>




<div class="card">

<div class="icon">

🏢

</div>


<div class="cardTitle">

기업 조사

</div>


<div class="cardText">

기업 관련 공개 정보를<br>

분석합니다.

</div>


</div>


</div>


</div>

""", unsafe_allow_html=True)
