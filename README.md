# python_final_project_SeoinBae
파이썬 기초 과제 1 _ 도서관 관리 시스템 CLI (MVP)
---

## 1. 레포 구조:
```
    python_final_project_SeoinBae/
    │
    ├── models/
    │   ├── __init__.py
    │   ├── base_book.py
    │   └── specialized_books.py
    │
    ├── utils/
    │   ├── __init__.py
    │   └── helpers.py
    │
    ├── data/
    │   ├── __init__.py
    │   └── books_info.py       ← sample data (optional)
    │
    ├── src/
    │   └── main.py
    │
    ├── pyproject.toml
    └── uv.lock
```
---

## 2. 실행 화면 (캡쳐본 첨부)


---

## 3. TIL
### Date: 2026-08-19
- 이날은 과제 요구 조건을 처음 제대로 보았다. 문제를 파악하고 어떤 구조로 가야하는지 그림을 그리는게 어려웠다. 
- 우선 필요한 환경을 먼저 세팅했다.
- 그래서 ChatGPT에 어떤 것부터 하는 게 좋을지 물어봤고, 프로젝트의 기본적인 흐름을 공부했다.
    
#### 프로젝트 개발 흐름
    ```
    (1) 환경 구성
    [uv · 가상환경(.venv) · VS Code]
            ↓
    (2) 데이터 구조 설계
    [List · Dictionary · 자료형]
            ↓
    (3) 클래스 설계
    [OOP · Class · 상속 · Getter/Setter]
            ↓
    (4) 샘플 데이터 준비 - (선택적으로 추가)
    [List + Dictionary]
            ↓
    (5) 객체 생성 및 테스트
    [객체(Instance) · Method]
            ↓
    (6) 유틸리티 / 예외 처리
    [함수 · try/except · ValueError]
            ↓
    (7) CLI 메뉴 구현
    [input · while · if/elif]
            ↓
    (8) 기능 연결
    [등록 · 조회 · 검색 · 대여/반납]
            ↓
    (9) 예외 상황 테스트
    [입력 검증 · 중복 ISBN · Debugging]
            ↓
    (10) 최종 정리
    [Module · Package · import]
    ```

### Date: 2026-08-21
- 오늘도 여전히 시작하려니 막막했다. 그래서 우선 샘플 데이터를 만들고, 부모 클래스와 자식 클래스에 들어갈 정보를 주석으로 정리했다. 그리고 키-값을 어떻게 넣을지를 고민했다.
- 샘플데이터를 처음에 models에 넣었다가 패키지라는걸 생각하니 data 폴더를 새로 생성해 관리하는게 맞다는 판단을 했다.
- 부모 클래스를 먼저 작성했다. `__init__ `에는 주요 변수들을 정의했다.
- 아래는 getter를 이용해 정보를 불러오는 함수를 정의하고, is_borrowed라는 대여 여부를 보여주는 변수에 대해서만 setter를 이용해 참일때 '대여중'이라는 조건을 설정해주었다.
- 다음 자식 클래스에는 부모 클래스를 import해온 후 아래에 각각 Ebook과 Paperbook을 각각 클래스로 정의하였다.
- 모든 클래스에는 정보 조회를 위한 `display_info()` 함수가 정의되어 있다. 여기서도 `self` 키워드로 매개변수를 받았기 때문에 문자열 포맷팅할때 중괄호 안에 `self.__title` 이런식으로 self로 받아주어야 한다는걸 다시 배웠다. (그 전에는 `get_title`, `get_title()`, `self.title`등으로 넣었어서 계속 오류가 났다.)
- 현재 시각 오후 8시 48분. 내일은 많이 못하니까 모레 일요일날 완성하자!! 컨디션 관리도 잘 하자 ...!