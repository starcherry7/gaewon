import streamlit as st
import streamlit.components.v1 as components

# 1. CSS 및 HTML 구조를 하나의 변수에 담습니다.
# 파이썬의 삼중 따옴표(""")를 사용하여 SyntaxError를 방지합니다.
html_code = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <style>
        :root {
            --bg: #ffffff;
            --text: #1d1d1f;
            --accent: #000000;
        }

        body {
            margin: 0;
            background-color: var(--bg);
            color: var(--text);
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            /* 에러가 났던 지점: 문자열 안에 있으므로 이제 안전합니다 */
            min-height: 100vh; 
        }

        #app {
            width: 100%;
            max-width: 450px;
            padding: 2rem;
            text-align: center;
        }

        .symbol {
            font-size: 5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #222, #888);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 1rem 0;
        }

        .btn {
            display: block;
            width: 100%;
            padding: 1.2rem;
            margin-bottom: 0.8rem;
            border: 1px solid #e1e1e3;
            background: #fcfcfc;
            border-radius: 14px;
            cursor: pointer;
            transition: 0.2s;
        }

        .btn:hover { background: #f5f5f7; border-color: #000; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div id="app">
        <div id="content">
            <h1 style="font-size: 2.5rem;">A-32</h1>
            <p>5개의 질문으로 당신의 고유 원소를 정의합니다.</p>
            <button class="btn" style="background: black; color: white; margin-top: 2rem;" onclick="start()">분석 시작</button>
        </div>
    </div>

    <script>
        const questions = [
            { q: "주말에 에너지를 얻는 방식은?", a: "사람들과 함께", b: "혼자만의 고요함", key: "E" },
            { q: "새로운 물건을 샀을 때 당신은?", a: "일단 만져본다", b: "설명서부터 읽는다", key: "S" },
            { q: "친구가 고민을 털어놓는다면?", a: "해결책 제시", b: "깊은 공감", key: "T" },
            { q: "여행을 떠나기 직전의 모습은?", a: "철저한 계획", b: "발길 닿는 대로", key: "J" },
            { q: "당신이 추구하는 삶의 태도는?", a: "강렬한 불꽃", b: "잔잔한 바다", key: "P" }
        ];

        let current = 0;
        let path = "";

        function start() { render(); }

        function render() {
            if (current < questions.length) {
                const q = questions[current];
                document.getElementById('content').innerHTML = `
                    <p style="color: #aaa;">STEP 0${current + 1}</p>
                    <p style="font-size: 1.2rem; margin-bottom: 1.5rem;">${q.q}</p>
                    <button class="btn" onclick="select('A')">${q.a}</button>
                    <button class="btn" onclick="select('B')">${q.b}</button>
                `;
            } else {
                showResult();
            }
        }

        function select(choice) {
            path += choice;
            current++;
            render();
        }

        function showResult() {
            const elements = ["수소","헬륨","리튬","베릴륨","붕소","탄소","질소","산소","플루오린","네온","나트륨","마그네슘","알루미늄","규소","인","황","염소","아르곤","칼륨","칼슘","스칸듐","티타늄","바나듐","크로뮴","망가니즈","철","코발트","니켈","구리","아연","갈륨","저마늄"];
            const idx = path.split('').reduce((a, b) => a + b.charCodeAt(0), 0) % 32;
            const res = elements[idx];
            document.getElementById('content').innerHTML = `
                <p>당신의 원소 바이브</p>
                <div class="symbol">${res}</div>
                <h2>원소 번호 ${idx + 1}</h2>
                <p style="line-height: 1.6; color: #555;">당신의 선택 패턴은 ${res}의 성질과 닮아있네요. 고유하고 특별한 에너지를 가졌습니다.</p>
                <button class="btn" onclick="location.reload()">다시 하기</button>
            `;
        }
    </script>
</body>
</html>
"""

# 2. 스트림릿에서 위 HTML 코드를 실행합니다.
st.set_page_config(page_title="Element Vibe", layout="centered")
components.html(html_code, height=600)
