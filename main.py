# 진입점: 메뉴 출력 → 입력받기 → QuizGame 메서드 호출을 반복하는 흐름 제어만 담당
from game import QuizGame
from utils import get_valid_number

print("🎮 퀴즈 실행 🎮")

def main():
    game = QuizGame()  # 생성 시점에 state.json을 자동으로 불러옴 (game.py 참고)

    try:
        while True:
            print("__________\n")
            print("📌 Home 📌 \n")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 등록")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")

            # get_valid_number가 공백/문자/범위 밖/빈 입력을 모두 걸러주므로
            # 여기서는 1~5 중 하나라는 것이 보장된 값만 받는다
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

    # Ctrl+C / 입력 스트림 종료 시에도 비정상 종료 대신 저장 후 안전하게 빠져나온다
    except KeyboardInterrupt:
        print("\n--------------------------------")
        print("\n⚠️  프로그램이 중단되었습니다.")
        game.save_to_json()

    except EOFError:
        print("\n--------------------------------")
        print("\n⚠️  입력이 종료되었습니다.")
        game.save_to_json()

if __name__ == "__main__":
    main()