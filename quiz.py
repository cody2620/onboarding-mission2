class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

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