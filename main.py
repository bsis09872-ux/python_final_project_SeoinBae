from utils.helper import validate_input_value, display_sub_menu_title
from models.specialized_books import PaperBook, EBook
from data.books_info import book_info

def sample_data_to_object():
    books = []

    for data in book_info:

        if data["유형"] == "일반":
            # PaperBook 객체 만들기
            paper_book = PaperBook(
                title = data['도서명'],
                author = data['저자명'],
                isbn = data['ISBN'],
                pages = data["페이지수"],
                types = data["유형"],
                location = data["위치"]
            )

            # books에 추가
            books.append(paper_book)

        elif data["유형"] == "전자":
            # EBook 객체 만들기
            ebook = EBook(
                title = data['도서명'],
                author = data['저자명'],
                isbn = data['ISBN'],
                pages = data["페이지수"],
                types = data["유형"],
                ftype = data["파일형식"],
                size = data["파일용량"]
            )

            # books에 추가
            books.append(ebook)

    return books


def main():

    books = sample_data_to_object()

    while True:
        print("=" * 6 + "도서 관리 시스템" + "=" * 6)
        print("""\n1. 도서 등록
2. 전체 도서 조회
3. 도서 검색
4. 도서 대여 / 반납
5. 종료
    """)
        print("=" * 28)
        
        choice = validate_input_value("메뉴를 선택하시오: ")

        if choice == 1:
            display_sub_menu_title("도서 등록")
            

        elif choice == 2: 
            display_sub_menu_title("전체 도서 조회")
    
        
        elif choice == 3: 
            display_sub_menu_title("도서 검색")


        elif choice == 4: 
            display_sub_menu_title("도서 대여 / 반납")
            EBook.display_info()
            
        elif choice == 5: 
            print("[안내] 도서 관리 시스템을 종료합니다.")
            break

        else:
            print("[오류] 원하시는 메뉴의 번호를 공백 없이 숫자로만 입력해주세요.")
     


if __name__ == "__main__":
    main()