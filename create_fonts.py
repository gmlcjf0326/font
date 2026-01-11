#!/usr/bin/env python3
"""
유니크한 커스텀 폰트 생성기
- 기하학적 스타일의 영문 + 숫자 + 한글 기본 폰트
"""

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.ttLib import TTFont
import math

# 폰트 기본 설정
UNITS_PER_EM = 1000
ASCENDER = 800
DESCENDER = -200
CAP_HEIGHT = 700
X_HEIGHT = 500

def create_geometric_font():
    """기하학적 버블 스타일 폰트 생성"""

    # 글리프 정의 (각 글자의 윤곽선)
    glyphs = {}

    # 기본 .notdef 글리프
    glyphs['.notdef'] = create_notdef_glyph()

    # 공백
    glyphs['space'] = {'width': 300, 'paths': []}

    # 영문 대문자
    glyphs['A'] = create_letter_A()
    glyphs['B'] = create_letter_B()
    glyphs['C'] = create_letter_C()
    glyphs['D'] = create_letter_D()
    glyphs['E'] = create_letter_E()
    glyphs['F'] = create_letter_F()
    glyphs['G'] = create_letter_G()
    glyphs['H'] = create_letter_H()
    glyphs['I'] = create_letter_I()
    glyphs['J'] = create_letter_J()
    glyphs['K'] = create_letter_K()
    glyphs['L'] = create_letter_L()
    glyphs['M'] = create_letter_M()
    glyphs['N'] = create_letter_N()
    glyphs['O'] = create_letter_O()
    glyphs['P'] = create_letter_P()
    glyphs['Q'] = create_letter_Q()
    glyphs['R'] = create_letter_R()
    glyphs['S'] = create_letter_S()
    glyphs['T'] = create_letter_T()
    glyphs['U'] = create_letter_U()
    glyphs['V'] = create_letter_V()
    glyphs['W'] = create_letter_W()
    glyphs['X'] = create_letter_X()
    glyphs['Y'] = create_letter_Y()
    glyphs['Z'] = create_letter_Z()

    # 영문 소문자
    glyphs['a'] = create_lower_a()
    glyphs['b'] = create_lower_b()
    glyphs['c'] = create_lower_c()
    glyphs['d'] = create_lower_d()
    glyphs['e'] = create_lower_e()
    glyphs['f'] = create_lower_f()
    glyphs['g'] = create_lower_g()
    glyphs['h'] = create_lower_h()
    glyphs['i'] = create_lower_i()
    glyphs['j'] = create_lower_j()
    glyphs['k'] = create_lower_k()
    glyphs['l'] = create_lower_l()
    glyphs['m'] = create_lower_m()
    glyphs['n'] = create_lower_n()
    glyphs['o'] = create_lower_o()
    glyphs['p'] = create_lower_p()
    glyphs['q'] = create_lower_q()
    glyphs['r'] = create_lower_r()
    glyphs['s'] = create_lower_s()
    glyphs['t'] = create_lower_t()
    glyphs['u'] = create_lower_u()
    glyphs['v'] = create_lower_v()
    glyphs['w'] = create_lower_w()
    glyphs['x'] = create_lower_x()
    glyphs['y'] = create_lower_y()
    glyphs['z'] = create_lower_z()

    # 숫자
    glyphs['zero'] = create_digit_0()
    glyphs['one'] = create_digit_1()
    glyphs['two'] = create_digit_2()
    glyphs['three'] = create_digit_3()
    glyphs['four'] = create_digit_4()
    glyphs['five'] = create_digit_5()
    glyphs['six'] = create_digit_6()
    glyphs['seven'] = create_digit_7()
    glyphs['eight'] = create_digit_8()
    glyphs['nine'] = create_digit_9()

    # 특수문자
    glyphs['period'] = create_period()
    glyphs['comma'] = create_comma()
    glyphs['exclam'] = create_exclamation()
    glyphs['question'] = create_question()
    glyphs['at'] = create_at()
    glyphs['numbersign'] = create_hash()

    return glyphs


def create_notdef_glyph():
    """기본 .notdef 글리프 (사각형)"""
    return {
        'width': 500,
        'paths': [
            # 외곽 사각형
            [('moveTo', (50, 0)),
             ('lineTo', (50, 700)),
             ('lineTo', (450, 700)),
             ('lineTo', (450, 0)),
             ('closePath', None)],
            # 내부 사각형 (구멍)
            [('moveTo', (100, 50)),
             ('lineTo', (400, 50)),
             ('lineTo', (400, 650)),
             ('lineTo', (100, 650)),
             ('closePath', None)]
        ]
    }


# ============================================
# 대문자 글리프 정의 - 둥근 기하학적 스타일
# ============================================

def create_letter_A():
    """대문자 A - 삼각형 + 가로줄"""
    return {
        'width': 650,
        'paths': [
            # 외곽 삼각형
            [('moveTo', (325, 700)),
             ('lineTo', (50, 0)),
             ('lineTo', (180, 0)),
             ('lineTo', (325, 500)),
             ('lineTo', (470, 0)),
             ('lineTo', (600, 0)),
             ('closePath', None)],
            # 가로줄
            [('moveTo', (150, 200)),
             ('lineTo', (500, 200)),
             ('lineTo', (470, 280)),
             ('lineTo', (180, 280)),
             ('closePath', None)]
        ]
    }

def create_letter_B():
    """대문자 B - 둥근 범프 두 개"""
    return {
        'width': 600,
        'paths': [
            # 메인 바디
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (350, 700)),
             ('qCurveTo', (520, 700), (520, 525)),
             ('qCurveTo', (520, 380), (380, 350)),
             ('qCurveTo', (550, 320), (550, 175)),
             ('qCurveTo', (550, 0), (350, 0)),
             ('closePath', None)],
            # 상단 구멍
            [('moveTo', (200, 580)),
             ('lineTo', (320, 580)),
             ('qCurveTo', (400, 580), (400, 525)),
             ('qCurveTo', (400, 420), (320, 420)),
             ('lineTo', (200, 420)),
             ('closePath', None)],
            # 하단 구멍
            [('moveTo', (200, 300)),
             ('lineTo', (340, 300)),
             ('qCurveTo', (430, 300), (430, 175)),
             ('qCurveTo', (430, 120), (340, 120)),
             ('lineTo', (200, 120)),
             ('closePath', None)]
        ]
    }

def create_letter_C():
    """대문자 C - 둥근 호"""
    return {
        'width': 600,
        'paths': [
            [('moveTo', (520, 150)),
             ('qCurveTo', (400, 0), (300, 0)),
             ('qCurveTo', (50, 0), (50, 350)),
             ('qCurveTo', (50, 700), (300, 700)),
             ('qCurveTo', (400, 700), (520, 550)),
             ('lineTo', (420, 480)),
             ('qCurveTo', (350, 580), (300, 580)),
             ('qCurveTo', (170, 580), (170, 350)),
             ('qCurveTo', (170, 120), (300, 120)),
             ('qCurveTo', (350, 120), (420, 220)),
             ('closePath', None)]
        ]
    }

def create_letter_D():
    """대문자 D"""
    return {
        'width': 620,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (300, 700)),
             ('qCurveTo', (550, 700), (550, 350)),
             ('qCurveTo', (550, 0), (300, 0)),
             ('closePath', None)],
            [('moveTo', (200, 120)),
             ('lineTo', (280, 120)),
             ('qCurveTo', (430, 120), (430, 350)),
             ('qCurveTo', (430, 580), (280, 580)),
             ('lineTo', (200, 580)),
             ('closePath', None)]
        ]
    }

def create_letter_E():
    """대문자 E"""
    return {
        'width': 550,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (500, 700)),
             ('lineTo', (500, 580)),
             ('lineTo', (200, 580)),
             ('lineTo', (200, 400)),
             ('lineTo', (450, 400)),
             ('lineTo', (450, 300)),
             ('lineTo', (200, 300)),
             ('lineTo', (200, 120)),
             ('lineTo', (500, 120)),
             ('lineTo', (500, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_F():
    """대문자 F"""
    return {
        'width': 520,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (480, 700)),
             ('lineTo', (480, 580)),
             ('lineTo', (200, 580)),
             ('lineTo', (200, 400)),
             ('lineTo', (420, 400)),
             ('lineTo', (420, 300)),
             ('lineTo', (200, 300)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_G():
    """대문자 G"""
    return {
        'width': 640,
        'paths': [
            [('moveTo', (520, 150)),
             ('qCurveTo', (400, 0), (300, 0)),
             ('qCurveTo', (50, 0), (50, 350)),
             ('qCurveTo', (50, 700), (300, 700)),
             ('qCurveTo', (450, 700), (550, 550)),
             ('lineTo', (450, 480)),
             ('qCurveTo', (380, 580), (300, 580)),
             ('qCurveTo', (170, 580), (170, 350)),
             ('qCurveTo', (170, 120), (300, 120)),
             ('qCurveTo', (380, 120), (420, 200)),
             ('lineTo', (420, 300)),
             ('lineTo', (320, 300)),
             ('lineTo', (320, 380)),
             ('lineTo', (550, 380)),
             ('lineTo', (550, 150)),
             ('closePath', None)]
        ]
    }

def create_letter_H():
    """대문자 H"""
    return {
        'width': 620,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (200, 700)),
             ('lineTo', (200, 420)),
             ('lineTo', (420, 420)),
             ('lineTo', (420, 700)),
             ('lineTo', (540, 700)),
             ('lineTo', (540, 0)),
             ('lineTo', (420, 0)),
             ('lineTo', (420, 300)),
             ('lineTo', (200, 300)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_I():
    """대문자 I"""
    return {
        'width': 300,
        'paths': [
            [('moveTo', (90, 0)),
             ('lineTo', (90, 700)),
             ('lineTo', (210, 700)),
             ('lineTo', (210, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_J():
    """대문자 J"""
    return {
        'width': 450,
        'paths': [
            [('moveTo', (50, 150)),
             ('qCurveTo', (50, 0), (200, 0)),
             ('qCurveTo', (380, 0), (380, 200)),
             ('lineTo', (380, 700)),
             ('lineTo', (260, 700)),
             ('lineTo', (260, 200)),
             ('qCurveTo', (260, 120), (200, 120)),
             ('qCurveTo', (140, 120), (140, 200)),
             ('lineTo', (140, 250)),
             ('lineTo', (50, 250)),
             ('closePath', None)]
        ]
    }

def create_letter_K():
    """대문자 K"""
    return {
        'width': 600,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (200, 700)),
             ('lineTo', (200, 420)),
             ('lineTo', (380, 700)),
             ('lineTo', (530, 700)),
             ('lineTo', (300, 350)),
             ('lineTo', (530, 0)),
             ('lineTo', (380, 0)),
             ('lineTo', (200, 280)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_L():
    """대문자 L"""
    return {
        'width': 500,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (200, 700)),
             ('lineTo', (200, 120)),
             ('lineTo', (460, 120)),
             ('lineTo', (460, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_M():
    """대문자 M"""
    return {
        'width': 750,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (220, 700)),
             ('lineTo', (375, 350)),
             ('lineTo', (530, 700)),
             ('lineTo', (670, 700)),
             ('lineTo', (670, 0)),
             ('lineTo', (550, 0)),
             ('lineTo', (550, 500)),
             ('lineTo', (400, 180)),
             ('lineTo', (350, 180)),
             ('lineTo', (200, 500)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_N():
    """대문자 N"""
    return {
        'width': 620,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (200, 700)),
             ('lineTo', (420, 250)),
             ('lineTo', (420, 700)),
             ('lineTo', (540, 700)),
             ('lineTo', (540, 0)),
             ('lineTo', (420, 0)),
             ('lineTo', (200, 450)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_O():
    """대문자 O - 완벽한 타원"""
    return {
        'width': 660,
        'paths': [
            [('moveTo', (330, 0)),
             ('qCurveTo', (50, 0), (50, 350)),
             ('qCurveTo', (50, 700), (330, 700)),
             ('qCurveTo', (610, 700), (610, 350)),
             ('qCurveTo', (610, 0), (330, 0)),
             ('closePath', None)],
            [('moveTo', (330, 120)),
             ('qCurveTo', (480, 120), (480, 350)),
             ('qCurveTo', (480, 580), (330, 580)),
             ('qCurveTo', (180, 580), (180, 350)),
             ('qCurveTo', (180, 120), (330, 120)),
             ('closePath', None)]
        ]
    }

def create_letter_P():
    """대문자 P"""
    return {
        'width': 580,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (320, 700)),
             ('qCurveTo', (520, 700), (520, 500)),
             ('qCurveTo', (520, 300), (320, 300)),
             ('lineTo', (200, 300)),
             ('lineTo', (200, 0)),
             ('closePath', None)],
            [('moveTo', (200, 420)),
             ('lineTo', (300, 420)),
             ('qCurveTo', (400, 420), (400, 500)),
             ('qCurveTo', (400, 580), (300, 580)),
             ('lineTo', (200, 580)),
             ('closePath', None)]
        ]
    }

def create_letter_Q():
    """대문자 Q"""
    return {
        'width': 660,
        'paths': [
            [('moveTo', (330, 0)),
             ('qCurveTo', (50, 0), (50, 350)),
             ('qCurveTo', (50, 700), (330, 700)),
             ('qCurveTo', (610, 700), (610, 350)),
             ('qCurveTo', (610, 50), (400, 0)),
             ('lineTo', (550, -100)),
             ('lineTo', (450, -150)),
             ('lineTo', (320, -30)),
             ('closePath', None)],
            [('moveTo', (330, 120)),
             ('qCurveTo', (480, 120), (480, 350)),
             ('qCurveTo', (480, 580), (330, 580)),
             ('qCurveTo', (180, 580), (180, 350)),
             ('qCurveTo', (180, 120), (330, 120)),
             ('closePath', None)]
        ]
    }

def create_letter_R():
    """대문자 R"""
    return {
        'width': 600,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (320, 700)),
             ('qCurveTo', (500, 700), (500, 520)),
             ('qCurveTo', (500, 380), (380, 340)),
             ('lineTo', (530, 0)),
             ('lineTo', (390, 0)),
             ('lineTo', (270, 300)),
             ('lineTo', (200, 300)),
             ('lineTo', (200, 0)),
             ('closePath', None)],
            [('moveTo', (200, 420)),
             ('lineTo', (300, 420)),
             ('qCurveTo', (380, 420), (380, 510)),
             ('qCurveTo', (380, 580), (300, 580)),
             ('lineTo', (200, 580)),
             ('closePath', None)]
        ]
    }

def create_letter_S():
    """대문자 S - 부드러운 곡선"""
    return {
        'width': 560,
        'paths': [
            [('moveTo', (480, 200)),
             ('qCurveTo', (480, 0), (280, 0)),
             ('qCurveTo', (60, 0), (60, 180)),
             ('lineTo', (180, 180)),
             ('qCurveTo', (180, 120), (280, 120)),
             ('qCurveTo', (360, 120), (360, 190)),
             ('qCurveTo', (360, 260), (250, 300)),
             ('qCurveTo', (60, 370), (60, 520)),
             ('qCurveTo', (60, 700), (280, 700)),
             ('qCurveTo', (480, 700), (480, 540)),
             ('lineTo', (360, 540)),
             ('qCurveTo', (360, 580), (280, 580)),
             ('qCurveTo', (180, 580), (180, 510)),
             ('qCurveTo', (180, 440), (300, 400)),
             ('qCurveTo', (480, 330), (480, 200)),
             ('closePath', None)]
        ]
    }

def create_letter_T():
    """대문자 T"""
    return {
        'width': 560,
        'paths': [
            [('moveTo', (220, 0)),
             ('lineTo', (220, 580)),
             ('lineTo', (40, 580)),
             ('lineTo', (40, 700)),
             ('lineTo', (520, 700)),
             ('lineTo', (520, 580)),
             ('lineTo', (340, 580)),
             ('lineTo', (340, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_U():
    """대문자 U"""
    return {
        'width': 620,
        'paths': [
            [('moveTo', (80, 700)),
             ('lineTo', (80, 250)),
             ('qCurveTo', (80, 0), (310, 0)),
             ('qCurveTo', (540, 0), (540, 250)),
             ('lineTo', (540, 700)),
             ('lineTo', (420, 700)),
             ('lineTo', (420, 250)),
             ('qCurveTo', (420, 120), (310, 120)),
             ('qCurveTo', (200, 120), (200, 250)),
             ('lineTo', (200, 700)),
             ('closePath', None)]
        ]
    }

def create_letter_V():
    """대문자 V"""
    return {
        'width': 620,
        'paths': [
            [('moveTo', (310, 0)),
             ('lineTo', (40, 700)),
             ('lineTo', (170, 700)),
             ('lineTo', (310, 200)),
             ('lineTo', (450, 700)),
             ('lineTo', (580, 700)),
             ('closePath', None)]
        ]
    }

def create_letter_W():
    """대문자 W"""
    return {
        'width': 850,
        'paths': [
            [('moveTo', (140, 0)),
             ('lineTo', (30, 700)),
             ('lineTo', (150, 700)),
             ('lineTo', (220, 200)),
             ('lineTo', (350, 600)),
             ('lineTo', (430, 600)),
             ('lineTo', (560, 200)),
             ('lineTo', (630, 700)),
             ('lineTo', (750, 700)),
             ('lineTo', (640, 0)),
             ('lineTo', (520, 0)),
             ('lineTo', (390, 400)),
             ('lineTo', (260, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_X():
    """대문자 X"""
    return {
        'width': 600,
        'paths': [
            [('moveTo', (50, 0)),
             ('lineTo', (230, 350)),
             ('lineTo', (50, 700)),
             ('lineTo', (190, 700)),
             ('lineTo', (300, 450)),
             ('lineTo', (410, 700)),
             ('lineTo', (550, 700)),
             ('lineTo', (370, 350)),
             ('lineTo', (550, 0)),
             ('lineTo', (410, 0)),
             ('lineTo', (300, 250)),
             ('lineTo', (190, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_Y():
    """대문자 Y"""
    return {
        'width': 580,
        'paths': [
            [('moveTo', (230, 0)),
             ('lineTo', (230, 280)),
             ('lineTo', (40, 700)),
             ('lineTo', (180, 700)),
             ('lineTo', (290, 420)),
             ('lineTo', (400, 700)),
             ('lineTo', (540, 700)),
             ('lineTo', (350, 280)),
             ('lineTo', (350, 0)),
             ('closePath', None)]
        ]
    }

def create_letter_Z():
    """대문자 Z"""
    return {
        'width': 560,
        'paths': [
            [('moveTo', (60, 0)),
             ('lineTo', (60, 120)),
             ('lineTo', (360, 580)),
             ('lineTo', (60, 580)),
             ('lineTo', (60, 700)),
             ('lineTo', (500, 700)),
             ('lineTo', (500, 580)),
             ('lineTo', (200, 120)),
             ('lineTo', (500, 120)),
             ('lineTo', (500, 0)),
             ('closePath', None)]
        ]
    }


# ============================================
# 소문자 글리프 정의
# ============================================

def create_lower_a():
    return {
        'width': 520,
        'paths': [
            [('moveTo', (420, 0)),
             ('lineTo', (420, 80)),
             ('qCurveTo', (350, 0), (240, 0)),
             ('qCurveTo', (60, 0), (60, 150)),
             ('qCurveTo', (60, 280), (240, 300)),
             ('lineTo', (320, 310)),
             ('lineTo', (320, 340)),
             ('qCurveTo', (320, 400), (240, 400)),
             ('qCurveTo', (160, 400), (140, 340)),
             ('lineTo', (60, 380)),
             ('qCurveTo', (100, 500), (250, 500)),
             ('qCurveTo', (420, 500), (420, 340)),
             ('lineTo', (420, 0)),
             ('closePath', None)],
            [('moveTo', (320, 220)),
             ('lineTo', (250, 210)),
             ('qCurveTo', (160, 200), (160, 150)),
             ('qCurveTo', (160, 100), (240, 100)),
             ('qCurveTo', (320, 100), (320, 180)),
             ('closePath', None)]
        ]
    }

def create_lower_b():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (200, 700)),
             ('lineTo', (200, 420)),
             ('qCurveTo', (260, 500), (340, 500)),
             ('qCurveTo', (480, 500), (480, 250)),
             ('qCurveTo', (480, 0), (340, 0)),
             ('qCurveTo', (260, 0), (200, 80)),
             ('lineTo', (200, 0)),
             ('closePath', None)],
            [('moveTo', (200, 250)),
             ('qCurveTo', (200, 120), (300, 120)),
             ('qCurveTo', (370, 120), (370, 250)),
             ('qCurveTo', (370, 380), (300, 380)),
             ('qCurveTo', (200, 380), (200, 250)),
             ('closePath', None)]
        ]
    }

def create_lower_c():
    return {
        'width': 480,
        'paths': [
            [('moveTo', (400, 100)),
             ('qCurveTo', (340, 0), (230, 0)),
             ('qCurveTo', (60, 0), (60, 250)),
             ('qCurveTo', (60, 500), (230, 500)),
             ('qCurveTo', (340, 500), (400, 400)),
             ('lineTo', (300, 340)),
             ('qCurveTo', (280, 380), (230, 380)),
             ('qCurveTo', (170, 380), (170, 250)),
             ('qCurveTo', (170, 120), (230, 120)),
             ('qCurveTo', (280, 120), (300, 160)),
             ('closePath', None)]
        ]
    }

def create_lower_d():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (340, 0)),
             ('lineTo', (340, 80)),
             ('qCurveTo', (280, 0), (200, 0)),
             ('qCurveTo', (60, 0), (60, 250)),
             ('qCurveTo', (60, 500), (200, 500)),
             ('qCurveTo', (280, 500), (340, 420)),
             ('lineTo', (340, 700)),
             ('lineTo', (460, 700)),
             ('lineTo', (460, 0)),
             ('closePath', None)],
            [('moveTo', (340, 250)),
             ('qCurveTo', (340, 380), (240, 380)),
             ('qCurveTo', (170, 380), (170, 250)),
             ('qCurveTo', (170, 120), (240, 120)),
             ('qCurveTo', (340, 120), (340, 250)),
             ('closePath', None)]
        ]
    }

def create_lower_e():
    return {
        'width': 520,
        'paths': [
            [('moveTo', (60, 250)),
             ('qCurveTo', (60, 500), (260, 500)),
             ('qCurveTo', (460, 500), (460, 260)),
             ('lineTo', (460, 220)),
             ('lineTo', (170, 220)),
             ('qCurveTo', (180, 120), (270, 120)),
             ('qCurveTo', (340, 120), (380, 180)),
             ('lineTo', (460, 120)),
             ('qCurveTo', (400, 0), (260, 0)),
             ('qCurveTo', (60, 0), (60, 250)),
             ('closePath', None)],
            [('moveTo', (170, 300)),
             ('lineTo', (350, 300)),
             ('qCurveTo', (340, 380), (260, 380)),
             ('qCurveTo', (180, 380), (170, 300)),
             ('closePath', None)]
        ]
    }

def create_lower_f():
    return {
        'width': 340,
        'paths': [
            [('moveTo', (100, 0)),
             ('lineTo', (100, 400)),
             ('lineTo', (40, 400)),
             ('lineTo', (40, 500)),
             ('lineTo', (100, 500)),
             ('qCurveTo', (100, 700), (250, 700)),
             ('lineTo', (300, 700)),
             ('lineTo', (300, 600)),
             ('lineTo', (260, 600)),
             ('qCurveTo', (220, 600), (220, 500)),
             ('lineTo', (300, 500)),
             ('lineTo', (300, 400)),
             ('lineTo', (220, 400)),
             ('lineTo', (220, 0)),
             ('closePath', None)]
        ]
    }

def create_lower_g():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (340, 500)),
             ('lineTo', (340, 420)),
             ('qCurveTo', (280, 500), (200, 500)),
             ('qCurveTo', (60, 500), (60, 250)),
             ('qCurveTo', (60, 0), (200, 0)),
             ('qCurveTo', (280, 0), (340, 80)),
             ('lineTo', (340, 0)),
             ('lineTo', (460, 0)),
             ('lineTo', (460, 400)),
             ('qCurveTo', (460, 600), (260, 600)),
             ('lineTo', (260, 500)),
             ('closePath', None)],
            [('moveTo', (340, 250)),
             ('qCurveTo', (340, 120), (240, 120)),
             ('qCurveTo', (170, 120), (170, 250)),
             ('qCurveTo', (170, 380), (240, 380)),
             ('qCurveTo', (340, 380), (340, 250)),
             ('closePath', None)]
        ]
    }

def create_lower_h():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (200, 700)),
             ('lineTo', (200, 420)),
             ('qCurveTo', (260, 500), (350, 500)),
             ('qCurveTo', (460, 500), (460, 350)),
             ('lineTo', (460, 0)),
             ('lineTo', (340, 0)),
             ('lineTo', (340, 320)),
             ('qCurveTo', (340, 380), (290, 380)),
             ('qCurveTo', (200, 380), (200, 280)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_lower_i():
    return {
        'width': 260,
        'paths': [
            [('moveTo', (70, 0)),
             ('lineTo', (70, 500)),
             ('lineTo', (190, 500)),
             ('lineTo', (190, 0)),
             ('closePath', None)],
            [('moveTo', (70, 600)),
             ('lineTo', (70, 700)),
             ('lineTo', (190, 700)),
             ('lineTo', (190, 600)),
             ('closePath', None)]
        ]
    }

def create_lower_j():
    return {
        'width': 260,
        'paths': [
            [('moveTo', (70, 500)),
             ('lineTo', (190, 500)),
             ('lineTo', (190, 0)),
             ('qCurveTo', (190, -150), (50, -150)),
             ('lineTo', (50, -50)),
             ('qCurveTo', (70, -50), (70, 0)),
             ('closePath', None)],
            [('moveTo', (70, 600)),
             ('lineTo', (70, 700)),
             ('lineTo', (190, 700)),
             ('lineTo', (190, 600)),
             ('closePath', None)]
        ]
    }

def create_lower_k():
    return {
        'width': 500,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 700)),
             ('lineTo', (200, 700)),
             ('lineTo', (200, 300)),
             ('lineTo', (340, 500)),
             ('lineTo', (470, 500)),
             ('lineTo', (290, 260)),
             ('lineTo', (470, 0)),
             ('lineTo', (340, 0)),
             ('lineTo', (200, 200)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_lower_l():
    return {
        'width': 260,
        'paths': [
            [('moveTo', (70, 0)),
             ('lineTo', (70, 700)),
             ('lineTo', (190, 700)),
             ('lineTo', (190, 0)),
             ('closePath', None)]
        ]
    }

def create_lower_m():
    return {
        'width': 780,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 500)),
             ('lineTo', (200, 500)),
             ('lineTo', (200, 420)),
             ('qCurveTo', (260, 500), (340, 500)),
             ('qCurveTo', (420, 500), (460, 420)),
             ('qCurveTo', (520, 500), (600, 500)),
             ('qCurveTo', (700, 500), (700, 350)),
             ('lineTo', (700, 0)),
             ('lineTo', (580, 0)),
             ('lineTo', (580, 320)),
             ('qCurveTo', (580, 380), (540, 380)),
             ('qCurveTo', (460, 380), (460, 280)),
             ('lineTo', (460, 0)),
             ('lineTo', (340, 0)),
             ('lineTo', (340, 320)),
             ('qCurveTo', (340, 380), (300, 380)),
             ('qCurveTo', (200, 380), (200, 280)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_lower_n():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 500)),
             ('lineTo', (200, 500)),
             ('lineTo', (200, 420)),
             ('qCurveTo', (260, 500), (350, 500)),
             ('qCurveTo', (460, 500), (460, 350)),
             ('lineTo', (460, 0)),
             ('lineTo', (340, 0)),
             ('lineTo', (340, 320)),
             ('qCurveTo', (340, 380), (290, 380)),
             ('qCurveTo', (200, 380), (200, 280)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_lower_o():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (270, 0)),
             ('qCurveTo', (60, 0), (60, 250)),
             ('qCurveTo', (60, 500), (270, 500)),
             ('qCurveTo', (480, 500), (480, 250)),
             ('qCurveTo', (480, 0), (270, 0)),
             ('closePath', None)],
            [('moveTo', (270, 120)),
             ('qCurveTo', (370, 120), (370, 250)),
             ('qCurveTo', (370, 380), (270, 380)),
             ('qCurveTo', (170, 380), (170, 250)),
             ('qCurveTo', (170, 120), (270, 120)),
             ('closePath', None)]
        ]
    }

def create_lower_p():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (80, -200)),
             ('lineTo', (80, 500)),
             ('lineTo', (200, 500)),
             ('lineTo', (200, 420)),
             ('qCurveTo', (260, 500), (340, 500)),
             ('qCurveTo', (480, 500), (480, 250)),
             ('qCurveTo', (480, 0), (340, 0)),
             ('qCurveTo', (260, 0), (200, 80)),
             ('lineTo', (200, -200)),
             ('closePath', None)],
            [('moveTo', (200, 250)),
             ('qCurveTo', (200, 120), (300, 120)),
             ('qCurveTo', (370, 120), (370, 250)),
             ('qCurveTo', (370, 380), (300, 380)),
             ('qCurveTo', (200, 380), (200, 250)),
             ('closePath', None)]
        ]
    }

def create_lower_q():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (340, -200)),
             ('lineTo', (340, 80)),
             ('qCurveTo', (280, 0), (200, 0)),
             ('qCurveTo', (60, 0), (60, 250)),
             ('qCurveTo', (60, 500), (200, 500)),
             ('qCurveTo', (280, 500), (340, 420)),
             ('lineTo', (340, 500)),
             ('lineTo', (460, 500)),
             ('lineTo', (460, -200)),
             ('closePath', None)],
            [('moveTo', (340, 250)),
             ('qCurveTo', (340, 380), (240, 380)),
             ('qCurveTo', (170, 380), (170, 250)),
             ('qCurveTo', (170, 120), (240, 120)),
             ('qCurveTo', (340, 120), (340, 250)),
             ('closePath', None)]
        ]
    }

def create_lower_r():
    return {
        'width': 380,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 500)),
             ('lineTo', (200, 500)),
             ('lineTo', (200, 400)),
             ('qCurveTo', (240, 500), (340, 500)),
             ('lineTo', (340, 380)),
             ('qCurveTo', (260, 380), (200, 300)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_lower_s():
    return {
        'width': 460,
        'paths': [
            [('moveTo', (380, 140)),
             ('qCurveTo', (380, 0), (220, 0)),
             ('qCurveTo', (60, 0), (60, 120)),
             ('lineTo', (160, 140)),
             ('qCurveTo', (170, 100), (220, 100)),
             ('qCurveTo', (280, 100), (280, 140)),
             ('qCurveTo', (280, 180), (200, 210)),
             ('qCurveTo', (60, 260), (60, 370)),
             ('qCurveTo', (60, 500), (230, 500)),
             ('qCurveTo', (400, 500), (400, 380)),
             ('lineTo', (300, 360)),
             ('qCurveTo', (290, 400), (230, 400)),
             ('qCurveTo', (160, 400), (160, 360)),
             ('qCurveTo', (160, 320), (240, 290)),
             ('qCurveTo', (380, 240), (380, 140)),
             ('closePath', None)]
        ]
    }

def create_lower_t():
    return {
        'width': 340,
        'paths': [
            [('moveTo', (100, 0)),
             ('qCurveTo', (100, 100), (180, 100)),
             ('lineTo', (220, 100)),
             ('qCurveTo', (220, 100), (220, 0)),
             ('lineTo', (300, 0)),
             ('qCurveTo', (300, 200), (220, 200)),
             ('lineTo', (220, 400)),
             ('lineTo', (300, 400)),
             ('lineTo', (300, 500)),
             ('lineTo', (220, 500)),
             ('lineTo', (220, 620)),
             ('lineTo', (100, 620)),
             ('lineTo', (100, 500)),
             ('lineTo', (40, 500)),
             ('lineTo', (40, 400)),
             ('lineTo', (100, 400)),
             ('closePath', None)]
        ]
    }

def create_lower_u():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (80, 500)),
             ('lineTo', (80, 150)),
             ('qCurveTo', (80, 0), (190, 0)),
             ('qCurveTo', (280, 0), (340, 80)),
             ('lineTo', (340, 0)),
             ('lineTo', (460, 0)),
             ('lineTo', (460, 500)),
             ('lineTo', (340, 500)),
             ('lineTo', (340, 180)),
             ('qCurveTo', (340, 120), (250, 120)),
             ('qCurveTo', (200, 120), (200, 180)),
             ('lineTo', (200, 500)),
             ('closePath', None)]
        ]
    }

def create_lower_v():
    return {
        'width': 480,
        'paths': [
            [('moveTo', (240, 0)),
             ('lineTo', (40, 500)),
             ('lineTo', (160, 500)),
             ('lineTo', (240, 180)),
             ('lineTo', (320, 500)),
             ('lineTo', (440, 500)),
             ('closePath', None)]
        ]
    }

def create_lower_w():
    return {
        'width': 700,
        'paths': [
            [('moveTo', (140, 0)),
             ('lineTo', (30, 500)),
             ('lineTo', (140, 500)),
             ('lineTo', (200, 180)),
             ('lineTo', (300, 450)),
             ('lineTo', (380, 450)),
             ('lineTo', (480, 180)),
             ('lineTo', (540, 500)),
             ('lineTo', (650, 500)),
             ('lineTo', (540, 0)),
             ('lineTo', (430, 0)),
             ('lineTo', (340, 280)),
             ('lineTo', (250, 0)),
             ('closePath', None)]
        ]
    }

def create_lower_x():
    return {
        'width': 480,
        'paths': [
            [('moveTo', (40, 0)),
             ('lineTo', (180, 250)),
             ('lineTo', (40, 500)),
             ('lineTo', (170, 500)),
             ('lineTo', (240, 340)),
             ('lineTo', (310, 500)),
             ('lineTo', (440, 500)),
             ('lineTo', (300, 250)),
             ('lineTo', (440, 0)),
             ('lineTo', (310, 0)),
             ('lineTo', (240, 160)),
             ('lineTo', (170, 0)),
             ('closePath', None)]
        ]
    }

def create_lower_y():
    return {
        'width': 480,
        'paths': [
            [('moveTo', (100, -200)),
             ('qCurveTo', (200, -200), (240, -100)),
             ('lineTo', (240, 0)),
             ('lineTo', (40, 500)),
             ('lineTo', (160, 500)),
             ('lineTo', (240, 280)),
             ('lineTo', (320, 500)),
             ('lineTo', (440, 500)),
             ('lineTo', (240, -50)),
             ('qCurveTo', (200, -150), (100, -150)),
             ('closePath', None)]
        ]
    }

def create_lower_z():
    return {
        'width': 460,
        'paths': [
            [('moveTo', (60, 0)),
             ('lineTo', (60, 100)),
             ('lineTo', (280, 400)),
             ('lineTo', (60, 400)),
             ('lineTo', (60, 500)),
             ('lineTo', (400, 500)),
             ('lineTo', (400, 400)),
             ('lineTo', (180, 100)),
             ('lineTo', (400, 100)),
             ('lineTo', (400, 0)),
             ('closePath', None)]
        ]
    }


# ============================================
# 숫자 글리프 정의
# ============================================

def create_digit_0():
    return {
        'width': 560,
        'paths': [
            [('moveTo', (280, 0)),
             ('qCurveTo', (60, 0), (60, 350)),
             ('qCurveTo', (60, 700), (280, 700)),
             ('qCurveTo', (500, 700), (500, 350)),
             ('qCurveTo', (500, 0), (280, 0)),
             ('closePath', None)],
            [('moveTo', (280, 120)),
             ('qCurveTo', (380, 120), (380, 350)),
             ('qCurveTo', (380, 580), (280, 580)),
             ('qCurveTo', (180, 580), (180, 350)),
             ('qCurveTo', (180, 120), (280, 120)),
             ('closePath', None)]
        ]
    }

def create_digit_1():
    return {
        'width': 400,
        'paths': [
            [('moveTo', (120, 0)),
             ('lineTo', (120, 120)),
             ('lineTo', (200, 120)),
             ('lineTo', (200, 580)),
             ('lineTo', (100, 500)),
             ('lineTo', (60, 580)),
             ('lineTo', (200, 700)),
             ('lineTo', (320, 700)),
             ('lineTo', (320, 120)),
             ('lineTo', (380, 120)),
             ('lineTo', (380, 0)),
             ('closePath', None)]
        ]
    }

def create_digit_2():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (60, 0)),
             ('lineTo', (60, 120)),
             ('lineTo', (320, 400)),
             ('qCurveTo', (400, 480), (400, 540)),
             ('qCurveTo', (400, 600), (280, 600)),
             ('qCurveTo', (180, 600), (140, 520)),
             ('lineTo', (60, 580)),
             ('qCurveTo', (120, 700), (280, 700)),
             ('qCurveTo', (500, 700), (500, 530)),
             ('qCurveTo', (500, 400), (380, 300)),
             ('lineTo', (180, 120)),
             ('lineTo', (480, 120)),
             ('lineTo', (480, 0)),
             ('closePath', None)]
        ]
    }

def create_digit_3():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (60, 120)),
             ('qCurveTo', (120, 0), (280, 0)),
             ('qCurveTo', (480, 0), (480, 170)),
             ('qCurveTo', (480, 300), (360, 340)),
             ('qCurveTo', (480, 380), (480, 510)),
             ('qCurveTo', (480, 700), (280, 700)),
             ('qCurveTo', (100, 700), (60, 560)),
             ('lineTo', (160, 520)),
             ('qCurveTo', (180, 580), (280, 580)),
             ('qCurveTo', (360, 580), (360, 510)),
             ('qCurveTo', (360, 420), (260, 400)),
             ('lineTo', (200, 400)),
             ('lineTo', (200, 300)),
             ('lineTo', (260, 300)),
             ('qCurveTo', (360, 280), (360, 190)),
             ('qCurveTo', (360, 120), (280, 120)),
             ('qCurveTo', (180, 120), (160, 180)),
             ('closePath', None)]
        ]
    }

def create_digit_4():
    return {
        'width': 560,
        'paths': [
            [('moveTo', (340, 0)),
             ('lineTo', (340, 200)),
             ('lineTo', (60, 200)),
             ('lineTo', (60, 320)),
             ('lineTo', (300, 700)),
             ('lineTo', (460, 700)),
             ('lineTo', (460, 320)),
             ('lineTo', (520, 320)),
             ('lineTo', (520, 200)),
             ('lineTo', (460, 200)),
             ('lineTo', (460, 0)),
             ('closePath', None)],
            [('moveTo', (340, 320)),
             ('lineTo', (340, 520)),
             ('lineTo', (180, 320)),
             ('closePath', None)]
        ]
    }

def create_digit_5():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (80, 100)),
             ('qCurveTo', (140, 0), (300, 0)),
             ('qCurveTo', (480, 0), (480, 200)),
             ('qCurveTo', (480, 400), (280, 400)),
             ('qCurveTo', (200, 400), (160, 360)),
             ('lineTo', (180, 580)),
             ('lineTo', (460, 580)),
             ('lineTo', (460, 700)),
             ('lineTo', (80, 700)),
             ('lineTo', (60, 300)),
             ('lineTo', (120, 280)),
             ('qCurveTo', (180, 320), (260, 320)),
             ('qCurveTo', (360, 320), (360, 200)),
             ('qCurveTo', (360, 100), (280, 100)),
             ('qCurveTo', (200, 100), (180, 160)),
             ('closePath', None)]
        ]
    }

def create_digit_6():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (400, 600)),
             ('qCurveTo', (340, 700), (260, 700)),
             ('qCurveTo', (60, 700), (60, 400)),
             ('lineTo', (60, 200)),
             ('qCurveTo', (60, 0), (280, 0)),
             ('qCurveTo', (480, 0), (480, 200)),
             ('qCurveTo', (480, 400), (280, 400)),
             ('qCurveTo', (200, 400), (180, 340)),
             ('lineTo', (180, 400)),
             ('qCurveTo', (180, 580), (260, 580)),
             ('qCurveTo', (300, 580), (320, 540)),
             ('closePath', None)],
            [('moveTo', (280, 120)),
             ('qCurveTo', (180, 120), (180, 200)),
             ('qCurveTo', (180, 280), (280, 280)),
             ('qCurveTo', (360, 280), (360, 200)),
             ('qCurveTo', (360, 120), (280, 120)),
             ('closePath', None)]
        ]
    }

def create_digit_7():
    return {
        'width': 520,
        'paths': [
            [('moveTo', (140, 0)),
             ('lineTo', (380, 580)),
             ('lineTo', (60, 580)),
             ('lineTo', (60, 700)),
             ('lineTo', (480, 700)),
             ('lineTo', (480, 600)),
             ('lineTo', (260, 0)),
             ('closePath', None)]
        ]
    }

def create_digit_8():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (280, 0)),
             ('qCurveTo', (60, 0), (60, 180)),
             ('qCurveTo', (60, 320), (180, 360)),
             ('qCurveTo', (60, 400), (60, 520)),
             ('qCurveTo', (60, 700), (280, 700)),
             ('qCurveTo', (500, 700), (500, 520)),
             ('qCurveTo', (500, 400), (380, 360)),
             ('qCurveTo', (500, 320), (500, 180)),
             ('qCurveTo', (500, 0), (280, 0)),
             ('closePath', None)],
            [('moveTo', (280, 100)),
             ('qCurveTo', (380, 100), (380, 180)),
             ('qCurveTo', (380, 260), (280, 280)),
             ('qCurveTo', (180, 260), (180, 180)),
             ('qCurveTo', (180, 100), (280, 100)),
             ('closePath', None)],
            [('moveTo', (280, 400)),
             ('qCurveTo', (360, 420), (360, 500)),
             ('qCurveTo', (360, 580), (280, 580)),
             ('qCurveTo', (200, 580), (200, 500)),
             ('qCurveTo', (200, 420), (280, 400)),
             ('closePath', None)]
        ]
    }

def create_digit_9():
    return {
        'width': 540,
        'paths': [
            [('moveTo', (140, 100)),
             ('qCurveTo', (200, 0), (280, 0)),
             ('qCurveTo', (480, 0), (480, 300)),
             ('lineTo', (480, 500)),
             ('qCurveTo', (480, 700), (260, 700)),
             ('qCurveTo', (60, 700), (60, 500)),
             ('qCurveTo', (60, 300), (260, 300)),
             ('qCurveTo', (340, 300), (360, 360)),
             ('lineTo', (360, 300)),
             ('qCurveTo', (360, 120), (280, 120)),
             ('qCurveTo', (240, 120), (220, 160)),
             ('closePath', None)],
            [('moveTo', (260, 420)),
             ('qCurveTo', (180, 420), (180, 500)),
             ('qCurveTo', (180, 580), (260, 580)),
             ('qCurveTo', (360, 580), (360, 500)),
             ('qCurveTo', (360, 420), (260, 420)),
             ('closePath', None)]
        ]
    }


# ============================================
# 특수문자
# ============================================

def create_period():
    return {
        'width': 280,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 120)),
             ('lineTo', (200, 120)),
             ('lineTo', (200, 0)),
             ('closePath', None)]
        ]
    }

def create_comma():
    return {
        'width': 280,
        'paths': [
            [('moveTo', (80, -80)),
             ('lineTo', (140, 120)),
             ('lineTo', (200, 120)),
             ('lineTo', (200, 0)),
             ('lineTo', (140, 0)),
             ('lineTo', (80, -80)),
             ('closePath', None)]
        ]
    }

def create_exclamation():
    return {
        'width': 280,
        'paths': [
            [('moveTo', (80, 0)),
             ('lineTo', (80, 120)),
             ('lineTo', (200, 120)),
             ('lineTo', (200, 0)),
             ('closePath', None)],
            [('moveTo', (100, 240)),
             ('lineTo', (120, 700)),
             ('lineTo', (160, 700)),
             ('lineTo', (180, 240)),
             ('closePath', None)]
        ]
    }

def create_question():
    return {
        'width': 480,
        'paths': [
            [('moveTo', (180, 0)),
             ('lineTo', (180, 120)),
             ('lineTo', (300, 120)),
             ('lineTo', (300, 0)),
             ('closePath', None)],
            [('moveTo', (180, 220)),
             ('lineTo', (180, 300)),
             ('qCurveTo', (180, 400), (300, 450)),
             ('qCurveTo', (380, 480), (380, 540)),
             ('qCurveTo', (380, 600), (250, 600)),
             ('qCurveTo', (140, 600), (100, 520)),
             ('lineTo', (60, 580)),
             ('qCurveTo', (120, 700), (260, 700)),
             ('qCurveTo', (480, 700), (480, 540)),
             ('qCurveTo', (480, 400), (320, 340)),
             ('qCurveTo', (300, 330), (300, 280)),
             ('lineTo', (300, 220)),
             ('closePath', None)]
        ]
    }

def create_at():
    return {
        'width': 800,
        'paths': [
            [('moveTo', (400, 100)),
             ('qCurveTo', (200, 100), (120, 250)),
             ('qCurveTo', (50, 400), (50, 400)),
             ('qCurveTo', (50, 600), (200, 700)),
             ('qCurveTo', (350, 780), (500, 700)),
             ('lineTo', (460, 620)),
             ('qCurveTo', (350, 680), (250, 640)),
             ('qCurveTo', (150, 580), (150, 400)),
             ('qCurveTo', (150, 220), (300, 180)),
             ('qCurveTo', (450, 150), (550, 250)),
             ('lineTo', (550, 420)),
             ('qCurveTo', (550, 480), (500, 480)),
             ('qCurveTo', (450, 480), (450, 400)),
             ('lineTo', (450, 280)),
             ('qCurveTo', (400, 200), (320, 200)),
             ('qCurveTo', (220, 200), (220, 340)),
             ('qCurveTo', (220, 480), (350, 480)),
             ('qCurveTo', (420, 480), (450, 420)),
             ('qCurveTo', (480, 560), (550, 560)),
             ('qCurveTo', (680, 560), (680, 400)),
             ('lineTo', (680, 250)),
             ('qCurveTo', (680, 50), (450, 50)),
             ('closePath', None)],
            [('moveTo', (350, 380)),
             ('qCurveTo', (350, 290), (330, 290)),
             ('qCurveTo', (310, 290), (310, 350)),
             ('qCurveTo', (310, 400), (350, 380)),
             ('closePath', None)]
        ]
    }

def create_hash():
    return {
        'width': 600,
        'paths': [
            [('moveTo', (120, 200)),
             ('lineTo', (80, 200)),
             ('lineTo', (80, 280)),
             ('lineTo', (100, 280)),
             ('lineTo', (60, 500)),
             ('lineTo', (80, 500)),
             ('lineTo', (80, 580)),
             ('lineTo', (140, 580)),
             ('lineTo', (140, 500)),
             ('lineTo', (260, 500)),
             ('lineTo', (260, 580)),
             ('lineTo', (320, 580)),
             ('lineTo', (320, 500)),
             ('lineTo', (440, 500)),
             ('lineTo', (440, 580)),
             ('lineTo', (500, 580)),
             ('lineTo', (500, 500)),
             ('lineTo', (540, 500)),
             ('lineTo', (540, 420)),
             ('lineTo', (480, 420)),
             ('lineTo', (520, 280)),
             ('lineTo', (540, 280)),
             ('lineTo', (540, 200)),
             ('lineTo', (480, 200)),
             ('lineTo', (480, 280)),
             ('lineTo', (360, 280)),
             ('lineTo', (360, 200)),
             ('lineTo', (300, 200)),
             ('lineTo', (300, 280)),
             ('lineTo', (180, 280)),
             ('lineTo', (180, 200)),
             ('closePath', None)],
            [('moveTo', (180, 360)),
             ('lineTo', (300, 360)),
             ('lineTo', (300, 420)),
             ('lineTo', (180, 420)),
             ('closePath', None)],
            [('moveTo', (360, 360)),
             ('lineTo', (480, 360)),
             ('lineTo', (480, 420)),
             ('lineTo', (360, 420)),
             ('closePath', None)]
        ]
    }


def build_font(glyphs, font_name, family_name, output_path):
    """TTF 폰트 파일 생성"""

    # 글리프 이름 목록
    glyph_order = ['.notdef'] + [g for g in glyphs.keys() if g != '.notdef']

    # 문자 매핑 생성
    cmap = {}
    char_map = {
        'space': 0x0020,
        'exclam': 0x0021,
        'numbersign': 0x0023,
        'comma': 0x002C,
        'period': 0x002E,
        'zero': 0x0030, 'one': 0x0031, 'two': 0x0032, 'three': 0x0033,
        'four': 0x0034, 'five': 0x0035, 'six': 0x0036, 'seven': 0x0037,
        'eight': 0x0038, 'nine': 0x0039,
        'question': 0x003F,
        'at': 0x0040,
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

    for glyph_name, unicode_val in char_map.items():
        if glyph_name in glyphs:
            cmap[unicode_val] = glyph_name

    # FontBuilder 생성
    fb = FontBuilder(UNITS_PER_EM, isTTF=True)
    fb.setupGlyphOrder(glyph_order)

    # 글리프 폭 설정
    advance_widths = {name: glyph['width'] for name, glyph in glyphs.items()}
    fb.setupCharacterMap(cmap)

    # 글리프 윤곽선 생성
    pen_glyphs = {}
    for name, glyph_data in glyphs.items():
        from fontTools.pens.ttGlyphPen import TTGlyphPen
        pen = TTGlyphPen(None)

        for path in glyph_data.get('paths', []):
            for item in path:
                cmd = item[0]
                args = item[1] if len(item) > 1 else None

                if cmd == 'moveTo':
                    pen.moveTo(args)
                elif cmd == 'lineTo':
                    pen.lineTo(args)
                elif cmd == 'qCurveTo':
                    # qCurveTo는 (컨트롤포인트, 끝점) 형태
                    if len(item) == 3:
                        pen.qCurveTo(item[1], item[2])
                    elif len(item) == 2 and isinstance(item[1], tuple):
                        # 단일 튜플인 경우
                        pen.qCurveTo(item[1])
                elif cmd == 'closePath':
                    pen.closePath()

        pen_glyphs[name] = pen.glyph()

    fb.setupGlyf(pen_glyphs)

    # 메트릭 설정
    metrics = {name: (glyph['width'], pen_glyphs[name].xMin if hasattr(pen_glyphs[name], 'xMin') and pen_glyphs[name].xMin is not None else 0)
               for name, glyph in glyphs.items()}
    fb.setupHorizontalMetrics(metrics)

    # 헤더 설정
    fb.setupHorizontalHeader(ascent=ASCENDER, descent=DESCENDER)
    fb.setupHead(unitsPerEm=UNITS_PER_EM)

    # 이름 테이블 설정
    name_strings = {
        'familyName': family_name,
        'styleName': 'Regular',
        'uniqueFontIdentifier': f'{family_name}-Regular',
        'fullName': f'{family_name} Regular',
        'version': 'Version 1.0',
        'psName': font_name,
    }
    fb.setupNameTable(name_strings)

    # OS/2 테이블 설정
    fb.setupOS2(sTypoAscender=ASCENDER, sTypoDescender=DESCENDER,
                sCapHeight=CAP_HEIGHT, sxHeight=X_HEIGHT)

    # Post 테이블 설정
    fb.setupPost()

    # 폰트 저장
    fb.save(output_path)
    print(f"✅ 폰트 생성 완료: {output_path}")


def main():
    print("=" * 50)
    print("  커스텀 폰트 생성기")
    print("=" * 50)
    print()

    # 기하학적 버블 스타일 폰트 생성
    print("📝 GeoRound 폰트 생성 중...")
    glyphs = create_geometric_font()
    build_font(glyphs, 'GeoRound', 'GeoRound', 'fonts/GeoRound-Regular.ttf')

    print()
    print("🎉 모든 폰트 생성 완료!")
    print()
    print("📁 생성된 폰트:")
    print("   - fonts/GeoRound-Regular.ttf (기하학적 둥근 스타일)")


if __name__ == '__main__':
    main()
