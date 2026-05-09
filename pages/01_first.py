<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Element Vibe Check | 32 Elements</title>
    <style>
        /* 미니멀리즘 디자인 시스템 */
        :root {
            --bg: #ffffff;
            --surface: #fcfcfc;
            --text: #1d1d1f;
            --accent: #000000;
            --border: #e1e1e3;
        }

        body {
            margin: 0;
            background-color: var(--bg);
            color: var(--text);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow-x: hidden;
        }

        #app {
            width: 100%;
            max-width: 450px;
            padding: 2rem;
            text-align: center;
        }

        .fade-in {
            animation: fadeIn 0.8s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 { font-size: 1.5rem; font-weight: 600; margin-bottom: 2rem; letter-spacing: -0.05rem; }
        
        .question-box { margin-bottom: 2.5rem; }
        .question-box p { font-size: 1.1rem; margin-bottom: 1.5rem; line-height: 1.5; }

        .btn {
            display: block;
            width: 100%;
            padding: 1.2rem;
            margin-bottom: 0.8rem;
            border: 1px solid var(--border);
            background: var(--surface);
            border-radius: 14px;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.2s ease;
            color: var(--text);
        }

        .btn:hover {
            border-color: var(--accent);
            background: #f5f5f7;
        }

        /* 결과 화면 특별 스타일 */
        .symbol {
            font-size: 5rem;
            font-weight: 800;
            margin: 1rem 0;
            background: linear-gradient(135deg, #222, #888);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .atomic-number { font-size: 1.2rem; color: #aaa; font-family: monospace; }
        .desc { font-size: 0.95rem; color: #555; line-height: 1.7; margin-top: 1.5rem; padding: 0 1rem; }
        
        .hidden { display: none; }
    </style>
</head>
<body>

<div id="app" class="fade-in">
    <!-- 화면 단계별 컨테이너 -->
    <div id="content">
        <!-- 초기 화면 -->
        <div id="start-view">
            <h1 style="font-size: 2.5rem;">A-32</h1>
            <p>5개의 질문으로 당신의 고유 원소를 정의합니다.</p>
            <button class="btn" style="background: black; color: white; margin-top: 2rem;" onclick="nextStep()">분석 시작</button>
        </div>
    </div>
</div>

<script>
    // 1. 데이터 정의: 5가지 질문 (바이너리 선택형)
    const questions = [
        { q: "주말에 에너지를 얻는 방식은?", a: "사람들과 시끌벅적하게", b: "혼자만의 고요한 시간", key: "E" },
        { q: "새로운 물건을 샀을 때 당신은?", a: "설명서 없이 일단 만져본다", b: "원리나 설명서를 먼저 읽는다", key: "S" },
        { q: "친구가 고민을 털어놓는다면?", a: "현실적인 해결책을 제시한다", b: "깊이 공감하며 마음을 다독인다", key: "T" },
        { q: "여행을 떠나기 직전의 모습은?", a: "시간 단위로 짠 계획표가 있다", b: "발길 닿는 대로 갈 준비가 됐다", key: "J" },
        { q: "당신이 추구하는 삶의 태도는?", a: "강렬하고 화려한 불꽃", b: "잔잔하고 깊은 바다", key: "P" }
    ];

    // 2. 32가지 결과 데이터 (간략화를 위해 일부 예시 포함, 패턴에 따라 32개 조합 가능)
    // 5비트(2^5=32) 조합 생성기 기반
    const resultLib = {
        "ESTJA": { s: "Ti", n: "티타늄", d: "강력한 내구성과 효율성을 가진 당신은 조직의 핵심 골격 같은 존재입니다." },
        "INFPB": { s: "Xe", n: "제논", d: "희귀하고 고귀하며, 신비로운 분위기를 풍기는 당신은 쉽게 정의할 수 없는 예술가입니다." },
        "ENTJP": { s: "Au", n: "금", d: "가장 가치 있고 빛나는 리더십을 가졌습니다. 어떤 환경에서도 변치 않는 확신을 보여줍니다." },
        "ISFQA": { s: "O", n: "산소", d: "없어서는 안 될 필수적인 존재. 당신의 친절함은 주변 사람들을 숨 쉬게 합니다." },
        // ... 실제 배포시 32개 조합을 이 오브젝트에 매핑합니다.
        // 편의상 아래 로직에서 미등록 조합은 '미지의 원소'로 처리하거나 자동 생성합니다.
    };

    let currentQ = 0;
    let userPath = "";

    function nextStep() {
        if (currentQ < questions.length) {
            renderQuestion();
        } else {
            renderResult();
        }
    }

    function renderQuestion() {
        const qData = questions[currentQ];
        const html = `
            <div class="fade-in">
                <p class="atomic-number">STEP 0${currentQ + 1}</p>
                <div class="question-box">
                    <p>${qData.q}</p>
                    <button class="btn" onclick="select('A')">${qData.a}</button>
                    <button class="btn" onclick="select('B')">${qData.b}</button>
                </div>
            </div>
        `;
        document.getElementById('content').innerHTML = html;
    }

    function select(choice) {
        userPath += questions[currentQ].key + choice;
        currentQ++;
        nextStep();
    }

    function renderResult() {
        // 32개 조합이 없을 경우를 대비한 동적 생성 알고리즘
        const elementList = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge"];
        const hash = userPath.split('').reduce((a, b) => a + b.charCodeAt(0), 0) % 32;
        const finalSymbol = elementList[hash];

        document.getElementById('content').innerHTML = `
            <div class="fade-in">
                <p>당신을 정제한 결과</p>
                <div class="symbol">${finalSymbol}</div>
                <h2 id="el-name">원소 번호 ${hash + 1}</h2>
                <p class="desc">당신의 선택 패턴(${userPath})은 주기율표의 ${finalSymbol}과 완벽한 공명을 이룹니다. 이 원소는 당신의 성격처럼 독특하고 대체 불가능한 특성을 지니고 있습니다.</p>
                <button class="btn" style="margin-top: 2rem;" onclick="location.reload()">다시 측정하기</button>
            </div>
        `;
    }
</script>

</body>
</html>
