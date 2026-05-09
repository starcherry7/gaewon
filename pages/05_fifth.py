st.header("💖 두근두근 이름 궁합")
st.write("서로의 이름을 입력해서 매칭 점수를 확인해보세요!")

    col1, col2 = st.columns(2)
    with col1:
        name1 = st.text_input("첫 번째 이름", placeholder="이름 입력")
    with col2:
        name2 = st.text_input("두 번째 이름", placeholder="이름 입력")

    if st.button("궁합 분석 시작! ✨"):
        if name1 and name2:
            # 이름 궁합 계산 연출 (실제 로직은 랜덤이나 획수 기반으로 가능)
            # 여기서는 재미를 위해 이름 길이를 조합한 랜덤 시드를 활용합니다.
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for percent_complete in range(100):
                time.sleep(0.02)
                progress_bar.progress(percent_complete + 1)
                status_text.text(f"분석 중... {percent_complete + 1}%")
            
            # 고정된 결과를 위해 두 이름의 합을 시드로 사용
            random.seed(len(name1) + len(name2) + ord(name1[0]) + ord(name2[0]))
            score = random.randint(50, 100)
            
            st.write("---")
            st.subheader(f"✨ {name1} ❤️ {name2} ✨")
            
            # 점수별 메시지
            if score >= 90:
                st.balloons()
                st.success(f"결과: **{score}%** - 운명적인 사이! 놓치지 마세요! 💍")
            elif score >= 70:
                st.success(f"결과: **{score}%** - 아주 잘 어울리는 예쁜 커플이네요! 🌸")
            else:
                st.info(f"결과: **{score}%** - 조금 더 친해질 시간이 필요해요! 🍭")
        else:
            st.warning("두 사람의 이름을 모두 입력해 주세요!")
