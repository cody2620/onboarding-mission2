from game import QuizGame

print("Hello Quiz")

def main():
    game = QuizGame()

    while True:
        print("제목")
        print("퀴즈 출제")
        print("퀴즈 등록")
        print("퀴즈 목록")
        print("점수 확인")
        print("종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            game.start_quiz()

        elif choice == '2':
            game.add_quiz()

        elif choice == '3':
            game.show_quiz()

        elif choice == '4':
            game.show_myscore()

        elif choice == '5':
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("\n 잘못된 입력입니다.")

if __name__ == "__main__": 
    main()