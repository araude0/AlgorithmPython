n = int(input())
array = list(map(int, input().split()))
array.sort()
count = 0
result = 0

for i in array:
    count += 1
    if i <= count:
        result += 1
        count = 0

print(result)