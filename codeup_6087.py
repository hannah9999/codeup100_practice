#코드업 기초100제(파이썬)
#6087 : [기초-종합] 3의 배수는 통과(설명)(py)

n = int(input())

for i in range(n+1):
    if i%3 == 0:
        continue
    print(i, end=' ')