data = input()
length = len(data)
result = 0

for i in range(length // 2):
    result += int(data[i])

for i in range(length // 2, length):
    result -= int(data[i])

if result == 0:
    print("LUCKY")
else:
    print("READY")