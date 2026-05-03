'''print('start')
c = 10 #counter - счётчик
while c != 0:
    print(c)
    c -= 1
print('stop')'''

'''print('start')
c = 100
while c != 0:
    print(c)
    c -= 2
print("stop")'''

'''print('start')
c = 101
while c != 1:
    c -= 2
    if c > 60 or c < 40:
        print(c)
print('stop')'''

c = input('введите пароль')
if '123' in c:
    print('простой')
while c !=8:
    if len(c) > 8:
        print('good')
    if len(c) < 8:
        print('bad')
