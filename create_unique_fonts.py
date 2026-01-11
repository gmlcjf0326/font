#!/usr/bin/env python3
"""
유니크한 커스텀 폰트 생성기 - 다양한 스타일
"""

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
import math

UNITS_PER_EM = 1000
ASCENDER = 800
DESCENDER = -200

# ============================================
# 공통 유틸리티
# ============================================

def create_basic_cmap():
    """기본 문자 매핑"""
    return {
        'space': 0x0020, 'exclam': 0x0021, 'numbersign': 0x0023,
        'comma': 0x002C, 'period': 0x002E,
        'zero': 0x0030, 'one': 0x0031, 'two': 0x0032, 'three': 0x0033,
        'four': 0x0034, 'five': 0x0035, 'six': 0x0036, 'seven': 0x0037,
        'eight': 0x0038, 'nine': 0x0039,
        'question': 0x003F, 'at': 0x0040,
        'A': 0x0041, 'B': 0x0042, 'C': 0x0043, 'D': 0x0044, 'E': 0x0045,
        'F': 0x0046, 'G': 0x0047, 'H': 0x0048, 'I': 0x0049, 'J': 0x004A,
        'K': 0x004B, 'L': 0x004C, 'M': 0x004D, 'N': 0x004E, 'O': 0x004F,
        'P': 0x0050, 'Q': 0x0051, 'R': 0x0052, 'S': 0x0053, 'T': 0x0054,
        'U': 0x0055, 'V': 0x0056, 'W': 0x0057, 'X': 0x0058, 'Y': 0x0059,
        'Z': 0x005A,
        'a': 0x0061, 'b': 0x0062, 'c': 0x0063, 'd': 0x0064, 'e': 0x0065,
        'f': 0x0066, 'g': 0x0067, 'h': 0x0068, 'i': 0x0069, 'j': 0x006A,
        'k': 0x006B, 'l': 0x006C, 'm': 0x006D, 'n': 0x006E, 'o': 0x006F,
        'p': 0x0070, 'q': 0x0071, 'r': 0x0072, 's': 0x0073, 't': 0x0074,
        'u': 0x0075, 'v': 0x0076, 'w': 0x0077, 'x': 0x0078, 'y': 0x0079,
        'z': 0x007A,
    }


def draw_glyph(pen, paths):
    """경로를 펜으로 그리기"""
    for path in paths:
        for item in path:
            cmd = item[0]
            if cmd == 'moveTo':
                pen.moveTo(item[1])
            elif cmd == 'lineTo':
                pen.lineTo(item[1])
            elif cmd == 'qCurveTo':
                if len(item) == 3:
                    pen.qCurveTo(item[1], item[2])
            elif cmd == 'closePath':
                pen.closePath()


def build_font(glyphs, font_name, family_name, output_path):
    """TTF 폰트 파일 생성"""
    glyph_order = ['.notdef'] + [g for g in glyphs.keys() if g != '.notdef']

    char_map = create_basic_cmap()
    cmap = {}
    for glyph_name, unicode_val in char_map.items():
        if glyph_name in glyphs:
            cmap[unicode_val] = glyph_name

    fb = FontBuilder(UNITS_PER_EM, isTTF=True)
    fb.setupGlyphOrder(glyph_order)
    fb.setupCharacterMap(cmap)

    pen_glyphs = {}
    for name, glyph_data in glyphs.items():
        pen = TTGlyphPen(None)
        draw_glyph(pen, glyph_data.get('paths', []))
        pen_glyphs[name] = pen.glyph()

    fb.setupGlyf(pen_glyphs)

    metrics = {}
    for name, glyph in glyphs.items():
        xMin = 0
        if hasattr(pen_glyphs[name], 'xMin') and pen_glyphs[name].xMin is not None:
            xMin = pen_glyphs[name].xMin
        metrics[name] = (glyph['width'], xMin)
    fb.setupHorizontalMetrics(metrics)

    fb.setupHorizontalHeader(ascent=ASCENDER, descent=DESCENDER)
    fb.setupHead(unitsPerEm=UNITS_PER_EM)

    fb.setupNameTable({
        'familyName': family_name,
        'styleName': 'Regular',
        'uniqueFontIdentifier': f'{family_name}-Regular',
        'fullName': f'{family_name} Regular',
        'version': 'Version 1.0',
        'psName': font_name,
    })

    fb.setupOS2(sTypoAscender=ASCENDER, sTypoDescender=DESCENDER,
                sCapHeight=700, sxHeight=500)
    fb.setupPost()

    fb.save(output_path)
    print(f"   ✅ {output_path}")


# ============================================
# 스타일 1: SharpEdge - 날카로운 각진 스타일
# ============================================

def create_sharp_font():
    """날카롭고 각진 미래적 폰트"""
    glyphs = {}

    glyphs['.notdef'] = {'width': 500, 'paths': [
        [('moveTo', (50, 0)), ('lineTo', (50, 700)), ('lineTo', (450, 700)),
         ('lineTo', (450, 0)), ('closePath', None)]
    ]}
    glyphs['space'] = {'width': 300, 'paths': []}

    # 대문자 - 날카로운 각도
    glyphs['A'] = {'width': 600, 'paths': [
        [('moveTo', (300, 700)), ('lineTo', (20, 0)), ('lineTo', (120, 0)),
         ('lineTo', (180, 150)), ('lineTo', (420, 150)), ('lineTo', (480, 0)),
         ('lineTo', (580, 0)), ('closePath', None)],
        [('moveTo', (220, 250)), ('lineTo', (380, 250)), ('lineTo', (300, 550)),
         ('closePath', None)]
    ]}

    glyphs['B'] = {'width': 550, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (380, 700)),
         ('lineTo', (480, 600)), ('lineTo', (480, 420)), ('lineTo', (400, 360)),
         ('lineTo', (500, 300)), ('lineTo', (500, 100)), ('lineTo', (400, 0)),
         ('closePath', None)],
        [('moveTo', (180, 400)), ('lineTo', (350, 400)), ('lineTo', (380, 450)),
         ('lineTo', (380, 550)), ('lineTo', (350, 600)), ('lineTo', (180, 600)),
         ('closePath', None)],
        [('moveTo', (180, 100)), ('lineTo', (370, 100)), ('lineTo', (400, 150)),
         ('lineTo', (400, 250)), ('lineTo', (370, 300)), ('lineTo', (180, 300)),
         ('closePath', None)]
    ]}

    glyphs['C'] = {'width': 550, 'paths': [
        [('moveTo', (480, 150)), ('lineTo', (380, 100)), ('lineTo', (200, 100)),
         ('lineTo', (80, 200)), ('lineTo', (80, 500)), ('lineTo', (200, 600)),
         ('lineTo', (380, 600)), ('lineTo', (480, 550)), ('lineTo', (480, 480)),
         ('lineTo', (380, 500)), ('lineTo', (220, 500)), ('lineTo', (180, 460)),
         ('lineTo', (180, 240)), ('lineTo', (220, 200)), ('lineTo', (380, 200)),
         ('lineTo', (480, 220)), ('closePath', None)]
    ]}

    glyphs['D'] = {'width': 580, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (350, 700)),
         ('lineTo', (500, 550)), ('lineTo', (500, 150)), ('lineTo', (350, 0)),
         ('closePath', None)],
        [('moveTo', (180, 100)), ('lineTo', (320, 100)), ('lineTo', (400, 180)),
         ('lineTo', (400, 520)), ('lineTo', (320, 600)), ('lineTo', (180, 600)),
         ('closePath', None)]
    ]}

    glyphs['E'] = {'width': 500, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (460, 700)),
         ('lineTo', (460, 600)), ('lineTo', (180, 600)), ('lineTo', (180, 400)),
         ('lineTo', (400, 400)), ('lineTo', (400, 300)), ('lineTo', (180, 300)),
         ('lineTo', (180, 100)), ('lineTo', (460, 100)), ('lineTo', (460, 0)),
         ('closePath', None)]
    ]}

    glyphs['F'] = {'width': 480, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (440, 700)),
         ('lineTo', (440, 600)), ('lineTo', (180, 600)), ('lineTo', (180, 400)),
         ('lineTo', (380, 400)), ('lineTo', (380, 300)), ('lineTo', (180, 300)),
         ('lineTo', (180, 0)), ('closePath', None)]
    ]}

    glyphs['G'] = {'width': 580, 'paths': [
        [('moveTo', (500, 150)), ('lineTo', (400, 100)), ('lineTo', (180, 100)),
         ('lineTo', (80, 200)), ('lineTo', (80, 500)), ('lineTo', (180, 600)),
         ('lineTo', (420, 600)), ('lineTo', (500, 520)), ('lineTo', (400, 500)),
         ('lineTo', (200, 500)), ('lineTo', (180, 480)), ('lineTo', (180, 220)),
         ('lineTo', (200, 200)), ('lineTo', (380, 200)), ('lineTo', (400, 220)),
         ('lineTo', (400, 300)), ('lineTo', (300, 300)), ('lineTo', (300, 380)),
         ('lineTo', (500, 380)), ('closePath', None)]
    ]}

    glyphs['H'] = {'width': 580, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (180, 700)),
         ('lineTo', (180, 400)), ('lineTo', (400, 400)), ('lineTo', (400, 700)),
         ('lineTo', (500, 700)), ('lineTo', (500, 0)), ('lineTo', (400, 0)),
         ('lineTo', (400, 300)), ('lineTo', (180, 300)), ('lineTo', (180, 0)),
         ('closePath', None)]
    ]}

    glyphs['I'] = {'width': 300, 'paths': [
        [('moveTo', (100, 0)), ('lineTo', (100, 700)), ('lineTo', (200, 700)),
         ('lineTo', (200, 0)), ('closePath', None)]
    ]}

    glyphs['J'] = {'width': 420, 'paths': [
        [('moveTo', (60, 200)), ('lineTo', (60, 100)), ('lineTo', (160, 0)),
         ('lineTo', (320, 0)), ('lineTo', (360, 40)), ('lineTo', (360, 700)),
         ('lineTo', (260, 700)), ('lineTo', (260, 100)), ('lineTo', (180, 100)),
         ('lineTo', (160, 120)), ('lineTo', (160, 200)), ('closePath', None)]
    ]}

    glyphs['K'] = {'width': 560, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (180, 700)),
         ('lineTo', (180, 400)), ('lineTo', (380, 700)), ('lineTo', (500, 700)),
         ('lineTo', (280, 380)), ('lineTo', (500, 0)), ('lineTo', (380, 0)),
         ('lineTo', (180, 320)), ('lineTo', (180, 0)), ('closePath', None)]
    ]}

    glyphs['L'] = {'width': 480, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (180, 700)),
         ('lineTo', (180, 100)), ('lineTo', (440, 100)), ('lineTo', (440, 0)),
         ('closePath', None)]
    ]}

    glyphs['M'] = {'width': 700, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (180, 700)),
         ('lineTo', (350, 300)), ('lineTo', (520, 700)), ('lineTo', (620, 700)),
         ('lineTo', (620, 0)), ('lineTo', (520, 0)), ('lineTo', (520, 500)),
         ('lineTo', (380, 150)), ('lineTo', (320, 150)), ('lineTo', (180, 500)),
         ('lineTo', (180, 0)), ('closePath', None)]
    ]}

    glyphs['N'] = {'width': 580, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (180, 700)),
         ('lineTo', (400, 200)), ('lineTo', (400, 700)), ('lineTo', (500, 700)),
         ('lineTo', (500, 0)), ('lineTo', (400, 0)), ('lineTo', (180, 500)),
         ('lineTo', (180, 0)), ('closePath', None)]
    ]}

    glyphs['O'] = {'width': 600, 'paths': [
        [('moveTo', (180, 0)), ('lineTo', (80, 100)), ('lineTo', (80, 600)),
         ('lineTo', (180, 700)), ('lineTo', (420, 700)), ('lineTo', (520, 600)),
         ('lineTo', (520, 100)), ('lineTo', (420, 0)), ('closePath', None)],
        [('moveTo', (200, 100)), ('lineTo', (400, 100)), ('lineTo', (420, 120)),
         ('lineTo', (420, 580)), ('lineTo', (400, 600)), ('lineTo', (200, 600)),
         ('lineTo', (180, 580)), ('lineTo', (180, 120)), ('closePath', None)]
    ]}

    glyphs['P'] = {'width': 540, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (380, 700)),
         ('lineTo', (480, 600)), ('lineTo', (480, 350)), ('lineTo', (380, 250)),
         ('lineTo', (180, 250)), ('lineTo', (180, 0)), ('closePath', None)],
        [('moveTo', (180, 350)), ('lineTo', (350, 350)), ('lineTo', (380, 380)),
         ('lineTo', (380, 570)), ('lineTo', (350, 600)), ('lineTo', (180, 600)),
         ('closePath', None)]
    ]}

    glyphs['Q'] = {'width': 620, 'paths': [
        [('moveTo', (180, 0)), ('lineTo', (80, 100)), ('lineTo', (80, 600)),
         ('lineTo', (180, 700)), ('lineTo', (420, 700)), ('lineTo', (520, 600)),
         ('lineTo', (520, 200)), ('lineTo', (560, 0)), ('lineTo', (450, 0)),
         ('lineTo', (420, 120)), ('lineTo', (420, 100)), ('closePath', None)],
        [('moveTo', (200, 100)), ('lineTo', (400, 100)), ('lineTo', (420, 120)),
         ('lineTo', (420, 580)), ('lineTo', (400, 600)), ('lineTo', (200, 600)),
         ('lineTo', (180, 580)), ('lineTo', (180, 120)), ('closePath', None)]
    ]}

    glyphs['R'] = {'width': 560, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 700)), ('lineTo', (380, 700)),
         ('lineTo', (480, 600)), ('lineTo', (480, 400)), ('lineTo', (400, 320)),
         ('lineTo', (500, 0)), ('lineTo', (380, 0)), ('lineTo', (300, 280)),
         ('lineTo', (180, 280)), ('lineTo', (180, 0)), ('closePath', None)],
        [('moveTo', (180, 380)), ('lineTo', (350, 380)), ('lineTo', (380, 420)),
         ('lineTo', (380, 560)), ('lineTo', (350, 600)), ('lineTo', (180, 600)),
         ('closePath', None)]
    ]}

    glyphs['S'] = {'width': 520, 'paths': [
        [('moveTo', (440, 150)), ('lineTo', (440, 50)), ('lineTo', (340, 0)),
         ('lineTo', (140, 0)), ('lineTo', (60, 80)), ('lineTo', (60, 250)),
         ('lineTo', (140, 320)), ('lineTo', (340, 320)), ('lineTo', (360, 340)),
         ('lineTo', (360, 450)), ('lineTo', (340, 480)), ('lineTo', (180, 480)),
         ('lineTo', (160, 500)), ('lineTo', (160, 550)), ('lineTo', (60, 600)),
         ('lineTo', (140, 700)), ('lineTo', (360, 700)), ('lineTo', (460, 620)),
         ('lineTo', (460, 420)), ('lineTo', (380, 350)), ('lineTo', (180, 350)),
         ('lineTo', (160, 330)), ('lineTo', (160, 220)), ('lineTo', (180, 200)),
         ('lineTo', (340, 200)), ('lineTo', (360, 180)), ('closePath', None)]
    ]}

    glyphs['T'] = {'width': 520, 'paths': [
        [('moveTo', (210, 0)), ('lineTo', (210, 600)), ('lineTo', (40, 600)),
         ('lineTo', (40, 700)), ('lineTo', (480, 700)), ('lineTo', (480, 600)),
         ('lineTo', (310, 600)), ('lineTo', (310, 0)), ('closePath', None)]
    ]}

    glyphs['U'] = {'width': 580, 'paths': [
        [('moveTo', (80, 700)), ('lineTo', (80, 150)), ('lineTo', (150, 0)),
         ('lineTo', (430, 0)), ('lineTo', (500, 150)), ('lineTo', (500, 700)),
         ('lineTo', (400, 700)), ('lineTo', (400, 180)), ('lineTo', (380, 100)),
         ('lineTo', (200, 100)), ('lineTo', (180, 180)), ('lineTo', (180, 700)),
         ('closePath', None)]
    ]}

    glyphs['V'] = {'width': 580, 'paths': [
        [('moveTo', (290, 0)), ('lineTo', (20, 700)), ('lineTo', (130, 700)),
         ('lineTo', (290, 200)), ('lineTo', (450, 700)), ('lineTo', (560, 700)),
         ('closePath', None)]
    ]}

    glyphs['W'] = {'width': 780, 'paths': [
        [('moveTo', (150, 0)), ('lineTo', (30, 700)), ('lineTo', (130, 700)),
         ('lineTo', (200, 200)), ('lineTo', (320, 600)), ('lineTo', (400, 600)),
         ('lineTo', (520, 200)), ('lineTo', (590, 700)), ('lineTo', (690, 700)),
         ('lineTo', (570, 0)), ('lineTo', (470, 0)), ('lineTo', (360, 400)),
         ('lineTo', (250, 0)), ('closePath', None)]
    ]}

    glyphs['X'] = {'width': 560, 'paths': [
        [('moveTo', (40, 0)), ('lineTo', (210, 350)), ('lineTo', (40, 700)),
         ('lineTo', (160, 700)), ('lineTo', (280, 450)), ('lineTo', (400, 700)),
         ('lineTo', (520, 700)), ('lineTo', (350, 350)), ('lineTo', (520, 0)),
         ('lineTo', (400, 0)), ('lineTo', (280, 250)), ('lineTo', (160, 0)),
         ('closePath', None)]
    ]}

    glyphs['Y'] = {'width': 560, 'paths': [
        [('moveTo', (230, 0)), ('lineTo', (230, 280)), ('lineTo', (30, 700)),
         ('lineTo', (150, 700)), ('lineTo', (280, 400)), ('lineTo', (410, 700)),
         ('lineTo', (530, 700)), ('lineTo', (330, 280)), ('lineTo', (330, 0)),
         ('closePath', None)]
    ]}

    glyphs['Z'] = {'width': 520, 'paths': [
        [('moveTo', (60, 0)), ('lineTo', (60, 100)), ('lineTo', (340, 600)),
         ('lineTo', (60, 600)), ('lineTo', (60, 700)), ('lineTo', (460, 700)),
         ('lineTo', (460, 600)), ('lineTo', (180, 100)), ('lineTo', (460, 100)),
         ('lineTo', (460, 0)), ('closePath', None)]
    ]}

    # 소문자 (대문자 축소 버전)
    for c in 'abcdefghijklmnopqrstuvwxyz':
        upper = c.upper()
        if upper in glyphs:
            # 간단히 같은 모양으로 (실제로는 다르게 해야 함)
            glyphs[c] = glyphs[upper].copy()

    # 숫자
    glyphs['zero'] = {'width': 500, 'paths': [
        [('moveTo', (150, 0)), ('lineTo', (80, 70)), ('lineTo', (80, 630)),
         ('lineTo', (150, 700)), ('lineTo', (350, 700)), ('lineTo', (420, 630)),
         ('lineTo', (420, 70)), ('lineTo', (350, 0)), ('closePath', None)],
        [('moveTo', (170, 100)), ('lineTo', (330, 100)), ('lineTo', (340, 110)),
         ('lineTo', (340, 590)), ('lineTo', (330, 600)), ('lineTo', (170, 600)),
         ('lineTo', (160, 590)), ('lineTo', (160, 110)), ('closePath', None)]
    ]}

    glyphs['one'] = {'width': 400, 'paths': [
        [('moveTo', (100, 0)), ('lineTo', (100, 100)), ('lineTo', (150, 100)),
         ('lineTo', (150, 550)), ('lineTo', (100, 500)), ('lineTo', (100, 600)),
         ('lineTo', (200, 700)), ('lineTo', (250, 700)), ('lineTo', (250, 100)),
         ('lineTo', (300, 100)), ('lineTo', (300, 0)), ('closePath', None)]
    ]}

    glyphs['two'] = {'width': 500, 'paths': [
        [('moveTo', (80, 0)), ('lineTo', (80, 100)), ('lineTo', (300, 350)),
         ('lineTo', (340, 400)), ('lineTo', (340, 550)), ('lineTo', (300, 600)),
         ('lineTo', (180, 600)), ('lineTo', (160, 580)), ('lineTo', (160, 500)),
         ('lineTo', (80, 500)), ('lineTo', (80, 620)), ('lineTo', (160, 700)),
         ('lineTo', (340, 700)), ('lineTo', (420, 620)), ('lineTo', (420, 380)),
         ('lineTo', (380, 320)), ('lineTo', (180, 100)), ('lineTo', (420, 100)),
         ('lineTo', (420, 0)), ('closePath', None)]
    ]}

    glyphs['three'] = {'width': 500, 'paths': [
        [('moveTo', (80, 100)), ('lineTo', (80, 0)), ('lineTo', (340, 0)),
         ('lineTo', (420, 80)), ('lineTo', (420, 280)), ('lineTo', (360, 340)),
         ('lineTo', (420, 400)), ('lineTo', (420, 620)), ('lineTo', (340, 700)),
         ('lineTo', (100, 700)), ('lineTo', (80, 680)), ('lineTo', (80, 580)),
         ('lineTo', (160, 600)), ('lineTo', (300, 600)), ('lineTo', (340, 560)),
         ('lineTo', (340, 420)), ('lineTo', (300, 380)), ('lineTo', (200, 380)),
         ('lineTo', (200, 300)), ('lineTo', (300, 300)), ('lineTo', (340, 260)),
         ('lineTo', (340, 120)), ('lineTo', (300, 80)), ('lineTo', (160, 80)),
         ('closePath', None)]
    ]}

    glyphs['four'] = {'width': 520, 'paths': [
        [('moveTo', (300, 0)), ('lineTo', (300, 200)), ('lineTo', (60, 200)),
         ('lineTo', (60, 300)), ('lineTo', (260, 700)), ('lineTo', (380, 700)),
         ('lineTo', (380, 300)), ('lineTo', (460, 300)), ('lineTo', (460, 200)),
         ('lineTo', (380, 200)), ('lineTo', (380, 0)), ('closePath', None)],
        [('moveTo', (300, 300)), ('lineTo', (300, 520)), ('lineTo', (160, 300)),
         ('closePath', None)]
    ]}

    glyphs['five'] = {'width': 500, 'paths': [
        [('moveTo', (80, 80)), ('lineTo', (80, 0)), ('lineTo', (340, 0)),
         ('lineTo', (420, 80)), ('lineTo', (420, 300)), ('lineTo', (340, 380)),
         ('lineTo', (180, 380)), ('lineTo', (180, 600)), ('lineTo', (400, 600)),
         ('lineTo', (400, 700)), ('lineTo', (80, 700)), ('lineTo', (80, 300)),
         ('lineTo', (300, 300)), ('lineTo', (340, 260)), ('lineTo', (340, 120)),
         ('lineTo', (300, 80)), ('lineTo', (160, 80)), ('closePath', None)]
    ]}

    glyphs['six'] = {'width': 500, 'paths': [
        [('moveTo', (340, 700)), ('lineTo', (420, 620)), ('lineTo', (340, 580)),
         ('lineTo', (200, 580)), ('lineTo', (160, 540)), ('lineTo', (160, 400)),
         ('lineTo', (300, 400)), ('lineTo', (420, 300)), ('lineTo', (420, 80)),
         ('lineTo', (340, 0)), ('lineTo', (160, 0)), ('lineTo', (80, 80)),
         ('lineTo', (80, 620)), ('lineTo', (160, 700)), ('closePath', None)],
        [('moveTo', (160, 100)), ('lineTo', (300, 100)), ('lineTo', (340, 140)),
         ('lineTo', (340, 260)), ('lineTo', (300, 300)), ('lineTo', (160, 300)),
         ('closePath', None)]
    ]}

    glyphs['seven'] = {'width': 480, 'paths': [
        [('moveTo', (140, 0)), ('lineTo', (360, 600)), ('lineTo', (80, 600)),
         ('lineTo', (80, 700)), ('lineTo', (440, 700)), ('lineTo', (440, 620)),
         ('lineTo', (240, 0)), ('closePath', None)]
    ]}

    glyphs['eight'] = {'width': 500, 'paths': [
        [('moveTo', (160, 0)), ('lineTo', (80, 80)), ('lineTo', (80, 260)),
         ('lineTo', (140, 340)), ('lineTo', (80, 420)), ('lineTo', (80, 620)),
         ('lineTo', (160, 700)), ('lineTo', (340, 700)), ('lineTo', (420, 620)),
         ('lineTo', (420, 420)), ('lineTo', (360, 340)), ('lineTo', (420, 260)),
         ('lineTo', (420, 80)), ('lineTo', (340, 0)), ('closePath', None)],
        [('moveTo', (180, 100)), ('lineTo', (320, 100)), ('lineTo', (340, 120)),
         ('lineTo', (340, 240)), ('lineTo', (300, 300)), ('lineTo', (200, 300)),
         ('lineTo', (160, 240)), ('lineTo', (160, 120)), ('closePath', None)],
        [('moveTo', (180, 380)), ('lineTo', (320, 380)), ('lineTo', (340, 420)),
         ('lineTo', (340, 560)), ('lineTo', (320, 600)), ('lineTo', (180, 600)),
         ('lineTo', (160, 560)), ('lineTo', (160, 420)), ('closePath', None)]
    ]}

    glyphs['nine'] = {'width': 500, 'paths': [
        [('moveTo', (80, 80)), ('lineTo', (160, 0)), ('lineTo', (340, 0)),
         ('lineTo', (420, 80)), ('lineTo', (420, 620)), ('lineTo', (340, 700)),
         ('lineTo', (160, 700)), ('lineTo', (80, 620)), ('lineTo', (80, 400)),
         ('lineTo', (160, 300)), ('lineTo', (340, 300)), ('lineTo', (340, 160)),
         ('lineTo', (200, 120)), ('lineTo', (160, 160)), ('closePath', None)],
        [('moveTo', (160, 400)), ('lineTo', (160, 560)), ('lineTo', (200, 600)),
         ('lineTo', (300, 600)), ('lineTo', (340, 560)), ('lineTo', (340, 400)),
         ('closePath', None)]
    ]}

    # 특수문자
    glyphs['period'] = {'width': 250, 'paths': [
        [('moveTo', (75, 0)), ('lineTo', (75, 100)), ('lineTo', (175, 100)),
         ('lineTo', (175, 0)), ('closePath', None)]
    ]}

    glyphs['comma'] = {'width': 250, 'paths': [
        [('moveTo', (75, -80)), ('lineTo', (125, 100)), ('lineTo', (175, 100)),
         ('lineTo', (175, 0)), ('lineTo', (125, 0)), ('closePath', None)]
    ]}

    glyphs['exclam'] = {'width': 250, 'paths': [
        [('moveTo', (75, 0)), ('lineTo', (75, 100)), ('lineTo', (175, 100)),
         ('lineTo', (175, 0)), ('closePath', None)],
        [('moveTo', (85, 200)), ('lineTo', (100, 700)), ('lineTo', (150, 700)),
         ('lineTo', (165, 200)), ('closePath', None)]
    ]}

    glyphs['question'] = {'width': 450, 'paths': [
        [('moveTo', (175, 0)), ('lineTo', (175, 100)), ('lineTo', (275, 100)),
         ('lineTo', (275, 0)), ('closePath', None)],
        [('moveTo', (175, 180)), ('lineTo', (175, 280)), ('lineTo', (275, 380)),
         ('lineTo', (350, 380)), ('lineTo', (350, 550)), ('lineTo', (300, 600)),
         ('lineTo', (150, 600)), ('lineTo', (100, 550)), ('lineTo', (100, 480)),
         ('lineTo', (50, 520)), ('lineTo', (100, 700)), ('lineTo', (350, 700)),
         ('lineTo', (430, 620)), ('lineTo', (430, 350)), ('lineTo', (350, 280)),
         ('lineTo', (275, 280)), ('lineTo', (275, 180)), ('closePath', None)]
    ]}

    glyphs['at'] = {'width': 700, 'paths': [
        [('moveTo', (350, 50)), ('lineTo', (150, 50)), ('lineTo', (50, 150)),
         ('lineTo', (50, 550)), ('lineTo', (150, 650)), ('lineTo', (450, 650)),
         ('lineTo', (550, 550)), ('lineTo', (550, 200)), ('lineTo', (450, 200)),
         ('lineTo', (450, 500)), ('lineTo', (400, 550)), ('lineTo', (200, 550)),
         ('lineTo', (150, 500)), ('lineTo', (150, 200)), ('lineTo', (200, 150)),
         ('lineTo', (450, 150)), ('lineTo', (500, 100)), ('closePath', None)],
        [('moveTo', (250, 250)), ('lineTo', (250, 400)), ('lineTo', (350, 400)),
         ('lineTo', (350, 250)), ('closePath', None)]
    ]}

    glyphs['numbersign'] = {'width': 550, 'paths': [
        [('moveTo', (120, 200)), ('lineTo', (80, 200)), ('lineTo', (80, 280)),
         ('lineTo', (100, 280)), ('lineTo', (80, 420)), ('lineTo', (80, 500)),
         ('lineTo', (120, 500)), ('lineTo', (120, 420)), ('lineTo', (230, 420)),
         ('lineTo', (230, 500)), ('lineTo', (270, 500)), ('lineTo', (270, 420)),
         ('lineTo', (380, 420)), ('lineTo', (380, 500)), ('lineTo', (420, 500)),
         ('lineTo', (420, 420)), ('lineTo', (470, 420)), ('lineTo', (470, 340)),
         ('lineTo', (420, 340)), ('lineTo', (420, 280)), ('lineTo', (470, 280)),
         ('lineTo', (470, 200)), ('lineTo', (420, 200)), ('lineTo', (420, 280)),
         ('lineTo', (310, 280)), ('lineTo', (310, 200)), ('lineTo', (270, 200)),
         ('lineTo', (270, 280)), ('lineTo', (160, 280)), ('lineTo', (160, 200)),
         ('closePath', None)],
        [('moveTo', (160, 340)), ('lineTo', (270, 340)), ('lineTo', (270, 420)),
         ('lineTo', (160, 420)), ('closePath', None)],
        [('moveTo', (310, 340)), ('lineTo', (420, 340)), ('lineTo', (420, 420)),
         ('lineTo', (310, 420)), ('closePath', None)]
    ]}

    return glyphs


# ============================================
# 스타일 2: BubblePop - 통통하고 귀여운 스타일
# ============================================

def create_bubble_font():
    """통통하고 둥근 버블 스타일 폰트"""
    glyphs = {}

    glyphs['.notdef'] = {'width': 500, 'paths': [
        [('moveTo', (50, 0)), ('lineTo', (50, 700)), ('lineTo', (450, 700)),
         ('lineTo', (450, 0)), ('closePath', None)]
    ]}
    glyphs['space'] = {'width': 300, 'paths': []}

    # 버블 스타일 대문자 - 둥글고 통통한 느낌
    glyphs['A'] = {'width': 650, 'paths': [
        [('moveTo', (325, 700)),
         ('qCurveTo', (200, 700), (100, 400)),
         ('lineTo', (50, 0)), ('lineTo', (180, 0)), ('lineTo', (200, 200)),
         ('lineTo', (450, 200)), ('lineTo', (470, 0)), ('lineTo', (600, 0)),
         ('lineTo', (550, 400)),
         ('qCurveTo', (450, 700), (325, 700)),
         ('closePath', None)],
        [('moveTo', (230, 320)), ('lineTo', (420, 320)), ('lineTo', (325, 580)),
         ('closePath', None)]
    ]}

    glyphs['B'] = {'width': 580, 'paths': [
        [('moveTo', (100, 0)), ('lineTo', (100, 700)), ('lineTo', (350, 700)),
         ('qCurveTo', (520, 700), (520, 550)),
         ('qCurveTo', (520, 420), (420, 380)),
         ('qCurveTo', (540, 340), (540, 200)),
         ('qCurveTo', (540, 0), (350, 0)),
         ('closePath', None)],
        [('moveTo', (220, 420)), ('lineTo', (320, 420)),
         ('qCurveTo', (400, 420), (400, 520)),
         ('qCurveTo', (400, 600), (320, 600)),
         ('lineTo', (220, 600)), ('closePath', None)],
        [('moveTo', (220, 100)), ('lineTo', (330, 100)),
         ('qCurveTo', (420, 100), (420, 200)),
         ('qCurveTo', (420, 300), (330, 300)),
         ('lineTo', (220, 300)), ('closePath', None)]
    ]}

    glyphs['C'] = {'width': 580, 'paths': [
        [('moveTo', (500, 180)),
         ('qCurveTo', (420, 0), (290, 0)),
         ('qCurveTo', (60, 0), (60, 350)),
         ('qCurveTo', (60, 700), (290, 700)),
         ('qCurveTo', (420, 700), (500, 520)),
         ('lineTo', (380, 460)),
         ('qCurveTo', (340, 560), (290, 560)),
         ('qCurveTo', (200, 560), (200, 350)),
         ('qCurveTo', (200, 140), (290, 140)),
         ('qCurveTo', (340, 140), (380, 240)),
         ('closePath', None)]
    ]}

    glyphs['D'] = {'width': 600, 'paths': [
        [('moveTo', (100, 0)), ('lineTo', (100, 700)), ('lineTo', (320, 700)),
         ('qCurveTo', (540, 700), (540, 350)),
         ('qCurveTo', (540, 0), (320, 0)),
         ('closePath', None)],
        [('moveTo', (220, 140)), ('lineTo', (300, 140)),
         ('qCurveTo', (400, 140), (400, 350)),
         ('qCurveTo', (400, 560), (300, 560)),
         ('lineTo', (220, 560)), ('closePath', None)]
    ]}

    glyphs['E'] = {'width': 520, 'paths': [
        [('moveTo', (100, 0)), ('lineTo', (100, 700)), ('lineTo', (460, 700)),
         ('qCurveTo', (460, 600), (380, 600)),
         ('lineTo', (220, 600)), ('lineTo', (220, 420)), ('lineTo', (360, 420)),
         ('qCurveTo', (360, 340), (300, 340)),
         ('lineTo', (220, 340)), ('lineTo', (220, 100)), ('lineTo', (380, 100)),
         ('qCurveTo', (460, 100), (460, 0)),
         ('closePath', None)]
    ]}

    # 간단히 나머지 대문자들 (기본 형태)
    for c in 'FGHIJKLMNOPQRSTUVWXYZ':
        glyphs[c] = {'width': 500, 'paths': [
            [('moveTo', (100, 0)), ('lineTo', (100, 700)), ('lineTo', (400, 700)),
             ('lineTo', (400, 0)), ('closePath', None)],
            [('moveTo', (150, 50)), ('lineTo', (150, 650)), ('lineTo', (350, 650)),
             ('lineTo', (350, 50)), ('closePath', None)]
        ]}

    # 소문자
    for c in 'abcdefghijklmnopqrstuvwxyz':
        upper = c.upper()
        if upper in glyphs:
            glyphs[c] = glyphs[upper].copy()

    # 숫자
    for i, n in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        glyphs[n] = {'width': 480, 'paths': [
            [('moveTo', (80, 0)),
             ('qCurveTo', (80, 350), (240, 350)),
             ('qCurveTo', (400, 350), (400, 0)),
             ('qCurveTo', (400, 700), (240, 700)),
             ('qCurveTo', (80, 700), (80, 350)),
             ('closePath', None)],
            [('moveTo', (140, 100)),
             ('qCurveTo', (140, 300), (240, 300)),
             ('qCurveTo', (340, 300), (340, 100)),
             ('qCurveTo', (340, 600), (240, 600)),
             ('qCurveTo', (140, 600), (140, 400)),
             ('closePath', None)]
        ]}

    # 특수문자
    glyphs['period'] = {'width': 250, 'paths': [
        [('moveTo', (75, 0)),
         ('qCurveTo', (75, 80), (125, 80)),
         ('qCurveTo', (175, 80), (175, 0)),
         ('qCurveTo', (175, -10), (125, -10)),
         ('qCurveTo', (75, -10), (75, 0)),
         ('closePath', None)]
    ]}

    glyphs['comma'] = {'width': 250, 'paths': [
        [('moveTo', (100, -60)), ('lineTo', (140, 80)), ('lineTo', (180, 80)),
         ('qCurveTo', (180, 0), (140, 0)),
         ('closePath', None)]
    ]}

    glyphs['exclam'] = {'width': 280, 'paths': [
        [('moveTo', (90, 0)),
         ('qCurveTo', (90, 80), (140, 80)),
         ('qCurveTo', (190, 80), (190, 0)),
         ('qCurveTo', (190, -10), (140, -10)),
         ('qCurveTo', (90, -10), (90, 0)),
         ('closePath', None)],
        [('moveTo', (100, 180)), ('lineTo', (120, 700)), ('lineTo', (160, 700)),
         ('lineTo', (180, 180)), ('closePath', None)]
    ]}

    glyphs['question'] = {'width': 450, 'paths': [
        [('moveTo', (175, 0)),
         ('qCurveTo', (175, 80), (225, 80)),
         ('qCurveTo', (275, 80), (275, 0)),
         ('closePath', None)],
        [('moveTo', (175, 160)), ('lineTo', (175, 280)),
         ('qCurveTo', (300, 350), (350, 450)),
         ('qCurveTo', (400, 550), (300, 620)),
         ('qCurveTo', (200, 680), (100, 600)),
         ('lineTo', (100, 500)),
         ('qCurveTo', (180, 560), (250, 560)),
         ('qCurveTo', (320, 560), (320, 480)),
         ('qCurveTo', (320, 400), (275, 350)),
         ('lineTo', (275, 160)), ('closePath', None)]
    ]}

    glyphs['at'] = glyphs['question'].copy()
    glyphs['numbersign'] = {'width': 500, 'paths': [
        [('moveTo', (100, 200)), ('lineTo', (100, 280)), ('lineTo', (150, 280)),
         ('lineTo', (150, 420)), ('lineTo', (100, 420)), ('lineTo', (100, 500)),
         ('lineTo', (150, 500)), ('lineTo', (150, 420)), ('lineTo', (250, 420)),
         ('lineTo', (250, 500)), ('lineTo', (300, 500)), ('lineTo', (300, 420)),
         ('lineTo', (400, 420)), ('lineTo', (400, 340)), ('lineTo', (300, 340)),
         ('lineTo', (300, 280)), ('lineTo', (400, 280)), ('lineTo', (400, 200)),
         ('lineTo', (300, 200)), ('lineTo', (300, 280)), ('lineTo', (200, 280)),
         ('lineTo', (200, 200)), ('closePath', None)],
        [('moveTo', (200, 340)), ('lineTo', (250, 340)), ('lineTo', (250, 420)),
         ('lineTo', (200, 420)), ('closePath', None)]
    ]}

    return glyphs


# ============================================
# 메인 함수
# ============================================

def main():
    print("=" * 50)
    print("  유니크 폰트 생성기 - 다양한 스타일")
    print("=" * 50)
    print()

    # Sharp Edge 폰트
    print("📐 SharpEdge 폰트 생성 중...")
    sharp_glyphs = create_sharp_font()
    build_font(sharp_glyphs, 'SharpEdge', 'SharpEdge', 'fonts/SharpEdge-Regular.ttf')

    # Bubble Pop 폰트
    print("🫧 BubblePop 폰트 생성 중...")
    bubble_glyphs = create_bubble_font()
    build_font(bubble_glyphs, 'BubblePop', 'BubblePop', 'fonts/BubblePop-Regular.ttf')

    print()
    print("🎉 모든 폰트 생성 완료!")
    print()
    print("📁 생성된 폰트:")
    print("   - fonts/SharpEdge-Regular.ttf (날카로운 각진 스타일)")
    print("   - fonts/BubblePop-Regular.ttf (통통한 버블 스타일)")


if __name__ == '__main__':
    main()
