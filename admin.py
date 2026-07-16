import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# =========================
# 페이지 설정
# =========================

st.set_page_config(
    page_title="Jessica Admin",
    page_icon="🔐",
    layout="wide"
)


# =========================
# Firebase 연결
# =========================

if not firebase_admin._apps:

    cred = credentials.Certificate(
        "firebase_key.json"
    )

    firebase_admin.initialize_app(
        cred
    )


db = firestore.client()


# =========================
# CSS
# =========================

st.markdown("""
<style>

.stApp{

background:
linear-gradient(
180deg,
#050505,
#150025,
#050505
);

color:white;

}


h1,h2,h3{

color:#FFD369;

}


.card{

background:
rgba(255,255,255,.08);

padding:25px;

border-radius:20px;

margin-bottom:20px;

border:1px solid rgba(255,211,105,.4);

}


</style>
""",
unsafe_allow_html=True)



# =========================
# 제목
# =========================

st.title(
    "🔐 Jessica Detective Agency"
)

st.subheader(
    "관리자 의뢰 확인 시스템"
)


st.divider()



# =========================
# Firebase 데이터 가져오기
# =========================

requests = db.collection(
    "requests"
).stream()



data = []


for request in requests:

    item = request.to_dict()

    item["id"] = request.id

    data.append(item)



# =========================
# 출력
# =========================


if len(data) == 0:

    st.info(
        "현재 접수된 의뢰가 없습니다."
    )


else:

    st.success(
        f"총 {len(data)}개의 의뢰가 접수되었습니다."
    )


    for item in data:


        st.markdown(
            f"""
            <div class="card">

            <h3>
            🔎 {item.get('category','')}
            </h3>


            <b>의뢰인:</b>
            {item.get('name','')}
            <br><br>


            <b>연락처:</b>
            {item.get('contact','')}
            <br><br>


            <b>의뢰 내용:</b>
            <br>
            {item.get('detail','')}
            <br><br>


            <b>상태:</b>
            {item.get('status','')}


            </div>
            """,
            unsafe_allow_html=True
        )
