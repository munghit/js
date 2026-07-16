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
# 기본 UI 제거
# =========================

st.markdown("""
<style>

#MainMenu{
display:none;
}

header{
display:none;
}

footer{
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
rgba(123,44,255,.45),
transparent 45%
),


radial-gradient(
ellipse at 50% 70%,
rgba(90,0,180,.3),
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
# 전체 CSS
# =========================

st.markdown("""
<style>


@import url(
'https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Orbitron:wght@500;700&family=Noto+Sans+KR:wght@300;500;700&display=swap'
);



/* HERO */

.hero{

height:85vh;

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






/* 카드 */


.cards{


display:flex;


justify-content:center;


gap:30px;


flex-wrap:wrap;


margin-bottom:150px;


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






/* 의뢰 영역 */


.request-box{


width:70%;


margin:auto;


padding:50px;


border-radius:30px;



background:


rgba(255,255,255,.08);



border:


1px solid rgba(255,211,105,.5);



backdrop-filter:blur(25px);



box-shadow:


0 0 50px rgba(123,44,255,.35);


}





.request-title{


text-align:center;


font-family:'Cinzel';


font-size:55px;


color:#FFD369;


letter-spacing:8px;


margin-bottom:20px;


}




.request-desc{


text-align:center;


font-family:'Noto Sans KR';


font-size:20px;


color:#ddd;


margin-bottom:40px;


}






/* 입력창 */


.stTextInput input,
.stTextArea textarea,
.stSelectbox div{


background:

rgba(255,255,255,.1)!important;


color:white!important;


border-radius:12px!important;


}





label{


color:#FFD369!important;


font-size:17px!important;


font-weight:700!important;


}






/* 버튼 */


.stButton button{


width:100%;


height:65px;


border-radius:18px;


background:


linear-gradient(

135deg,

rgba(255,211,105,.35),

rgba(123,44,255,.55)

);



border:


1px solid #FFD369;



color:#FFD369;



font-size:22px;



font-weight:700;



letter-spacing:5px;


}




</style>
""", unsafe_allow_html=True)





# =========================
# 메인 HERO
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
# 서비스 카드
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

""", unsafe_allow_html=True)





# =========================
# 의뢰하기 영역
# =========================


st.markdown("""
<div class="request-box">


<div class="request-title">

REQUEST

</div>


<div class="request-desc">

🔐 의뢰하기<br><br>

당신의 의뢰 내용은 안전하게 보호됩니다.

</div>


</div>
""", unsafe_allow_html=True)



st.write("")



# =========================
# 입력
# =========================


category = st.selectbox(
    "의뢰 유형",
    [
        "사람 찾기",
        "사실 조사",
        "디지털 분석",
        "기업 조사",
        "기타"
    ]
)



name = st.text_input(
    "의뢰인 이름"
)



contact = st.text_input(
    "연락 방법"
)



detail = st.text_area(
    "의뢰 내용",
    height=200,
    placeholder="상세한 의뢰 내용을 입력해주세요."
)



agree = st.checkbox(
    "개인정보 보호 및 의뢰 접수에 동의합니다."
)





# =========================
# 접수 버튼
# =========================


if st.button("🔐 의뢰 접수하기"):


    if not agree:


        st.warning(
            "개인정보 보호 및 의뢰 접수 동의가 필요합니다."
        )



    elif name == "" or contact == "":


        st.warning(
            "의뢰인 이름과 연락 방법을 입력해주세요."
        )



    else:


        st.markdown("""
        <div style="

        margin-top:40px;

        padding:35px;

        border-radius:30px;


        background:

        linear-gradient(

        135deg,

        rgba(255,211,105,.25),

        rgba(123,44,255,.45)

        );


        border:1px solid #FFD369;


        box-shadow:

        0 0 40px rgba(255,211,105,.5);


        text-align:center;


        font-family:'Noto Sans KR';


        ">



        <div style="

        font-size:50px;

        margin-bottom:15px;

        ">

        🔐

        </div>




        <div style="

        font-size:30px;

        font-weight:700;

        color:#FFD369;

        ">

        의뢰가 접수되었습니다

        </div>




        <div style="

        margin-top:20px;

        font-size:18px;

        color:white;

        line-height:1.8;

        ">


        Jessica Detective Agency가<br>

        의뢰 내용을 안전하게 확인하겠습니다.<br>

        빠른 시일 내에 연락드리겠습니다.


        </div>



        </div>

        """, unsafe_allow_html=True)
