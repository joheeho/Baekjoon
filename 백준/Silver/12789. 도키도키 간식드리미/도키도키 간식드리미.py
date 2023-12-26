n = int(input())
students = list(map(int, input().split()))

stack = []
expected_order = 1

for student in students:
    # 스택이 비어있지 않고, 스택의 맨 위 값이 기대하는 순서와 같으면
    while stack and stack[-1] == expected_order:
        stack.pop()
        expected_order += 1

    # 현재 학생이 기대하는 순서와 같으면 기대하는 순서 증가
    if student == expected_order:
        expected_order += 1
    else:
        stack.append(student)

# 스택에 남아있는 값들을 처리
while stack:
    if stack[-1] == expected_order:
        stack.pop()
        expected_order += 1
    else:
        break

# 모든 학생이 기대하는 순서로 줄을 세울 수 있는 경우 "Nice", 아니면 "Sad" 출력
if expected_order - 1 == n:
    print("Nice")
else:
    print("Sad")
