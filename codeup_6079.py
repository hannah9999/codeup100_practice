##코드업 기초100제(파이썬)
#6079 : [기초-종합] 언제까지 더해야 할까?(py)

n = int(input())
sum = 0
num =0
while True:
    sum +=num
    num += 1
    if sum >= n:
        print(num - 1)
        break
