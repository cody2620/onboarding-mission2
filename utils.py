# 공통 입력 검증 함수 모음.
# 메뉴 선택, 퀴즈 등록, 정답 입력 등 문자열/숫자 입력이 필요한 모든 곳에서 재사용한다.

# 빈 문자열(공백만 입력 포함)이 아닌 값이 들어올 때까지 재입력받는다
def get_non_empty_string(prompt):
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("⚠️ 내용을 입력해 주세요")
            continue
        return raw


# min_val ~ max_val 범위의 정수 하나를 받을 때까지 재입력받는다.
# 검증 순서: 빈 입력 -> 숫자 변환 실패 -> 허용 범위 밖
def get_valid_number(prompt, min_val, max_val):
    while True:
        raw = input(prompt).strip()

        # 1. 빈 입력 처리
        if raw == "":
            print("⚠️ 번호를 입력해 주세요.")
            continue

        # 2. 숫자 변환 실패 처리
        try:
            number = int(raw)
        except ValueError:
            print(f"⚠️ 숫자만 입력해 주세요. (예: {min_val})")
            continue

        # 3. 허용 범위 밖 처리
        if not (min_val <= number <= max_val):
            print(f"⚠️ {min_val} ~ {max_val} 사이의 숫자를 입력해 주세요.")
            continue

        # 모든 검증 통과
        return number