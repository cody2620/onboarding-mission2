# 퀴즈 한 문제를 표현하는 클래스.
# 문제 데이터(question/choices/answer)와 그 데이터를 다루는 동작(출력, 채점, 변환)을
# 한 곳에서 책임진다. QuizGame은 이 클래스의 메서드만 호출하고 내부 속성을 직접 다루지 않는다.
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question   # 문제 텍스트
        self.choices = choices     # 보기 목록 (기본 4개)
        self.answer = answer       # 정답 번호 (1~4)

    # 문제와 보기 출력. index가 있으면 "[N번 문제]" 형태(목록 조회용),
    # 없으면 번호 없이 출력(퀴즈 풀이용)
    def display(self, index=None):
        if index is not None:
            print(f"\n[{index}번 문제] {self.question}")
        else:
            print(f"\n {self.question}")

        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    # 사용자가 입력한 답과 정답을 비교해 True/False 반환
    def check_answer(self, user_answer):
        return user_answer == self.answer

    # Quiz 객체 -> dict 변환 (state.json 저장용)
    def to_dict(self):
        return{
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    # dict -> Quiz 객체 변환 (state.json 불러오기용)
    @staticmethod
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])