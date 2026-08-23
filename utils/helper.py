# 최소 기능: 도서 등록, 전체 조회, 검색, 대여, 반납
# 필요 함수: 메뉴 출력, 입력 검증, 도서 검색, 도서 정보 포맷팅

def display_sub_menu_title(title):
    print(">" * 6 + title + "<" * 6)


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

    

def validate_info_isbn():
    pass

# def validate_info_
