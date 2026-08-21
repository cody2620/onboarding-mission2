
> ## 프로젝트 개요
* 개발환경
  - 사용 언어: Python 3.12.13
  - OrbStack(Docker): Version 2.0.5
  - IDE: Visual Studio Code

> ## 퀴즈 주제와 선정 이유
  * 퀴즈 주제: 파이썬 기초 퀴즈
  * 선정 이유: 파이썬 기초를 공부한 후 복습할 겸 활용해보고 싶었다.

> ## 실행 방법
* python main.py

> ## 기능 목록
* 퀴즈 풀기
* 퀴즈 등록
* 퀴즈 목록 조회
* 최종 점수
* 퀴즈 종료

> ## 파일 구조
```
project-root/
├── 📄 .gitignore  
├── 📄 Dockerfile  : Docker 설정
├── 📄 game.py     : 게임 로직 
├── 📄 main.py     : 메인 프로그램
├── 📄 quiz.py     : 퀴즈 클래스
├── 📄 README.md   
├── 📄 state.json  : 퀴즈 목록, 최고 점수 저장소
└── 📄 utils.py    : 유틸리티 함수
```

> ## git
* git clone 수행 기록
<img width="714" height="130" alt="스크린샷 2026-08-21 오후 2 40 31" src="https://github.com/user-attachments/assets/2c0aebfe-28fe-45db-90e3-eb6039b8948d" />


* git pull 수행 기록
<img width="368" height="31" alt="스크린샷 2026-08-21 오후 2 43 04" src="https://github.com/user-attachments/assets/6dd7bef6-2d2e-42b0-bd75-5122727a4581" />

<br><br>

> ## 데이터 파일 설명

* state.json 경로
  - ./state.json
    
* 역할
  - 퀴즈 데이터와 사용자 최고 기록을 JSON 형식으로 저장
    
* 스키마
  - quiz_list (List): 퀴즈 데이터의 집합
  - question (String): 문제 내용
  - choices (List): 4지 선다형 보기 리스트
  - answer (Int): 정답 번호 (1~4)
  - best_score (Int): 현재까지 기록된 최고 점수
  - has_played(boolean): 0점과 한번도 퀴즈 풀지 않은 사람 구분   

> ## 실행화면 스크린샷

* ### 퀴즈 등록

<img width="1179" height="422" alt="퀴즈 등록" src="https://github.com/user-attachments/assets/77184b45-4dd9-41d0-a85f-a315aa33b1c2" />
<br>

* ### 퀴즈 풀기

<img width="867" height="713" alt="퀴즈풀기" src="https://github.com/user-attachments/assets/ffa57f13-7eae-4085-8b5a-3acdcaead256" />
<br>

* ### 퀴즈 목록 조회
  
<img width="867" height="751" alt="퀴즈목록 조회" src="https://github.com/user-attachments/assets/9f1379fc-002f-41ae-a079-ec2c800864e1" />

* ### 퀴즈 목록이 없을때

<img width="605" height="547" alt="퀴즈목록이 없을때" src="https://github.com/user-attachments/assets/b7241b0c-6f8c-4528-965b-b5895ad25283" />

** **
### ❗오류 및 수정할 것들

8월 2일
- 5를 제외하고 어떤 번호를 넣어도 "잘못된 입력입니다" 가 출력됨

  ✔️그냥 반영이 늦게 된듯

8월 5일
- 퀴즈 등록시 정답을 등록할때 문자를 입력해도 등록이 가능함

- 퀴즈 등록할때 그냥 엔터도 등록이 됨

8월 17일

❗**오류**: state.json 파일이 없는 상태에서 처음 실행해도 기본 퀴즈 데이터가 로드되지 않고, 퀴즈 0개인 빈 상태로 시작됨

- **원인**: `main.py`의 `init_game_state()` 함수가 `QuizGame`을 생성하기 *전에* 먼저 빈 퀴즈 목록(`quiz_list: []`)으로 state.json 파일을 만들어버림. 그러다 보니 `game.py`의 `load_from_json()`이 파일을 읽을 때는 이미 파일이 존재하는 상태라, "파일이 없을 때 기본 퀴즈 데이터를 사용한다"는 예외 처리 코드가 실행될 기회 자체가 없었음

  ✔️두 곳에서 같은 일(파일 초기화)을 나눠서 처리하다 보니, 먼저 실행되는 쪽이 나중 로직을 무력화시킨 경우

- **해결**: `main.py`의 `init_game_state()` 함수와 그 호출을 제거. 파일 생성과 기본 데이터 로드를 `game.py`의 `QuizGame.load_from_json()` 한 곳에서만 담당하도록 정리함. 이제 state.json이 없으면 `FileNotFoundError` 예외 처리 분기가 정상적으로 실행되어 기본 퀴즈 데이터로 파일이 생성됨


❗**수정할 것**: 요구사항에서는 `Quiz` 클래스가 "퀴즈 출력, 정답 확인" 기능까지 갖도록 요구했지만, 실제로는 `Quiz`가 데이터 변환(to_dict/from_dict)만 담당하고, 문제 출력과 정답 비교는 전부 `QuizGame`(game.py)이 `Quiz`의 내부 속성(question, choices, answer)을 직접 꺼내 처리하고 있었음

- **원인**: 클래스 설계 시 "데이터를 담는 역할"과 "데이터를 다루는 동작"을 분리하지 않고, 동작 로직을 전부 `QuizGame` 쪽에만 몰아서 구현함. 그 결과 `Quiz`는 단순 데이터 컨테이너 역할만 하고, `QuizGame`이 `quiz.answer == answer`처럼 다른 객체의 내부 데이터를 직접 들여다보며 비교하는 구조가 됨 (캡슐화 부족)

- **해결**: `Quiz` 클래스에 다음 두 메서드를 추가함
  - `display(index=None)` : 문제와 보기를 출력 (목록 조회 시엔 번호 포함, 퀴즈 풀 때는 번호 없이 출력)
  - `check_answer(user_answer)` : 입력받은 답과 정답을 비교해 True/False 반환


❗**수정할 것**: "점수 확인" 메뉴에서 `show_myscore()`가 `best_score` 값을 조건 없이 그대로 출력함. 그 결과 "아직 한 번도 퀴즈를 풀지 않은 상태(0점)"와 "퀴즈를 풀었는데 전부 틀려서 0점을 받은 상태"가 화면상 똑같이 "최고 점수: 0점"으로 표시되어 구분이 안 됨

- **원인**: `best_score`는 숫자값이라 "점수가 0점"과 "아직 점수 자체가 없음(미플레이)"을 같은 값(0)으로만 표현할 수 있었음. "사용자가 퀴즈를 한 번이라도 풀어봤는지" 여부를 별도로 기록하는 상태값이 없어서 발생한 문제

- **해결**: `state.json` 스키마에 `has_played`(Boolean) 키를 추가함
  - 기본값은 `false`(아직 안 풂)
  - `start_quiz()`로 퀴즈를 한 번이라도 끝까지 풀면 `true`로 바뀌고 저장됨 (최고 점수를 갱신하지 못해도 플레이 여부는 항상 저장)

  `show_myscore()`에서 `has_played`가 `false`면 "아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어보세요!" 안내를 띄우고, `true`일 때만 실제 최고 점수를 출력하도록 수정함. 이제 0점(플레이 후)과 미플레이 상태가 명확히 구분됨

  그리고 `game.py`의 `_display_quiz_item`, `ask_question`이 `quiz.question` / `quiz.answer`를 직접 꺼내 쓰던 부분을 `quiz.display()`, `quiz.check_answer()` 호출로 교체함. 이제 "퀴즈를 어떻게 보여줄지, 정답을 어떻게 확인할지"는 `Quiz` 객체 스스로가 책임지고, `QuizGame`은 그 결과만 받아서 게임 진행에만 집중함



