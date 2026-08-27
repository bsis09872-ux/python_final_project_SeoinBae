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
            isbn = (input("📌 등록할 도서의 ISBN을 입력하세요.\n→ "))

            if isbn in isbn_set:
                print(f"⚠️ 등록하신 ISBN({isbn})은 이미 등록된 도서입니다.")

            else:
                print(f"✅ ISBN: {isbn}\n도서 정보를 입력해주세요.")
                title = get_string("📖 도서명을 입력하세요.\n→ ")

                author = get_string("✍️ 저자명을 입력하세요.\n→ ")

                pages = get_valid_integer("📄 페이지 수를 입력하세요.\n→ ")

                book_type = get_valid_booktype(
                    "📚 등록할 도서 유형을 선택하세요.\n"
                    "1. 일반도서\n"
                    "2. 전자도서\n"
                    "→ "
                )

                if book_type == 1:
                    location = get_valid_integer( "🏢 도서가 위치한 층수를 숫자로 입력하세요.\n→ ")
                    new_book = PaperBook(title, author, isbn, pages, location)
                    books.append(new_book)
                    isbn_set.add(isbn)
                    print("✅ [완료] 일반 도서 등록이 완료되었습니다.")

                elif book_type == 2:
                    ftype = get_string("💾 전자 도서의 파일 형식을 입력하세요. (예: PDF, EPUB)\n→ ")
                    size = get_float("💽 전자 도서의 파일 용량을 입력하세요. (MB)\n→ ")
                    new_book = EBook(title, author, isbn, pages, ftype, size)
                    books.append(new_book)
                    isbn_set.add(isbn)
                    print("✅ [완료] 전자 도서 등록이 완료되었습니다.")

                else: 
                    print("⚠️ [경고] 도서 유형을 다시 선택해주세요.")
  
                

        elif choice == 2: 
            display_sub_menu_title("전체 도서 조회")

            for book in books:
                a_book_info = book.display_info()
                print(a_book_info)

    
        
        elif choice == 3: 
            display_sub_menu_title("도서 검색")

            keyword = get_string( "🔎 찾으시는 도서의 ISBN, 도서명 또는 저자명을 입력하세요.\n→ ")
            found = False

            for book in books:
                if (
                    book.get_isbn() == keyword
                    or keyword in book.get_title()
                    or keyword in book.get_author()

                ):
                    print(book.display_info())
                    found = True

            if found is False:
                print("ℹ️ [안내] 검색 결과가 없습니다.")      


        elif choice == 4: 
            display_sub_menu_title("도서 대여 / 반납")
      
            target_isbn = get_string("📚 대여/반납할 도서의 ISBN을 입력하세요.\n→ ")

            if target_isbn not in isbn_set:
                print("ℹ️ [안내] 해당 ISBN을 가진 도서를 찾을 수 없습니다.")

            else:
                for book in books:
                    if book.get_isbn() == target_isbn:
                        target_info = book.display_info()
                        target_book_status = book.get_status()

                        if target_book_status:
                            print(f"📖 [도서 정보]\n{target_info}")
                            print("ℹ️ [안내] 해당 도서는 현재 대여 중입니다.")
                            
                            want_return = get_valid_integer("📥 도서를 반납하시겠습니까?\n1. 예\n2. 아니오\n→ ")

                            if want_return == 1:
                                 book.set_status(False)
                                 print("✅ [완료] 도서 반납이 완료되었습니다. 감사합니다.")

                            elif want_return == 2:
                                print("ℹ️ [안내] 도서 반납을 취소합니다.")

                            else:
                                print("⚠️ [경고] 올바른 번호를 입력해주세요.")

                        else:
                            print(f"📖 [도서 정보]\n{target_info}")
                            print("ℹ️ [안내] 해당 도서는 대여가 가능합니다.")

                            want = get_valid_integer("📤 도서를 대여하시겠습니까?\n1. 예\n2. 아니오\n→ ")

                            if want == 1:
                                # 도서 대여
                                book.set_status(True) 
                                updated_info = book.display_info()
                                print(f"✅ [완료] 도서 대출이 완료되었습니다.\n대출 기한은 30일입니다.")
                                print(updated_info)

                            elif want == 2:
                                # 메인화면으로 돌아가기
                                print("ℹ️ [안내] 도서 대여를 취소합니다.")
        

                            else:
                                print("⚠️ [경고] 올바른 번호를 입력해주세요.") 
            
        elif choice == 5: 
            print("ℹ️ [안내] 도서 관리 시스템을 종료합니다.")
            break

        else:
            print("⚠️ [경고] 메뉴에 있는 번호를 공백 없이 입력해주세요.")
     


if __name__ == "__main__":
    main()