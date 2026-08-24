# 하위 도서 클래스
from .base_book import BaseBook

class PaperBook(BaseBook):
    def __init__(self,title, author, isbn, pages, location):
        super().__init__(title, author, isbn, pages)
        self.__location = location

    def display_info(self):
        base_info = super().display_info()
        return f"""[일반도서] {base_info}
        위치: {self.__location} 층

        """


class EBook(BaseBook):
    def __init__(self,title, author, isbn, pages, ftype, size):
        super().__init__(title, author, isbn, pages)
        self.__ftype = ftype
        self.__size = size

    def display_info(self):
        base_info = super().display_info()
        return f"""[전자도서] {base_info}
        형식: {self.__ftype}
        크기: {self.__size} MB

        """