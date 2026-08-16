class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    # 문제와 보기를 출력
    def display(self, index=None):
        if index is not None:
            print(f"\n[{index}번 문제] {self.question}")
        else:
            print(f"\n {self.question}")

        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    # 사용자가 입력한 답이 정답인지 확인
    def check_answer(self, user_answer):
        return user_answer == self.answer

    # 객체 Quiz를 딕셔러니로 변환(json 저장용)
    def to_dict(self):
        return{
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    # 딕셔너리를 객체 Quiz로 변환(json 불러오기용)
    @staticmethod
    def from_dict(data):
        return Quiz(data["question"], data["choices"], data["answer"])