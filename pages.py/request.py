import streamlit as st


# =========================
# 페이지 설정
# =========================

st.set_page_config(
    page_title="의뢰하기 | Jessica Detective Agency",
    page_icon="🔐",
    layout="wide"
)



# =========================
# 기본 설정
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

padding-top:0;

}



.stApp{


background:


radial-gradient(

ellipse at 50% 10%,

rgba(123,44,255,.45),

transparent 45%

),



radial-gradient(

ellipse at 50% 80%,

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


}



</style>
""", unsafe_allow_html=True)



# =========================
# 디자인
# =========================

st.markdown("""
<style>


@import url(
'https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Noto+Sans+KR:wght@300;500;700&display=swap'
);



.container{


max-width:900px;

margin:auto;

padding-top:80px;

}



.logo{


font-family:'Cinzel';

font-size:65px;

letter-spacing:10px;

color:white;

text-align:center;

text-shadow:

0 0 30px rgba(255,255,255,.4);

}



.sub{


text-align:center;

font-family:'Noto Sans KR';

font-size:24px;

color:#9b55ff;

margin-top:20px;

margin-bottom:60px;

}



.box{


background:

rgba(255,255,255,.08);


border:

1px solid rgba(255,255,255,.2);


border-radius:30px;


padding:45px;


backdrop-filter:blur(20px);


box-shadow:

0 0 40px rgba(123,44,255,.25);


}



label{


color:#FFD369 !important;

font-weight:700;

}



.stTextInput input,
.stTextArea textarea,
.stSelectbox div{


background:

rgba(255,255,255,.08) !important;


color:white !important;


border-radius:12px !important;


}



.stButton button{


width:100%;


height:65px;


border-radius:18px;


background:


linear-gradient(

135deg,

rgba(255,211,105,.3),

rgba(123,44,255,.5)

);



border:1px solid #FFD369;



color:#FFD369;



font-size:22px;



font-weight:700;



letter-spacing:5px;



transition:.4s;


}



.stButton button:hover{


transform:translateY(-5px);



box-shadow:


0 0 40px #FFD369;


}


</style>
""", unsafe_allow_html=True)



# =========================
# 화면
# =========================

st.markdown("""
<div class="container">

<div class="logo">

JESSICA

</div>


<div class="sub">

CONFIDENTIAL REQUEST

</div>


<div class="box">

""", unsafe_allow_html=True)



st.markdown(
"""
### 🔐 의뢰 접수

당신의 요청은 철저하게 보호됩니다.
"""
)



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
    placeholder="조사하고 싶은 내용을 자세히 작성해주세요."
)



agree = st.checkbox(
    "개인정보 보호 및 의뢰 접수에 동의합니다."
)



if st.button("🔐 의뢰 접수하기"):

    if not agree:

        st.warning(
            "의뢰 접수를 위해 동의가 필요합니다."
        )

    elif name == "" or contact == "":

        st.warning(
            "이름과 연락 방법을 입력해주세요."
        )

    else:

        st.success(
            "의뢰가 안전하게 접수되었습니다."
        )



st.markdown(
"""
</div>

</div>
""",
unsafe_allow_html=True
)
