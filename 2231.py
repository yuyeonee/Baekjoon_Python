n = input()

start = 1 
if len(n)>2: # 세자리 숫자부터는 9*len(n) 해도 음수가 안 나온다 
    start = int(n)-9*(len(n)) # 한자리, 두자리 숫자는 음수 나와서 분리해줘야됨

answer = 0 # 생성자 못 찾았으면 0으로 나가도록
for i in range(start, int(n)):
    sum = i # 생성자 대상 숫자 일단 더하기
    for c in str(i):
        sum += int(c) # 분해합 더하기
    if sum == int(n):
        answer = i # 같으면 answer 갱신하고 빠져나가기
        break

print(answer)