
"""
<helper.py 함수 목록>

화면 출력
└─ display_sub_menu_title()

문자열 입력
└─ get_string()

숫자 입력
├─ get_valid_integer()
└─ get_float()

메뉴 선택
├─ validate_input_value()
└─ get_valid_booktype()
"""

# ==============================
# 1. 화면 출력 관련 함수
# ==============================

# 서브 메뉴 제목을 일정한 형식으로 출력
def display_sub_menu_title(title):
    print(">" * 6 + title + "<" * 6)


# ==============================
# 2. 문자열 입력 관련 함수
# ==============================

# 문자열을 입력받고 앞뒤 공백을 제거한 뒤,
# 빈 값이 아닌 경우에만 반환
def get_string(prompt):

    while True:
        try:
            info = input(prompt).strip()
            return info

        except ValueError as e:
            print(f"⚠️ [경고]-{e}: 입력하신 값이 없거나 올바르지 않습니다.")


# ==============================
# 3. 숫자 입력 관련 함수
# ==============================

# 정수를 입력받아 반환
# 페이지 수, 도서 위치 등 정수값 입력에 사용
def get_valid_integer(prompt):

    while True:
        try:
            num = int(input(prompt))
            return num

        except ValueError as e:
            print(f"⚠️ [경고]-{e}: 입력하신 값이 없거나 올바르지 않습니다.")

        

# 실수를 입력받아 반환
# 전자책 파일 용량 등 소수값 입력에 사용
def get_float(prompt):

    while True:
        try:
            info = float(input(prompt))
            return info
    
        except ValueError as e:
            print(f"⚠️ [경고]-{e}: 입력하신 값이 없거나 올바르지 않습니다.")





# ==============================
# 4. 메뉴 선택 관련 함수
# ==============================

# 메인 메뉴에서 1~5 사이의 숫자를 입력받아 반환
def validate_input_value(prompt):

    try:
        raw_input = input(prompt)
        choice = int(raw_input)

        if 0 < choice <= 5:
            return choice

        else:
            print("⚠️ [경고] 1~5 사이의 공백 없는 숫자로만 입력 바랍니다.")

    except ValueError as e:
        print(f"⚠️ [경고]{e} - 1~5 사이의 공백 없는 숫자로만 입력 바랍니다.")
    

# 도서 유형 메뉴에서 1 또는 2를 입력받아 반환
# 1 = 일반도서, 2 = 전자도서
def get_valid_booktype(prompt):

    try:
        raw_input = input(prompt)
        option_num = int(raw_input)

        if option_num == 1 or option_num == 2:
            return option_num

        else:
            return "⚠️ [경고] 메뉴에 있는 숫자를 공백 없이 입력 바랍니다."

    except ValueError as e:
        print(f"⚠️ [경고]{e} - 메뉴에 있는 숫자를 공백 없이 입력 바랍니다.")

# -------------------------------------------------------
