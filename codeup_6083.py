#코드업 파이썬 기초 100제
#6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)

r, g ,b = map(int,input().split())
count = 0


for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)

            count += 1
print(count)