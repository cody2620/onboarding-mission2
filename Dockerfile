# 1. 파이썬 가벼운 버전 사용
FROM python:3.11-slim

# 2. 컨테이너 내부 작업 폴더 설정
WORKDIR /app

# 3. 현재 폴더의 모든 파일을 컨테이너 안으로 복사
COPY . .

# 4. 프로그램 실행 (main.py가 실행 파일이라고 가정)
CMD ["python", "main.py"]