import streamlit as st

st.set_page_config(page_title="Jessica Detective Agency", layout="wide", initial_sidebar_state="collapsed")

# 1. 스타일을 완벽하게 적용하기 위해 head 태그 주입 및 구조 재설계
st.markdown("""
<style>
    /* 전체 배경을 stApp에서 직접 강제 설정하여 짤림 방지 */
    .stApp {
        background: radial-gradient(ellipse at 50% 10%, rgba(123,44,255,.4), transparent 45%),
                    radial-gradient(ellipse at 50% 70%, rgba(90,0,180,.25), transparent 55%),
                    linear-gradient(180deg, #050505, #100020, #050505) !important;
        background-attachment: fixed !important;
    }
    
    /* 레이아웃 초기화 */
    [data-testid="stSidebar"], header, footer, #MainMenu { display: none !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* 히어로 섹션 */
    .hero-container { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 60vh; }
    
    /* 버튼 중앙 배치: 부모 컨테이너를 이용한 명시적 중앙 정렬 */
    .btn-container { display: flex; justify-content: center; margin-bottom: 50px; }
    div.stButton > button {
        width: 280px !important; height: 65px !important;
        background: linear-gradient(135deg, #4A1291, #1A0033) !important;
        border: 2px solid #7B2CFF !important; color: #E2D5F5 !important;
        font-weight: 700 !important; border-radius: 50px !important;
        font-size: 19px !important;
    }

    /* 카드 */
    .cards { display: flex; justify-content: center; gap: 30px; }
</style>
""", unsafe_allow_html=True)

# 페이지 구성
st.markdown("""
    <div class="hero-container">
        <div style="font-family:'Orbitron'; color:#FFD369; letter-spacing:12px;">JESSICA</div>
        <div style="font-family:'Cinzel'; font-size:100px; color:white;">DETECTIVE</div>
        <div style="font-family:'Orbitron'; font-size:38px; color:#9b55ff;">AGENCY</div>
    </div>
""", unsafe_allow_html=True)

# 버튼 강제 중앙 정렬
st.markdown('<div class="btn-container">', unsafe_allow_html=True)
if st.button("🔐 의뢰하기"):
    st.switch_page("pages/1_의뢰하기.py")
st.markdown('</div>', unsafe_allow_html=True)
