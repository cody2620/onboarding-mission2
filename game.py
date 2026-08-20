import json
from quiz import Quiz
from utils import get_valid_number
from utils import get_non_empty_string

# 게임 전체를 관리하는 클래스.
# 퀴즈 목록/최고점수 등 상태를 들고, 메뉴별 기능(풀기/등록/목록/점수)과
# state.json 저장·불러오기를 담당한다. 개별 문제의 출력/채점은 Quiz에 위임한다.
class QuizGame:
    def __init__(self):
        self.quiz_list = []     # Quiz 객체 리스트
        self.best_score = 0     # 최고 점수
        self.has_played = False # 퀴즈를 한 번이라도 풀었는지 여부 (0점과 미플레이 구분용)
        self.load_from_json()   # 생성 시점에 state.json에서 상태를 복원

    # === 파일 입출력 ===

    # state.json에서 데이터 불러오기.
    # 파일이 없거나(FileNotFoundError) 손상됐으면(JSONDecodeError) 기본 퀴즈로 복구한다.
    def load_from_json(self):

        # 파일이 없거나 손상됐을 때 사용할 기본 퀴즈 데이터
        default_quiz = [
            {
                "question": "다음 중 파이썬의 self에 대한 설명으로 사실이 아닌 것은?",
                "choices": ["인스턴스(객체) 자기 자신을 가리킨다.", "클래스 내의 함수를 정의할 때 첫 번째 매개변수는 관례적으로 self를 사용한다.", "(오답)메서드를 호출할 때, 사용자가 직접 self 자리에 인수를 전달해야 한다.", "self를 통해 클래스 내부에서 인스턴스 변수에 접근하거나 값을 수정할 수 있다."],
                "answer": 3
            },
            {
                "question": "다음 중 파이썬에서 사용할 수 있는 올바른 변수명은?",
                "choices": ["7th_player", "my name", "_my_score", "if"],
                "answer": 3
            },
            {
                "question": "다음 중 사용자로부터 데이터를 입력받을 때 사용하는 함수는?",
                "choices": ["output()", "input()", "print()", "scan()"],
                "answer": 2
            },
            {
                "question": "파이썬에서 주석 처리할때 사용하는 특수문자가 아닌 것은?",
                "choices": [" # ", " '' ", " \"\" ", " // "],
                "answer": 4
            },
            {
                "question": "다음 변수 a에 담긴 값의 자료형은? a = \"2024\" ",
                "choices": ["int 정수", "str 문자열", "bool 불리언", "dict 딕셔너리"],
                "answer": 2
            },
            {
                "question": "다음 중 list에 해당하는 보기는?",
                "choices": ["colors = \"red\", \"blue\"", "colors = {\"red\", \"blue\"}", "colors = [\"red\", \"blue\"]", "colors = {\"red\": \"blue\"}"],
                "answer": 3
            }
        ]

        try:
            with open('state.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 퀴즈 데이터 정상 로드
            self.quiz_list = [Quiz.from_dict(quiz) for quiz in data["quiz_list"]]
            self.best_score = data["best_score"]
            self.has_played = data.get("has_played", False)

            print(f"✅ 저장된 데이터 로드 완료! (총 퀴즈: {len(self.quiz_list)}개, 최고점: {self.best_score}점)")
            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # 파일이 없거나(FileNotFoundError) 깨졌을 때(JSONDecodeError) 공통 처리
            if isinstance(e, FileNotFoundError):
                print("⚠️ state.json 파일을 찾을 수 없어 기본 데이터를 로드합니다.")
            else:
                print("⚠️ state.json 파일이 손상되어 기본 데이터로 복구합니다.")

            # 기본 데이터로 객체 생성 및 할당
            self.quiz_list = [Quiz.from_dict(q) for q in default_quiz]
            self.best_score = 0
            self.has_played = False

            # 복구된 데이터 다시 저장
            self.save_to_json()

    # 현재 상태(퀴즈 목록/최고점수/플레이 여부)를 state.json에 통째로 덮어쓴다.
    # 퀴즈 등록/퀴즈 풀이 완료/프로그램 종료 시점마다 호출된다.
    def save_to_json(self):
        data={
            "quiz_list": [quiz.to_dict() for quiz in self.quiz_list],
            "best_score": self.best_score,
            "has_played": self.has_played
        }

        with open('state.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print("✅ 데이터가 저장되었습니다")

    # === 메뉴 기능 ===

    # 3. 퀴즈 목록 조회
    def show_quiz(self):
        print("\n--- 등록된 퀴즈 목록 ---")

        if not self.quiz_list:
            print("등록된 퀴즈가 없습니다. 퀴즈를 등록해 주세요!")
            return

        for i, quiz in enumerate(self.quiz_list, 1):
            self._display_quiz_item(i, quiz)

    # 목록 조회 시 문제 하나를 "번호 + 정답"까지 함께 보여주는 보조 메서드
    def _display_quiz_item(self, index, quiz):
        quiz.display(index)
        print(f"정답: {quiz.answer}")

    # 2. 퀴즈 등록: 문제/보기 4개/정답 번호를 입력받아 Quiz로 만들고 저장
    def add_quiz(self):
        print("\n--- 새로운 퀴즈 등록 ---")
        question = get_non_empty_string("질문 입력: ")
        
        choices = []
        for i in range(1, 5):
            choice =  get_non_empty_string(f"보기 {i}번을 입력하세요: ")
            choices.append(choice)

        answer = get_valid_number("정답인 번호를 입력하세요: ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quiz_list.append(new_quiz)
        self.save_to_json()

        print("\n✅ 퀴즈가 성공적으로 등록되었습니다!")

    # 4. 최고 점수 확인. 한 번도 플레이한 적 없으면 0점 대신 안내 메시지 출력
    def show_myscore(self):
        if not self.has_played:
            print("\n아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어보세요!")
            return

        print(f"\n현재까지 최고 점수: {self.best_score}점")

    # 1. 퀴즈 풀기: 전체 문제를 순서대로 출제하고 채점 → 최고 점수 갱신 → 저장
    def start_quiz(self):
        if not self.quiz_list:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 퀴즈를 등록해주세요.")
            return

        print("\n퀴즈를 시작합니다!")

        score = 0
        for quiz in self.quiz_list:
            if self.ask_question(quiz):
                score += 1
        print(f"\n결과: {score}/{len(self.quiz_list)}")

        self.has_played = True

        previous_best = self.best_score
        print(f"\n내 점수: {score}점 / 최고 점수: {previous_best}점")

        if score > previous_best:
            self.best_score = score
            print("🏆 최고 점수 갱신 🏆")
        else:
            print("최고 점수를 넘지 못했습니다.")

        self.save_to_json()

    # 문제 하나를 출제하고 사용자 답을 받아 채점 결과(True/False)를 반환
    def ask_question(self, quiz):
        quiz.display()

        answer = get_valid_number("\n 정답: ", 1, len(quiz.choices))

        if quiz.check_answer(answer):
            print("\n⭕ 정답입니다 ⭕")
            return True
        else:
            print("\n❌ 오답입니다 ❌")
            return False