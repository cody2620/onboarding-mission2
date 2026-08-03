from quiz import Quiz

class QuizGame:
    def __init__(self):
        # 프로그램 실행 중에만 유지되는 퀴즈 리스트입니다.
        self.quizzes = []
        self.best_score = 0

    # 1. [기능 분리] 목록 보기 (전체 흐름 관리)
    def show_quiz(self):
        print("\n--- 등록된 퀴즈 목록 ---")
        
        # 퀴즈가 하나도 없는 경우 예외 처리
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 퀴즈를 등록해 주세요!")
            return

        # 리스트를 돌면서 각 퀴즈를 출력 (일꾼 메서드 호출)
        for i, quiz in enumerate(self.quizzes, 1):
            self._display_quiz_item(i, quiz)

    # 2. [기능 분리] 퀴즈 하나를 출력하는 전담 메서드 (보조 일꾼)
    def _display_quiz_item(self, index, quiz):
        print(f"\n[{index}번 문제] {quiz.question}")
        for j, choice in enumerate(quiz.choices, 1):
            print(f"  {j}. {choice}")
        print(f"정답: {quiz.answer}")

    # 퀴즈 등록 기능
    def add_quiz(self):
        print("\n--- 새로운 퀴즈 등록 ---")
        question = input("질문 입력: ")
        
        choices = []
        for i in range(1, 5):
            choice = input(f"보기 {i}번을 입력하세요: ")
            choices.append(choice)

        answer = input("정답인 번호를 입력하세요: ")

        # Quiz 객체 생성 및 리스트에 추가
        new_quiz = Quiz(question, choices, answer)    
        self.quizzes.append(new_quiz)

        print("\n✅ 퀴즈가 성공적으로 등록되었습니다!")

    def show_myscore(self):
        print(f"\n현재까지 최고 점수: {self.best_score}점")

    def start_quiz(self):
        print("\n퀴즈를 시작합니다!")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0
        for quiz in self.quizzes:
            if self.ask_question(quiz):
                score += 1
        print(f"\n결과: {score}/{len(self.quizzes)}")

        if score > self.best_score:
            self.best_score = score
            print("🏆 최고 점수 갱신 🏆")

    def ask_question(self, quiz):
        print(f"\n {quiz.question}")
        answer = input("정답: ")

        if answer == quiz.answer:
            print("정답")
            return True
        else:
            print("오답")
            return False