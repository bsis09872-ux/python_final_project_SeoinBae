from utils.helper import validate_input_value, display_sub_menu_title, get_string, get_valid_integer, get_valid_booktype, get_float
from models.specialized_books import PaperBook, EBook
from models.base_book import *
from data.books_info import book_info

def sample_data_to_object():
    books = []
    isbn_set = set(book_info.keys())

    for isbn, data in book_info.items():

        if  data['유형']== "일반":
            # PaperBook 객체 만들기
            paper_book = PaperBook(
                title = data['도서명'],
                author = data['저자명'],
                isbn = isbn,
                pages = data["페이지수"],
                location = data["위치"]
            )

            # books에 추가
            books.append(paper_book)

        elif data["유형"] == "전자":
            # EBook 객체 만들기
            ebook = EBook(
                title = data['도서명'],
                author = data['저자명'],
                isbn = isbn,
                pages = data["페이지수"],
                ftype = data["파일형식"],
                size = data["파일용량"]
            )

            # books에 추가
            books.append(ebook)

    return books, isbn_set


def main():

    books, isbn_set = sample_data_to_object()

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
            isbn = (input("(ISBN) 등록을 원하는 도서의 고유 식별 번호를 입력하세요.:"))

            if isbn in isbn_set:
                print(f"등록하신 코드({isbn})는 기존 도서 목록에 이미 등록이 되어 있는 코드입니다.")

            else:
                print(f"ISBN: {isbn} - 등록을 원하는 도서의 정보를 입력해주세요.")
                title = get_string("도서명을 입력하세요:")
                author = get_string("저자명을 입력하세요.:")
                pages = get_valid_integer("페이지수를 입력하세요.:")

                book_type = get_valid_booktype("등록을 원하시는 도서 유형에 해당하는 번호를 입력하시오.\n(1) 일반도서\n(2) 전자도서\n :")

                if book_type == 1:
                    location = get_valid_integer("도서 위치를 나타내는 층수를 숫자로 입력해주세요.:")
                    new_book = PaperBook(title, author, isbn, pages, location)
                    books.append(new_book)
                    isbn_set.add(isbn)
                    print("일반 도서 등록이 완료되었습니다.")

                elif book_type == 2:
                    ftype = get_string("해당 전자 도서의 접근 가능한 파일 형식을 입력하세요:")
                    size = get_float("해당 전자 도서 파일의 용량을 입력하세요.:")
                    new_book = EBook(title, author, isbn, pages, ftype, size)
                    books.append(new_book)
                    isbn_set.add(isbn)
                    print("전자 도서 등록이 완료되었습니다.")

                else: 
                    print("[안내] 입력하신 도서의 유형을 다시 선택해주세요.")
  
                

        elif choice == 2: 
            display_sub_menu_title("전체 도서 조회")

            for book in books:
                a_book_info = book.display_info()
                print(a_book_info)

    
        
        elif choice == 3: 
            display_sub_menu_title("도서 검색")
            # isbn으로 검색하는거랑 제목으로 검색하기 저자명으로 검색하기 나누기!!
            isbn = input("찾으시는 도서의 식별번호(ISBN)를 입력하세요.:")

            if isbn in isbn_set:
                for book in books:
                    if book.get_isbn() == isbn:
                        the_book_info = book.display_info()
                        print(the_book_info)
            
            else: 
                print("찾으시는 도서가 없습니다. 도서 식별 번호를 다시 확인하세요.")
        


        elif choice == 4: 
            display_sub_menu_title("도서 대여 / 반납")
            target_isbn = get_string("찾으시는 도서의 식별번호(ISBN)를 입력하세요.:")

            if target_isbn not in isbn_set:
                print("해당 ISBN을 가진 도서를 찾을 수 없습니다.")

            else:
                for book in books:
                    if book.get_isbn() == target_isbn:
                        target_info = book.display_info()
                        target_book_status = book.get_status()
                        print(target_info)

                        if target_book_status is True:
                            print("해당 도서는 대여중입니다. 다른 이용자가 반납한 이후에 이용 가능합니다.")

                        else:
                            print("해당 도서는 대여가 가능합니다.")
                            want = get_valid_integer("대여를 원하시나요?(예 = 1 , 아니오 = 2)")
                            if want == 1:
                                book.set_status()
                            elif want == 2:
                                # 메인화면으로 돌아가기
                            else ValueError as e:
                                    print(f"[경고]-{e} 올바른 숫자를 공백없이 입력해주세요.")
                            
                            





            
        elif choice == 5: 
            print("[안내] 도서 관리 시스템을 종료합니다.")
            break

        else:
            print("[오류] 원하시는 메뉴의 번호를 공백 없이 숫자로만 입력해주세요.")
     


if __name__ == "__main__":
    main()