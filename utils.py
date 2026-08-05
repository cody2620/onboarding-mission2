def get_valid_number(prompt, min_val, max_val):
    """
    숫자 입력을 검증하는 공통 함수
    - prompt  : 입력 안내 문구
    - min_val : 허용 최솟값
    - max_val : 허용 최댓값
    """
    while True:
        raw = input(prompt).strip()

        # 1. 빈 입력 처리
        if raw == "":
            print("⚠️ 값을 입력해 주세요.")
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