import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="✨ 반짝반짝 미니게임 천국 ✨", page_icon="🎨", layout="centered")

# --- 커스텀 스타일링 ---
st.markdown("""
    <style>
    .main {
        background-color: #fff0f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: 2px solid #ff85c0;
        background-color: #fff0f6;
        color: #eb2f96;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff85c0;
        color: white;
        transform: scale(1.05);
    }
    h1, h2, h3 {
        color: #eb2f96;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ 큐트 반짝 미니게임 ✨")
st.write("---")

# 사이드바 메뉴
menu = st.sidebar.selectbox("🎮 게임을 골라보세요!", ["🥠 포춘 쿠키", "🎡 룰렛 돌리기", "🪜 사다리 타기"])

# 1. 포춘 쿠키 게임
if menu == "🥠 포춘 쿠키":
    st.header("🥠 오늘의 행운 포춘 쿠키")
    st.write("쿠키를 열어 오늘 어떤 행운이 기다리는지 확인해봐요!")
    
    fortunes = [
        "오늘은 최고의 행운이 함께할 거예요! ✨",
        "달콤한 간식을 먹으면 기분이 좋아질지도? 🍰",
        "생각지도 못한 곳에서 기쁜 소식이 들려올 거예요!",
        "지금 가장 하고 싶은 일을 시작해보세요! 🚀",
        "반짝반짝 빛나는 하루가 당신을 기다려요 🌟"
    ]
    
    if st.button("쿠키 열기 🪄"):
        with st.spinner("두근두근..."):
            time.sleep(1)
            st.balloons()  # 반짝반짝 효과
            st.success(random.choice(fortunes))

# 2. 룰렛 게임
elif menu == "🎡 룰렛 돌리기":
    st.header("🎡 화려한 룰렛")
    items = st.text_input("추첨 항목을 쉼표(,)로 구분해서 적어주세요", "떡볶이, 케이크, 푸딩, 마카롱")
    
    if st.button("룰렛 돌리기!! 🍭"):
        item_list = [i.strip() for i in items.split(",")]
        if len(item_list) > 1:
            with st.empty():
                for _ in range(10):
                    pick = random.choice(item_list)
                    st.subheader(f"🎲 {pick}")
                    time.sleep(0.1)
            st.balloons()
            st.markdown(f"## 🎉 결과: **{pick}**")
        else:
            st.warning("항목을 2개 이상 입력해주세요!")

# 3. 사다리 게임 (심플 버전)
elif menu == "🪜 사다리 타기":
    st.header("🪜 간단 사다리 게임")
    names = st.text_input("참여 인원 (쉼표 구분)", "너구리, 토끼, 고양이")
    results = st.text_input("결과 항목 (쉼표 구분)", "당첨, 꽝, 다시")
    
    if st.button("사다리 결과 보기 🎀"):
        name_list = [n.strip() for n in names.split(",")]
        res_list = [r.strip() for r in results.split(",")]
        
        if len(name_list) == len(res_list):
            random.shuffle(res_list)
            final = dict(zip(name_list, res_list))
            for k, v in final.items():
                st.write(f"💖 **{k}** ───▶ **{v}**")
            st.snow()
        else:
            st.error("참여 인원과 결과 항목의 개수를 맞춰주세요!")
