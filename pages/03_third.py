import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# 페이지 설정
st.set_page_config(page_title="Sleep Tracker", page_icon="🌙")

st.title("🌙 개인 수면 분석 대시보드")
st.markdown("수면 데이터를 기록하고 분석하여 최적의 패턴을 찾아보세요.")

# 사이드바: 데이터 입력
st.sidebar.header("오늘의 수면 기록")
date = st.sidebar.date_input("날짜", datetime.date.today())
sleep_time = st.sidebar.time_input("잠든 시간", datetime.time(23, 0))
wake_time = st.sidebar.time_input("일어난 시간", datetime.time(7, 0))
quality = st.sidebar.slider("수면 만족도 (1-10)", 1, 10, 7)

# 데이터 계산
def calculate_duration(start, end):
    start_dt = datetime.datetime.combine(datetime.date.today(), start)
    end_dt = datetime.datetime.combine(datetime.date.today(), end)
    if end_dt <= start_dt:
        end_dt += datetime.timedelta(days=1)
    duration = (end_dt - start_dt).seconds / 3600
    return round(duration, 1)

duration = calculate_duration(sleep_time, wake_time)

# --- 섹션 1: 수면 사이클 분석 ---
st.header("📊 수면 요약")
col1, col2, col3 = st.columns(3)
col1.metric("총 수면 시간", f"{duration}시간")
col2.metric("수면 만족도", f"{quality}/10")
col3.metric("수면 사이클", f"{round(duration * 60 / 90, 1)}회")

# 90분 사이클 조언 (6시간 = 4사이클)
if duration == 6.0:
    st.success("완벽한 4사이클(6시간) 수면입니다! 렘수면 상태에서 깨어날 확률이 적습니다.")
elif duration == 7.5:
    st.success("완벽한 5사이클(7.5시간) 수면입니다! 가장 권장되는 수면 시간입니다.")

# --- 섹션 2: 시각화 (예시 데이터 포함) ---
st.header("📈 주간 수면 트렌드")

# 실제 앱에서는 DB나 CSV에서 불러와야 하지만, 여기서는 예시 데이터를 생성합니다.
chart_data = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    'Hours': [6.5, 7.0, 6.0, 5.5, 8.0, 9.0, duration]
})

fig, ax = plt.subplots()
sns.barplot(x='Day', y='Hours', data=chart_data, palette="viridis", ax=ax)
ax.axhline(7.5, color='red', linestyle='--', label='Target (7.5h)')
plt.legend()
st.pyplot(fig)

# --- 섹션 3: 기상 시간 계산기 ---
st.header("⏰ 최적 기상 시간 계산기")
bedtime = st.time_input("언제 잠들 예정인가요?", datetime.time(23, 30))

st.write("90분 사이클을 고려한 추천 기상 시간:")
cycles = [4, 5, 6] # 6시간, 7.5시간, 9시간
cols = st.columns(len(cycles))

for i, c in enumerate(cycles):
    wake_at = (datetime.datetime.combine(datetime.date.today(), bedtime) + 
               datetime.timedelta(minutes=c*90 + 15)).time() # 잠드는 시간 15분 추가
    cols[i].button(f"{c}사이클 ({c*1.5}h)\n\n {wake_at.strftime('%H:%M')}")
