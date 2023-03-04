
table = [list(map(int, input().split())) for _ in range(9)] # 테이블 만들기 

best = 0
ansrow, anscol = 0, 0
for row in range(9):
    for col in range(9):
        if best <= table[row][col]: # 테이블 쓰기
            best = table[row][col]
            ansrow = row + 1
            anscol = col + 1
            
print(best)
print(ansrow, anscol)