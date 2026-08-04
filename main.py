import json
import os
from game import QuizGame

print("🎮 퀴즈 실행 🎮")

def init_game_state():
    # 게임 시작 시 state.json 초기화
    if not os.path.exists('state.json'):
        # 1. 퀴즈 저장할 공간(빈 배열) 2. 최고점 초기값(0점)
        init_data = {
            "quiz_list": [],
            "best_score": 0
        }
        with open('state.json', 'w') as f:
            json.dump(init_data, f, indent=2)
        print("✅ state.json 파일이 생성되었습니다.")
    
def main():
    init_game_state()
    game = QuizGame()

    # 저장된 데이터 불러오기
    game.load_from_json() 
    
    while True:
        print("\n 📌 Home 📌 \n")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 등록")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

        choice = input("\n👉 메뉴를 선택하세요: ")

        if choice == '1':
            game.start_quiz()

        elif choice == '2':
            game.add_quiz()
            game.save_to_json()

        elif choice == '3':
            game.show_quiz()

        elif choice == '4':
            game.show_myscore()

        elif choice == '5':
            game.save_to_json()
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("\n 잘못된 입력입니다.")

if __name__ == "__main__": 
    main()