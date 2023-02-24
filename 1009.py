n = int(input()) # 반복 횟수

for _ in range(n): # 반복횟수 쓸 때 이렇게 해보자
    a, b = map(int, input().split()) # map으로 입력 정수로 바꾸는 거 한 번에 하기
    a = a%10 # 끝자리 숫자만 보기
    
    if a==1 or a==5 or a==6: # 1개 반복 규칙
        print(a)
    elif a==2 or a==3 or a==8 or a==7: # 4개 반복 규칙
        if b%4==0: # 나머지 0 나올 때 네번째 거로 반영
            print(a**4%10)
        else:
            print(a**(b%4)%10)
    elif a==4 or a==9: # 2개 반복 규칙
        if b%2==0: # 나머지 0 나올 때 두번째 거로 반영
            print((a**2)%10)
        else:
            print(a**(b%2)%10)
    else: # 0일 때 10번 컴퓨터
        print(10)
    



        


    
