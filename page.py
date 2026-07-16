import streamlit as st


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
# 기본 설정
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
#050505,
#090018,
#050505
);

}



/* =========================
   버튼 중앙 정렬
========================= */


.stButton{

width:100% !important;

display:flex !important;

justify-content:center !important;

align-items:center !important;

margin-top:40px !important;

margin-bottom:100px !important;

}



.stButton > button{


width:280px !important;

height:80px !important;


border-radius:18px !important;


background:

linear-gradient(

135deg,

rgba(255,255,255,.15),

rgba(255,255,255,.03)

)!important;



border:

1px solid #FFD369 !important;



color:#FFD369 !important;



font-size:22px !important;


font-weight:700 !important;


letter-spacing:4px;



box-shadow:

0 0 25px rgba(255,211,105,.3);



transition:.5s;



}



.stButton > button:hover{


transform:translateY(-6px);


color:white !important;


border-color:#7B2CFF !important;



box-shadow:

0 0 40px #7B2CFF,

0 0 90px rgba(123,44,255,.6);


}



</style>

""", unsafe_allow_html=True)



# =========================
# 디자인
# =========================

st.markdown("""

<style>


@import url(
'https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Orbitron:wght@500;700&family=Noto+Sans+KR:wght@300;500;700&display=swap'
);



html,body{

background:#050505;

}



/* HERO */


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



/* 카드 */


.cards{


display:flex;


justify-content:center;


gap:30px;


padding:100px 0 120px;


width:100%;



background:


radial-gradient(

circle at center,

rgba(123,44,255,.18),

transparent 60%

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

if st.button(
    "🔐 의뢰하기",
    use_container_width=False
):

    st.switch_page(
        "pages/1_의뢰하기.py"
    )



# =========================
# 카드
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
