#코드업 기초100제(파이썬)
#6077번 : [기초-종합] 짝수 합 구하기(설명)(py)

n = int(input())
a=[]

for i in range(1,n+1):
    if i %2 ==0:
        a.append(i)
print(sum(a))
