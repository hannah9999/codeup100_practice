n = int(input())
sum = 0
num = 0

while True:
    sum += num
    num += 1
    if sum >= n:
        print(sum)
        break
