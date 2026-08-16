from game import QuizGame
from utils import get_valid_number

print("🎮 퀴즈 실행 🎮")

def main():
    game = QuizGame()

    try:
        while True:
            print("\n 📌 Home 📌 \n")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 등록")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")

            choice = get_valid_number("\n👉 메뉴를 선택하세요: ", 1, 5)

            if choice == 1:
                game.start_quiz()

            elif choice == 2:
                game.add_quiz()

            elif choice == 3:
                game.show_quiz()

            elif choice == 4:
                game.show_myscore()

            elif choice == 5:
                game.save_to_json()
                print("\n프로그램을 종료합니다.")
                break
            # else:
            #     print("\n 잘못된 입력입니다.")
    except KeyboardInterrupt:
        print("\n⚠️ 프로그램이 중단되었습니다.")
        game.save_to_json()
        print("\n 데이터를 저장했습니다.")

    except EOFError:
        print("\n⚠️ 입력이 종료되었습니다.")
        game.save_to_json()
        print("\n 데이터를 저장했습니다.")

if __name__ == "__main__": 
    main()