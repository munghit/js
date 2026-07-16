import streamlit as st
import streamlit.components.v1 as components


# =========================
# 페이지 이동 함수
# =========================

def go_request():
    st.switch_page("pages/의뢰하기.py")



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



/* 숨김 버튼 */

div[data-testid="stButton"] button{

display:none;

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
