
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

        except ValueError as e:
            return f"[경고]-{e}: 입력하신 값이 없거나 올바르지 않습니다."

        if info == "":
            print("입력하신 값이 없거나 올바르지 않습니다.")

        else:
            return info


# ==============================
# 3. 숫자 입력 관련 함수
# ==============================

# 정수를 입력받아 반환
# 페이지 수, 도서 위치 등 정수값 입력에 사용
def get_valid_integer(prompt):

    while True:
        try:
            num = int(input(prompt))

        except ValueError as e:
            print(f"[경고]-{e}: 입력하신 값이 없거나 올바르지 않습니다.")

        if num == "":
            return "입력하신 값이 없거나 올바르지 않습니다."

        else:
            return num


# 실수를 입력받아 반환
# 전자책 파일 용량 등 소수값 입력에 사용
def get_float(prompt):

    while True:
        try:
            info = float(input(prompt))

        except ValueError as e:
            print(f"[경고]-{e}: 입력하신 값이 없거나 올바르지 않습니다.")

        if info == "":
            return "입력하신 값이 없거나 올바르지 않습니다."

        else:
            return info


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
            print("1~5 사이의 공백 없는 숫자로만 입력 바랍니다.")

    except ValueError as e:
        print(f"[경고]{e} - 1~5 사이의 공백 없는 숫자로만 입력 바랍니다.")

# 검색 메뉴에서 1~3 사이의 숫자를 입력받아 반환
def validate_input_value2(prompt):

    try:
        raw_input = input(prompt)
        search_option = int(raw_input)

        if 0 < search_option <= 3:
            return search_option

        else:
            print("1~5 사이의 공백 없는 숫자로만 입력 바랍니다.")

    except ValueError as e:
        print(f"[경고]{e} - 1~3 사이의 공백 없는 숫자로만 입력

# 도서 유형 메뉴에서 1 또는 2를 입력받아 반환
# 1 = 일반도서, 2 = 전자도서
def get_valid_booktype(prompt):

    try:
        raw_input = input(prompt)
        option_num = int(raw_input)

        if option_num == 1 or option_num == 2:
            return option_num

        else:
            return "메뉴에 있는 숫자를 공백 없이 입력 바랍니다."

    except ValueError as e:
        print(f"[경고]{e} - 메뉴에 있는 숫자를 공백 없이 입력 바랍니다.")

# -------------------------------------------------------
# 찾은 도서 객체의 현재 상태를 확인하고 대여 또는 반납 처리
def handle_borrow_return(book):
    target_info = book.display_info()
    target_book_status = book.get_status()

    print(target_info)

    # 현재 대여 중인 경우 → 반납 처리
    if target_book_status is True:
        print("해당 도서는 현재 대여 중입니다.")

        want = get_valid_integer(
            "반납을 원하시나요? (예 = 1, 아니오 = 2): "
        )

        if want == 1:
            book.set_status(False)
            print("도서 반납이 완료되었습니다.")

        elif want == 2:
            print("반납을 취소합니다.")

        else:
            print("[경고] 1 또는 2를 입력해주세요.")

    # 현재 대여 가능한 경우 → 대여 처리
    else:
        print("해당 도서는 대여가 가능합니다.")

        want = get_valid_integer(
            "대여를 원하시나요? (예 = 1, 아니오 = 2): "
        )

        if want == 1:
            book.set_status(True)
            print("도서 대출 신청이 완료되었습니다. 대출 기한은 30일입니다.")

        elif want == 2:
            print("대여를 취소합니다.")

        else:
            print("[경고] 1 또는 2를 입력해주세요.")