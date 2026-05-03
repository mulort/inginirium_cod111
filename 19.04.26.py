'''a = []
while True:
    rost = input('введите рост')
    if rost == "!":
        break
    if int(rost) >= 160 and int(rost) <= 180:
        a.append(rost)

print(len(a))
print(min(a), max(a))
'''

'''n = list(map(int, input().split()))
for i in range(len(n)):
    print('*' * n[i])'''

h = int(input())
for i in range(h):
    print(' ' * (h - i) + '*' * ((i * 2) + 1))
