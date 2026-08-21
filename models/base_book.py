# 상위 도서 클래스

class BaseBook:
    def __init__(self, title, author, isbn, pages):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__pages = pages
        self.__is_borrowed = False
        
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_pages(self):
        return self.__pages

    def get_status(self):
        return self.__is_borrowed

    def set_status(self, status):
        self.__is_borrowed = status

    def display_info(self):
        status = "대여 중" if self.__is_borrowed else "대여 가능"


        return (f"""도서명: {self.get_title}
        저자: {self.get_author}
        ISBN: {self.get_isbn}
        쪽수: {self.get_pages}
        [{status}]
          """)
    

  