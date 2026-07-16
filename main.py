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
# 기본 UI + 배경
# =========================

st.markdown("""
<style>

#MainMenu{
display:none;
}

footer{
display:none;
}

header{
display:none;
}


[data-testid="stSidebar"]{
display:none;
}


.block-container{
padding:0;
}



.stApp{


background:


radial-gradient(

ellipse at 50% 10%,

rgba(123,44,255,.4),

transparent 45%

),


radial-gradient(

ellipse at 50% 70%,

rgba(90,0,180,.25),

transparent 55%

),


linear-gradient(

180deg,

#050505,

#100020,

#050505

);



background-attachment:fixed;


min-height:100vh;


}

</style>
""", unsafe_allow_html=True)



# =========================
# 디자인 CSS
# =========================

st.markdown("""
<style>


@import url(
'https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Orbitron:wght@500;700&family=Noto+Sans+KR:wght@300;500;700&display=swap'
);



.page{

width:100%;

padding-bottom:180px;

}



.hero{


min-height:75vh;


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


0 0 25px rgba(255,255,255,.4);


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





.cards{


display:flex;


justify-content:center;


gap:30px;


flex-wrap:wrap;


}





.card{


width:250px;


padding:35px;


border-radius:25px;


background:

rgba(255,255,255,.07);



border:

1px solid rgba(255,255,255,.18);



backdrop-filter:blur(20px);



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


""", unsafe_allow_html=True)



# =========================
# 의뢰하기 버튼
# =========================

components.html(
"""

<style>

body{

margin:0;

background:transparent;

display:flex;

justify-content:center;

}



.btn{


width:300px;


height:75px;


display:flex;


align-items:center;


justify-content:center;



border-radius:20px;



background:


linear-gradient(

135deg,

rgba(255,211,105,.25),

rgba(123,44,255,.35)

);



border:

1px solid #FFD369;



color:#FFD369;



font-family:'Noto Sans KR';



font-size:24px;



font-weight:700;



letter-spacing:5px;



box-shadow:


0 0 25px rgba(255,211,105,.5);



cursor:pointer;



transition:.4s;


}



.btn:hover{


transform:

translateY(-8px)

scale(1.05);



box-shadow:


0 0 50px #FFD369,


0 0 100px rgba(123,44,255,.8);


}


</style>



<div

class="btn"

onclick="window.parent.location.href='/의뢰하기';"

>

🔐 의뢰하기

</div>


""",
height=120
)



st.markdown("""
</div>


<div class="cards">


<div class="card">

<div class="icon">

🔍

</div>

<div class="cardTitle">

사람 찾기

</div>

<div class="cardText">

실종자 및 연락 두절 관련<br>

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
