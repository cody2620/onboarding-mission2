import json
from quiz import Quiz
from utils import get_valid_number
from utils import get_non_empty_string

class QuizGame:
    def __init__(self):
        # 프로그램 실행 중에만 유지되는 퀴즈 리스트
        self.quiz_list = []
        self.best_score = 0
        self.load_from_json()

    # json에서 데이터 불러오기
    def load_from_json(self):

        # 기본 데이터
        default_quiz = [{
            "question": "다음 중 파이썬의 self에 대한 설명으로 사실이 아닌 것은?", 
            "choices": ["인스턴스(객체) 자기 자신을 가리킨다.", "클래스 내의 함수를 정의할 때 첫 번째 매개변수는 관례적으로 self를 사용한다.", "(오답)메서드를 호출할 때, 사용자가 직접 self 자리에 인수를 전달해야 한다.", "self를 통해 클래스 내부에서 인스턴스 변수에 접근하거나 값을 수정할 수 있다."],
            "answer": 3
                    }]

        try:
            with open('state.json', 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 퀴즈 데이터 정상 로드
            self.quiz_list = [Quiz.from_dict(quiz) for quiz in data["quiz_list"]]
            self.best_score = data["best_score"]

            print(f"✅ 저장된 데이터 로드 완료! (퀴즈: {len(self.quiz_list)}개, 최고점: {self.best_score}점)")
            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # 파일이 없거나(FileNotFoundError) 깨졌을 때(JSONDecodeError) 공통 처리
            if isinstance(e, FileNotFoundError):
                print("⚠️ state.json 파일을 찾을 수 없어 기본 데이터를 로드합니다.")
            else:
                print("⚠️ state.json 파일이 손상되어 기본 데이터로 복구합니다.")

            # 기본 데이터로 객체 생성 및 할당
            self.quiz_list = [Quiz.from_dict(q) for q in default_quiz]
            self.best_score = 0

            # 복구된 데이터 다시 저장
            self.save_to_json()

    # JSON에 데이터 저장하기
    def save_to_json(self):
        data={
            "quiz_list": [quiz.to_dict() for quiz in self.quiz_list],
            "best_score": self.best_score
        }

        with open('state.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print("✅ 데이터가 저장되었습니다")

    # 1. [기능 분리] 목록 보기 (전체 흐름 관리)
    def show_quiz(self):
        print("\n--- 등록된 퀴즈 목록 ---")
        
        # 퀴즈가 하나도 없는 경우 예외 처리
        if not self.quiz_list:
            print("등록된 퀴즈가 없습니다. 퀴즈를 등록해 주세요!")
            return

        # 리스트를 돌면서 각 퀴즈를 출력 (일꾼 메서드 호출)
        for i, quiz in enumerate(self.quiz_list, 1):
            self._display_quiz_item(i, quiz)

    # 2. [기능 분리] 퀴즈 하나를 출력하는 전담 메서드 (보조 일꾼)
    def _display_quiz_item(self, index, quiz):
        print(f"\n[{index}번 문제] {quiz.question}")
        for j, choice in enumerate(quiz.choices, 1):
            print(f"  {j}. {choice}")
        print(f"정답: {quiz.answer}")

    # 퀴즈 등록
    def add_quiz(self):
        print("\n--- 새로운 퀴즈 등록 ---")
        question = get_non_empty_string("질문 입력: ")
        
        choices = []
        for i in range(1, 5):
            choice =  get_non_empty_string(f"보기 {i}번을 입력하세요: ")
            choices.append(choice)

        answer = get_valid_number("정답인 번호를 입력하세요: ", 1, 4)
        
        # Quiz 객체 생성 및 리스트에 추가
        new_quiz = Quiz(question, choices, answer)    
        self.quiz_list.append(new_quiz)
        self.save_to_json()

        print("\n✅ 퀴즈가 성공적으로 등록되었습니다!")

    def show_myscore(self):
        print(f"\n현재까지 최고 점수: {self.best_score}점")

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

        if score > self.best_score:
            self.best_score = score
            print("🏆 최고 점수 갱신 🏆")
            self.save_to_json()

    def ask_question(self, quiz):
        print(f"\n {quiz.question}")

        for i, choice in enumerate(quiz.choices, start=1):
            print(f"{i}. {choice}")

        answer = get_valid_number("\n 정답: ", 1, len(quiz.choices))

        if answer == quiz.answer:
            print("\n⭕ 정답입니다 ⭕")
            return True
        else:
            print("\n❌ 오답입니다 ❌")
            return False