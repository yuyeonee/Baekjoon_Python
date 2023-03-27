n = int(input())

for i in range(n):
    sen = list(input().split())
    answer = ''
    for word in sen:
        for i in range(len(word)):
            answer += word[len(word)-1-i]
        answer += ' '
    print(answer)