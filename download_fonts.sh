#!/bin/bash

# ===========================================
# 한글 폰트 TTF 다운로드 스크립트
# Google Fonts에서 인기 한글 폰트 다운로드
# ===========================================

FONT_DIR="./fonts"
mkdir -p "$FONT_DIR"

echo "=========================================="
echo "  한글 폰트 TTF 다운로드 시작"
echo "=========================================="
echo ""

# 다운로드 함수
download_font() {
    local url="$1"
    local filename="$2"

    echo "📥 다운로드 중: $filename"

    if curl -L -s -o "$FONT_DIR/$filename" "$url"; then
        echo "   ✅ 완료: $filename"
    else
        echo "   ❌ 실패: $filename"
    fi
}

# Google Fonts GitHub 저장소 기반 URL
BASE_URL="https://github.com/google/fonts/raw/main"

echo "[ 1/17 ] Noto Sans KR (본고딕)"
download_font "$BASE_URL/ofl/notosanskr/NotoSansKR%5Bwght%5D.ttf" "NotoSansKR-Variable.ttf"

echo "[ 2/17 ] Noto Serif KR (본명조)"
download_font "$BASE_URL/ofl/notoserifkr/NotoSerifKR%5Bwght%5D.ttf" "NotoSerifKR-Variable.ttf"

echo "[ 3/17 ] Black Han Sans (검은고딕)"
download_font "$BASE_URL/ofl/blackhansans/BlackHanSans-Regular.ttf" "BlackHanSans-Regular.ttf"

echo "[ 4/17 ] Do Hyeon (도현)"
download_font "$BASE_URL/ofl/dohyeon/DoHyeon-Regular.ttf" "DoHyeon-Regular.ttf"

echo "[ 5/17 ] Jua (주아)"
download_font "$BASE_URL/ofl/jua/Jua-Regular.ttf" "Jua-Regular.ttf"

echo "[ 6/17 ] Gothic A1"
download_font "$BASE_URL/ofl/gothica1/GothicA1-Regular.ttf" "GothicA1-Regular.ttf"
download_font "$BASE_URL/ofl/gothica1/GothicA1-Bold.ttf" "GothicA1-Bold.ttf"
download_font "$BASE_URL/ofl/gothica1/GothicA1-Black.ttf" "GothicA1-Black.ttf"

echo "[ 7/17 ] Gugi (구기)"
download_font "$BASE_URL/ofl/gugi/Gugi-Regular.ttf" "Gugi-Regular.ttf"

echo "[ 8/17 ] Gaegu (개구)"
download_font "$BASE_URL/ofl/gaegu/Gaegu-Regular.ttf" "Gaegu-Regular.ttf"
download_font "$BASE_URL/ofl/gaegu/Gaegu-Bold.ttf" "Gaegu-Bold.ttf"

echo "[ 9/17 ] Hi Melody (하이멜로디)"
download_font "$BASE_URL/ofl/himelody/HiMelody-Regular.ttf" "HiMelody-Regular.ttf"

echo "[ 10/17 ] Poor Story (푸어스토리)"
download_font "$BASE_URL/ofl/poorstory/PoorStory-Regular.ttf" "PoorStory-Regular.ttf"

echo "[ 11/17 ] Single Day (싱글데이)"
download_font "$BASE_URL/ofl/singleday/SingleDay-Regular.ttf" "SingleDay-Regular.ttf"

echo "[ 12/17 ] Sunflower (선플라워)"
download_font "$BASE_URL/ofl/sunflower/Sunflower-Light.ttf" "Sunflower-Light.ttf"
download_font "$BASE_URL/ofl/sunflower/Sunflower-Medium.ttf" "Sunflower-Medium.ttf"
download_font "$BASE_URL/ofl/sunflower/Sunflower-Bold.ttf" "Sunflower-Bold.ttf"

echo "[ 13/17 ] Yeon Sung (연성)"
download_font "$BASE_URL/ofl/yeonsung/YeonSung-Regular.ttf" "YeonSung-Regular.ttf"

echo "[ 14/17 ] Nanum Gothic (나눔고딕)"
download_font "$BASE_URL/ofl/nanumgothic/NanumGothic-Regular.ttf" "NanumGothic-Regular.ttf"
download_font "$BASE_URL/ofl/nanumgothic/NanumGothic-Bold.ttf" "NanumGothic-Bold.ttf"
download_font "$BASE_URL/ofl/nanumgothic/NanumGothic-ExtraBold.ttf" "NanumGothic-ExtraBold.ttf"

echo "[ 15/17 ] Nanum Myeongjo (나눔명조)"
download_font "$BASE_URL/ofl/nanummyeongjo/NanumMyeongjo-Regular.ttf" "NanumMyeongjo-Regular.ttf"
download_font "$BASE_URL/ofl/nanummyeongjo/NanumMyeongjo-Bold.ttf" "NanumMyeongjo-Bold.ttf"
download_font "$BASE_URL/ofl/nanummyeongjo/NanumMyeongjo-ExtraBold.ttf" "NanumMyeongjo-ExtraBold.ttf"

echo "[ 16/17 ] Nanum Brush Script (나눔손글씨 붓)"
download_font "$BASE_URL/ofl/nanumbrushscript/NanumBrushScript-Regular.ttf" "NanumBrushScript-Regular.ttf"

echo "[ 17/17 ] Nanum Pen Script (나눔손글씨 펜)"
download_font "$BASE_URL/ofl/nanumpenscript/NanumPenScript-Regular.ttf" "NanumPenScript-Regular.ttf"

echo ""
echo "=========================================="
echo "  다운로드 완료!"
echo "=========================================="
echo ""
echo "📁 폰트 저장 위치: $FONT_DIR"
echo ""
echo "💡 사용 방법:"
echo "   1. fonts 폴더의 .ttf 파일을 더블클릭"
echo "   2. '설치' 버튼 클릭"
echo "   3. 한글, 엑셀, PPT 등에서 사용 가능!"
echo ""

# 다운로드된 파일 목록 표시
echo "📋 다운로드된 폰트 목록:"
ls -lh "$FONT_DIR"/*.ttf 2>/dev/null | awk '{print "   " $NF " (" $5 ")"}'

echo ""
echo "총 $(ls "$FONT_DIR"/*.ttf 2>/dev/null | wc -l)개의 폰트 파일"
