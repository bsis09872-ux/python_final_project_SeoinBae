# 하위 도서 클래스
from .base_book import BaseBook

class PaperBook(BaseBook):
    def __init__(self,title, author, isbn, pages, types, location):
        super().__init__(self, title, author, isbn, pages)
        self.__types = types
        self.__location = location

    def display_info(self):
        base_info = super().display_info()
        return f"""{base_info}
        유형: {self.__types} 도서
        위치: {self.__location} 층

        """


class EBook(BaseBook):
    def __init__(self,title, author, isbn, pages, types, ftype, size):
        super().__init__(self, title, author, isbn, pages)
        self.__types = types
        self.__ftype = ftype
        self.__size = size

    def display_info(self):
        base_info = super().display_info()
        return f"""{base_info}
        유형: {self.__types} 도서
        형식: {self.__ftype}
        크기: {self.__size} MB

        """