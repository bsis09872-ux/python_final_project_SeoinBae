elif choice == 3: 
    display_sub_menu_title("도서 검색")

    keyword = get_string("찾으시는 도서의 ISBN, 도서명 또는 저자명을 입력하세요.:")
    found = False

    for book in books:
        if (
             book.get_isbn() == keyword
             or keyword in book.get_tutke()
             or keyword in book.get_author()

        ):
            print(book.display_info())
            found = True

    if found is False:
        print("검색 결과가 없습니다.")      
        

elif choice == 4: 
            display_sub_menu_title("도서 대여 / 반납")
      
            target_isbn = get_string("대여/반납을 희망하는 도서의 ISBN을 입력하세요.:")

            if target_isbn not in isbn_set:
                print("해당 ISBN을 가진 도서를 찾을 수 없습니다.")

            else:
                for book in books:
                    if book.get_isbn() == target_isbn:
                        target_info = book.display_info()
                        target_book_status = book.get_status()
                        print(target_info)

                        if target_book_status:
                            print("해당 도서는 대여중인 도서입니다.")
                            want_return = get_valid_integer("도서를 반납하시겠습니까?\n(예 = 1 , 아니오 = 2)\n:")

                            if want_return == 1:
                                 book.set_status(False)
                                 print("[안내] 도서의 반납이 완료되었습니다. 감사합니다.")

                            elif want_return == 2:
                                print("[안내] 반납을 취소합니다.")

                            else:
                                print("[경고] 올바른 숫자를 공백없이 입력해주세요")

                        else:
                            print(f"[도서 정보] {target_info}\n해당 도서는 대여가 가능합니다.")

                            want = get_valid_integer("도서 대여를 원하시나요?\n(예 = 1 , 아니오 = 2)\n:")

                            if want == 1:
                                # 도서 대여
                                book.set_status(True) 
                                print(f"도서 대출이 완료되었습니다. 대출 기한은 30일 입니다.:\n{target_info}")

                            elif want == 2:
                                # 메인화면으로 돌아가기
                                print("도서 대여를 취소합니다.")
        

                            else:
                                print("[경고] 올바른 숫자를 공백없이 입력해주세요.")

