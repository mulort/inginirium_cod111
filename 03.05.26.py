result = [0, 0, 0]
numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    result[numbers[i] - 1] = i + 1
for i in range(len(result)):
    print(result[i], end=' ')
