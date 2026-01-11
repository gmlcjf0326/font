/**
 * 폰트랩 AI - 창의적인 폰트 스타일 갤러리
 * JavaScript 인터랙션 로직
 */

// 폰트 스타일 데이터
const fontStyles = [
    {
        id: 'neon-glow',
        name: '네온 글로우',
        category: 'retro',
        categoryLabel: '레트로',
        className: 'font-neon-glow',
        css: `font-family: 'Black Han Sans', sans-serif;
color: #fff;
text-shadow:
    0 0 5px #fff,
    0 0 10px #fff,
    0 0 20px #ff00de,
    0 0 30px #ff00de,
    0 0 40px #ff00de,
    0 0 55px #ff00de,
    0 0 75px #ff00de;`
    },
    {
        id: 'gradient-flow',
        name: '그라데이션 플로우',
        category: 'art',
        categoryLabel: '아트',
        className: 'font-gradient-flow',
        css: `font-family: 'Gothic A1', sans-serif;
font-weight: 900;
background: linear-gradient(90deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3, #ff6b6b);
background-size: 200% auto;
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
animation: gradient-shift 3s linear infinite;

@keyframes gradient-shift {
    0% { background-position: 0% center; }
    100% { background-position: 200% center; }
}`
    },
    {
        id: 'glitch',
        name: '사이버펑크 글리치',
        category: 'futuristic',
        categoryLabel: '미래적',
        className: 'font-glitch',
        hasDataText: true,
        css: `font-family: 'Do Hyeon', sans-serif;
position: relative;
color: #fff;
/* ::before와 ::after 의사 요소 필요 */
/* RGB 분리 및 글리치 효과 */`
    },
    {
        id: 'retro-sunset',
        name: '레트로 선셋',
        category: 'retro',
        categoryLabel: '레트로',
        className: 'font-retro-sunset',
        css: `font-family: 'Gugi', cursive;
background: linear-gradient(180deg, #ff6a00 0%, #ee0979 50%, #bd00ff 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
filter: drop-shadow(2px 2px 0 rgba(238, 9, 121, 0.3));`
    },
    {
        id: 'emboss',
        name: '3D 엠보스',
        category: '3d',
        categoryLabel: '3D',
        className: 'font-emboss',
        css: `font-family: 'Noto Sans KR', sans-serif;
font-weight: 900;
color: #e0e0e0;
text-shadow:
    -1px -1px 1px rgba(255,255,255,0.8),
    1px 1px 1px rgba(0,0,0,0.3),
    2px 2px 2px rgba(0,0,0,0.2),
    3px 3px 3px rgba(0,0,0,0.15);`
    },
    {
        id: 'chalk',
        name: '칠판 분필',
        category: 'handwriting',
        categoryLabel: '손글씨',
        className: 'font-chalk',
        css: `font-family: 'Gaegu', cursive;
font-weight: 700;
color: #fff;
text-shadow:
    0 0 5px #fff,
    0 0 2px rgba(255,255,255,0.8);
filter: blur(0.3px);
letter-spacing: 2px;`
    },
    {
        id: 'gold',
        name: '골드 럭셔리',
        category: 'classic',
        categoryLabel: '클래식',
        className: 'font-gold',
        css: `font-family: 'Noto Serif KR', serif;
font-weight: 700;
background: linear-gradient(180deg, #f9d423 0%, #e65c00 25%, #f9d423 50%, #e65c00 75%, #f9d423 100%);
background-size: 100% 200%;
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
animation: gold-shine 2s ease infinite;

@keyframes gold-shine {
    0%, 100% { background-position: 0% 0%; }
    50% { background-position: 0% 100%; }
}`
    },
    {
        id: 'comic',
        name: '만화 팝',
        category: 'art',
        categoryLabel: '아트',
        className: 'font-comic',
        css: `font-family: 'Jua', sans-serif;
color: #ffeb3b;
text-shadow:
    3px 3px 0 #ff5722,
    6px 6px 0 #e91e63,
    -1px -1px 0 #000,
    1px -1px 0 #000,
    -1px 1px 0 #000,
    1px 1px 0 #000;
letter-spacing: 2px;`
    },
    {
        id: 'fire',
        name: '불타는 텍스트',
        category: 'art',
        categoryLabel: '아트',
        className: 'font-fire',
        css: `font-family: 'Black Han Sans', sans-serif;
color: #fff;
text-shadow:
    0 0 4px #fff,
    0 -5px 4px #ff3,
    2px -10px 6px #fd3,
    -2px -15px 11px #f80,
    2px -25px 18px #f20;
animation: fire-flicker 0.15s infinite alternate;`
    },
    {
        id: 'ice',
        name: '얼음 크리스탈',
        category: 'art',
        categoryLabel: '아트',
        className: 'font-ice',
        css: `font-family: 'Gothic A1', sans-serif;
font-weight: 700;
background: linear-gradient(180deg, #e0f7fa 0%, #80deea 30%, #4dd0e1 70%, #00bcd4 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
filter: drop-shadow(0 0 8px rgba(77, 208, 225, 0.5));`
    },
    {
        id: 'hologram',
        name: '홀로그램',
        category: 'futuristic',
        categoryLabel: '미래적',
        className: 'font-hologram',
        css: `font-family: 'Do Hyeon', sans-serif;
background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
background-size: 400% 400%;
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
animation: hologram-shift 3s ease infinite;`
    },
    {
        id: 'newspaper',
        name: '빈티지 신문',
        category: 'classic',
        categoryLabel: '클래식',
        className: 'font-newspaper',
        css: `font-family: 'Noto Serif KR', serif;
font-weight: 600;
color: #2c2c2c;
text-shadow: 1px 1px 0 rgba(0,0,0,0.1);
letter-spacing: -1px;`
    },
    {
        id: 'typewriter',
        name: '타자기',
        category: 'classic',
        categoryLabel: '클래식',
        className: 'font-typewriter',
        css: `font-family: 'Poor Story', cursive;
color: #333;
text-shadow:
    1px 1px 0 rgba(0,0,0,0.2),
    0 0 1px rgba(0,0,0,0.3);
letter-spacing: 1px;`
    },
    {
        id: 'stencil',
        name: '스텐실',
        category: 'modern',
        categoryLabel: '모던',
        className: 'font-stencil',
        css: `font-family: 'Black Han Sans', sans-serif;
color: transparent;
-webkit-text-stroke: 2px currentColor;
letter-spacing: 4px;`
    },
    {
        id: 'rainbow-shadow',
        name: '레인보우 섀도우',
        category: 'art',
        categoryLabel: '아트',
        className: 'font-rainbow-shadow',
        css: `font-family: 'Jua', sans-serif;
color: #fff;
text-shadow:
    1px 1px 0 #ff0000,
    2px 2px 0 #ff7700,
    3px 3px 0 #ffdd00,
    4px 4px 0 #00ff00,
    5px 5px 0 #0077ff,
    6px 6px 0 #7700ff,
    7px 7px 0 #ff00ff;`
    },
    {
        id: 'elegant-serif',
        name: '우아한 세리프',
        category: 'classic',
        categoryLabel: '클래식',
        className: 'font-elegant-serif',
        css: `font-family: 'Noto Serif KR', serif;
font-weight: 400;
letter-spacing: 3px;
font-style: italic;`
    },
    {
        id: 'minimal-sans',
        name: '미니멀 산스',
        category: 'modern',
        categoryLabel: '모던',
        className: 'font-minimal-sans',
        css: `font-family: 'Noto Sans KR', sans-serif;
font-weight: 300;
letter-spacing: 6px;
text-transform: uppercase;`
    },
    {
        id: 'brush',
        name: '붓글씨',
        category: 'handwriting',
        categoryLabel: '손글씨',
        className: 'font-brush',
        css: `font-family: 'Nanum Brush Script', cursive;`
    },
    {
        id: 'calligraphy',
        name: '캘리그라피',
        category: 'handwriting',
        categoryLabel: '손글씨',
        className: 'font-calligraphy',
        css: `font-family: 'Nanum Pen Script', cursive;
letter-spacing: 1px;`
    },
    {
        id: 'sketchy',
        name: '스케치',
        category: 'handwriting',
        categoryLabel: '손글씨',
        className: 'font-sketchy',
        css: `font-family: 'Hi Melody', cursive;
letter-spacing: 1px;`
    },
    {
        id: 'arcade',
        name: '아케이드 픽셀',
        category: 'retro',
        categoryLabel: '레트로',
        className: 'font-arcade',
        css: `font-family: 'Do Hyeon', sans-serif;
color: #00ff00;
text-shadow:
    0 0 5px #00ff00,
    0 0 10px #00ff00,
    0 0 15px #00ff00;
letter-spacing: 3px;`
    },
    {
        id: 'deep-shadow',
        name: '딥 섀도우',
        category: '3d',
        categoryLabel: '3D',
        className: 'font-deep-shadow',
        css: `font-family: 'Gothic A1', sans-serif;
font-weight: 900;
color: #fff;
text-shadow:
    1px 1px 0 #ccc,
    2px 2px 0 #c9c9c9,
    3px 3px 0 #bbb,
    4px 4px 0 #b9b9b9,
    5px 5px 0 #aaa,
    6px 6px 1px rgba(0,0,0,.1);`
    },
    {
        id: 'neon-blue',
        name: '네온 블루',
        category: 'futuristic',
        categoryLabel: '미래적',
        className: 'font-neon-blue',
        css: `font-family: 'Gugi', cursive;
color: #fff;
text-shadow:
    0 0 5px #fff,
    0 0 10px #fff,
    0 0 20px #00b4ff,
    0 0 30px #00b4ff,
    0 0 40px #00b4ff,
    0 0 55px #00b4ff;
animation: neon-pulse 1.5s ease-in-out infinite alternate;`
    },
    {
        id: 'perspective',
        name: '원근감',
        category: '3d',
        categoryLabel: '3D',
        className: 'font-perspective',
        css: `font-family: 'Black Han Sans', sans-serif;
transform: perspective(500px) rotateX(15deg);
text-shadow:
    0 1px 0 #ccc,
    0 2px 0 #c9c9c9,
    0 3px 0 #bbb,
    0 4px 0 #b9b9b9,
    0 5px 0 #aaa;`
    },
    {
        id: 'watercolor',
        name: '수채화',
        category: 'art',
        categoryLabel: '아트',
        className: 'font-watercolor',
        css: `font-family: 'Nanum Myeongjo', serif;
font-weight: 700;
background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 50%, #a18cd1 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
filter: blur(0.3px);`
    }
];

// DOM 요소
const fontGrid = document.getElementById('fontGrid');
const searchInput = document.getElementById('searchInput');
const globalSampleText = document.getElementById('globalSampleText');
const fontSizeSlider = document.getElementById('fontSizeSlider');
const fontSizeValue = document.getElementById('fontSizeValue');
const categoryTabs = document.querySelectorAll('.category-tab');
const resultCount = document.getElementById('resultCount');
const themeToggle = document.getElementById('themeToggle');
const modalOverlay = document.getElementById('modalOverlay');
const modalClose = document.getElementById('modalClose');
const modalTitle = document.getElementById('modalTitle');
const cssCode = document.getElementById('cssCode');
const btnCopy = document.getElementById('btnCopy');
const toast = document.getElementById('toast');

// 현재 상태
let currentCategory = 'all';
let currentSearchTerm = '';
let currentFontSize = 40;
let currentSampleText = '안녕하세요';

// 초기화
function init() {
    renderFontCards();
    bindEvents();
    loadTheme();
}

// 이벤트 바인딩
function bindEvents() {
    // 검색
    searchInput.addEventListener('input', (e) => {
        currentSearchTerm = e.target.value.toLowerCase();
        filterAndRenderCards();
    });

    // 샘플 텍스트 변경
    globalSampleText.addEventListener('input', (e) => {
        currentSampleText = e.target.value || '안녕하세요';
        updateAllPreviews();
    });

    // 폰트 크기 변경
    fontSizeSlider.addEventListener('input', (e) => {
        currentFontSize = e.target.value;
        fontSizeValue.textContent = `${currentFontSize}px`;
        updateAllFontSizes();
    });

    // 카테고리 탭
    categoryTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            categoryTabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            currentCategory = tab.dataset.category;
            filterAndRenderCards();
        });
    });

    // 테마 토글
    themeToggle.addEventListener('click', toggleTheme);

    // 모달 닫기
    modalClose.addEventListener('click', closeModal);
    modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) closeModal();
    });

    // CSS 복사
    btnCopy.addEventListener('click', copyCSS);

    // 키보드 ESC로 모달 닫기
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeModal();
    });
}

// 폰트 카드 렌더링
function renderFontCards() {
    fontGrid.innerHTML = '';

    const filteredFonts = filterFonts();
    resultCount.textContent = filteredFonts.length;

    filteredFonts.forEach((font, index) => {
        const card = createFontCard(font, index);
        fontGrid.appendChild(card);
    });
}

// 폰트 필터링
function filterFonts() {
    return fontStyles.filter(font => {
        const matchesCategory = currentCategory === 'all' || font.category === currentCategory;
        const matchesSearch = font.name.toLowerCase().includes(currentSearchTerm) ||
                             font.categoryLabel.includes(currentSearchTerm);
        return matchesCategory && matchesSearch;
    });
}

// 필터링 후 렌더링
function filterAndRenderCards() {
    renderFontCards();
}

// 폰트 카드 생성
function createFontCard(font, index) {
    const card = document.createElement('div');
    card.className = 'font-card';
    card.style.animationDelay = `${index * 0.05}s`;

    const previewText = font.hasDataText
        ? `<span class="font-preview-text ${font.className}" data-text="${currentSampleText}" style="font-size: ${currentFontSize}px;">${currentSampleText}</span>`
        : `<span class="font-preview-text ${font.className}" style="font-size: ${currentFontSize}px;">${currentSampleText}</span>`;

    card.innerHTML = `
        <div class="font-card-header">
            <span class="font-name">${font.name}</span>
            <span class="font-category">${font.categoryLabel}</span>
        </div>
        <div class="font-preview">
            ${previewText}
        </div>
        <div class="font-card-footer">
            <button class="btn-css" data-font-id="${font.id}">
                <svg viewBox="0 0 24 24" width="14" height="14">
                    <path fill="currentColor" d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/>
                </svg>
                CSS 보기
            </button>
        </div>
    `;

    // CSS 보기 버튼 이벤트
    const btnCSS = card.querySelector('.btn-css');
    btnCSS.addEventListener('click', () => showCSSModal(font));

    return card;
}

// 모든 미리보기 텍스트 업데이트
function updateAllPreviews() {
    const previewTexts = document.querySelectorAll('.font-preview-text');
    previewTexts.forEach(text => {
        text.textContent = currentSampleText;
        if (text.hasAttribute('data-text')) {
            text.setAttribute('data-text', currentSampleText);
        }
    });
}

// 모든 폰트 크기 업데이트
function updateAllFontSizes() {
    const previewTexts = document.querySelectorAll('.font-preview-text');
    previewTexts.forEach(text => {
        text.style.fontSize = `${currentFontSize}px`;
    });
}

// CSS 모달 표시
function showCSSModal(font) {
    modalTitle.textContent = `${font.name} - CSS 코드`;
    cssCode.textContent = font.css;
    modalOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// 모달 닫기
function closeModal() {
    modalOverlay.classList.remove('active');
    document.body.style.overflow = '';
}

// CSS 복사
async function copyCSS() {
    const css = cssCode.textContent;

    try {
        await navigator.clipboard.writeText(css);
        showToast();
    } catch (err) {
        // 폴백: 구식 방법
        const textarea = document.createElement('textarea');
        textarea.value = css;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        showToast();
    }
}

// 토스트 표시
function showToast() {
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 2000);
}

// 테마 토글
function toggleTheme() {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';

    if (isDark) {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
}

// 테마 로드
function loadTheme() {
    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        document.documentElement.setAttribute('data-theme', 'dark');
    }
}

// 페이지 로드 시 초기화
document.addEventListener('DOMContentLoaded', init);
