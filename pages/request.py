import streamlit as st


# =========================
# 페이지 설정
# =========================

st.set_page_config(
    page_title="Jessica Detective Agency | Request",
    page_icon="🔐",
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

ellipse at 50% 80%,

rgba(90,0,180,.35),

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
'https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family
