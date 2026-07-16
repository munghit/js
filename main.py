import streamlit as st

st.set_page_config(page_title="Jessica Detective Agency", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    /* 1. 스트림릿 기본값 강제 무효화 */
    [data-testid="stSidebar"], header, footer, #MainMenu { display: none !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; margin: 0 !important; }
    .stApp { background-color: #050505 !important; }

    /* 2. 전체 화면을 덮는 고정된 배경 */
    .full-page {
        width: 100vw;
        min-height: 100vh;
        background: radial-gradient(ellipse at 50% 10%, rgba(123,44,255,.4), transparent 45%),
                    radial-gradient(ellipse at 50% 70%, rgba(90,0,180,.25), transparent 55%),
                    linear-gradient(180deg, #050505, #100020, #050505);
        background-attachment: fixed;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 80px;
    }

    /* 3. 요소들 (제목, 버튼, 카드) 스타일 */
    .hero-text { text-align: center; color: white; margin-bottom: 30px; }
    .title { font-family: 'Cinzel'; font-size: 80px; letter-spacing: 10px; }
    .subtitle { font-family: 'Orbitron'; color: #9b55ff; font-size: 30px; letter-spacing: 8px; }
    
    /* 버튼을 중앙에 고정시키는 스타일 */
    .btn-wrap { margin: 30px 0; }
    div.stButton > button {
        width: 250px !important; height: 60px !important;
        background: linear-gradient(135deg, #4A1291, #1A0033) !important;
        border: 2px solid #7B2CFF !important; color: #E2D5F5 !important;
        font-weight: 700 !important; border-radius: 50px !important;
    }

    .cards { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; }
    .card { width: 220px; padding: 30px; border-radius: 20px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); text-align: center; color: white; }
</style>
""", unsafe_allow_html=True)

# HTML로 직접 전체 구조 생성 (Streamlit 레이아웃 영향 배제)
st.markdown('<div class="full-page">', unsafe_allow_html=True)
st.markdown("""
    <div class="hero-text">
        <div class="title">DETECTIVE</div>
        <div class="subtitle">AGENCY</div>
        <div style="color: #ddd; margin-top: 20px;">진실은 언제나 흔적을 남깁니다.</div>
    </div>
""", unsafe_allow_html=True)

# 버튼 (이것만 스트림릿 컴포넌트)
if st.button("🔐 의뢰하기"):
    st.switch_page("pages/1_의뢰하기.py")

# 카드 영역
st.markdown("""
    <div class="cards">
        <div class="card">사람 찾기</div>
        <div class="card">사실 조사</div>
        <div class="card">디지털 분석</div>
        <div class="card">기업 조사</div>
    </div>
</div>
""", unsafe_allow_html=True)
