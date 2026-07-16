import streamlit as st
import streamlit.components.v1 as components


# =========================
# 페이지 설정
# =========================

st.set_page_config(
    page_title="Jessica Detective Agency",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================
# Streamlit 기본 UI 제거
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


.main{

background:

linear-gradient(
180deg,
#050505 0%,
#090018 45%,
#050505 100%
);

}


</style>
""", unsafe_allow_html=True)



# =========================
# 전체 디자인 CSS
# =========================

st.markdown("""

<style>


@import url(
'https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Orbitron:wght@500;700&family=Noto+Sans+KR:wght@300;500;700&display=swap'
);



html,body{

background:#050505;

}





/* =====================
   HERO
===================== */


.hero{


min-height:100vh;


display:flex;


flex-direction:column;


justify-content:center;


align-items:center;



background:


radial-gradient(

ellipse at 50% 20%,

rgba(123,44,255,.35),

transparent 45%

),


radial-gradient(

ellipse at 50% 80%,

rgba(90,0,180,.25),

transparent 60%

),


linear-gradient(

180deg,

#050505,

#090018,

#050505

);



text-align:center;


position:relative;


overflow:hidden;


}




.logo{


font-family:'Orbitron';


font-size:22px;


letter-spacing:10px;


color:#FFD369;


margin-bottom:30px;


}





.title{


font-family:'Cinzel';


font-size:100px;


font-weight:700;


letter-spacing:15px;


color:white;


line-height:1;


text-shadow:

0 0 20px rgba(255,255,255,.3);



}





.subtitle{


font-family:'Orbitron';


font-size:38px;


letter-spacing:12px;


color:#9b55ff;


margin-top:20px;


margin-bottom:40px;


}





.desc{


font-family:'Noto Sans KR';


font-size:22px;


line-height:1.8;


color:#ddd;


}





/* =====================
   카드
===================== */


.cards{


display:flex;


justify-content:center;


gap:30px;


padding-top:100px;


padding-bottom:120px;


width:100%;



background:


radial-gradient(

circle at center,

rgba(123,44,255,.18),

transparent 60%

),


linear-gradient(

180deg,

transparent,

rgba(20,0,40,.9)

);



flex-wrap:wrap;


}





.card{


width:250px;


padding:35px;


border-radius:25px;



background:

rgba(255,255,255,.06);



border:

1px solid rgba(255,255,255,.15);



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


margin-bottom:20px;


}



.cardTitle{


font-family:'Noto Sans KR';


font-size:25px;


font-weight:700;


color:white;


margin-bottom:15px;


}




.cardText{


font-family:'Noto Sans KR';


font-size:15px;


line-height:1.7;


color:#ccc;


}


</style>


""", unsafe_allow_html=True)



# =========================
# 메인
# =========================


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


</div>

""", unsafe_allow_html=True)



# =========================
# 의뢰 버튼
# =========================


components.html(

"""

<style>


body{

margin:0;

background:transparent;

display:flex;

justify-content:center;

align-items:center;

height:130px;

}



.caseButton{


width:280px;

height:80px;



display:flex;


align-items:center;


justify-content:center;



position:relative;



border-radius:18px;



background:

linear-gradient(

135deg,

rgba(255,255,255,.15),

rgba(255,255,255,.03)

);



border:

1px solid #FFD369;



color:#FFD369;



font-family:'Noto Sans KR';



font-size:22px;



font-weight:700;



letter-spacing:4px;



overflow:hidden;



cursor:pointer;



box-shadow:


0 0 25px rgba(255,211,105,.3);



transition:.5s;



}




.caseButton::before{


content:"";

position:absolute;


top:0;


left:-120%;



width:70%;


height:100%;



background:

linear-gradient(

120deg,

transparent,

rgba(255,255,255,.9),

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



.caseButton:hover{


transform:translateY(-6px);



color:white;



border-color:#7B2CFF;



box-shadow:


0 0 40px #7B2CFF,


0 0 90px rgba(123,44,255,.6);


}



</style>



<div class="caseButton">

🔐 의뢰하기

</div>


""",

height=130

)



# =========================
# 서비스 카드
# =========================


st.markdown("""

<div class="cards">


<div class="card">

<div class="icon">🔍</div>

<div class="cardTitle">

사람 찾기

</div>


<div class="cardText">

실종자 및 연락 두절 관련<br>

상담 서비스를 제공합니다.

</div>

</div>



<div class="card">

<div class="icon">📁</div>

<div class="cardTitle">

사실 조사

</div>


<div class="cardText">

공개 자료 기반<br>

사실관계를 분석합니다.

</div>

</div>



<div class="card">

<div class="icon">💻</div>

<div class="cardTitle">

디지털 분석

</div>


<div class="cardText">

디지털 자료 분석과<br>

상담을 제공합니다.

</div>

</div>



<div class="card">

<div class="icon">🏢</div>

<div class="cardTitle">

기업 조사

</div>


<div class="cardText">

기업 관련 공개 정보를<br>

분석합니다.

</div>

</div>


</div>

""", unsafe_allow_html=True)
