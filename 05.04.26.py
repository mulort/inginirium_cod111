'''name = 'Inginirim'
for index in range(len(name)):
    print(name[index], end='')

name = 'Inginirim'
print('In' in name)
if 'iri' in name:
    print('+')
else:
    print('-')

name = 'Inginirium'
for Ietter in name:
    print(Ietter, end=)

name = 'Inginirium'
print(name[0:4:1])
print(name[4:0:-1])
print(name[:])
print(name[::-1])

name = input('введите слово')
for index in name:
    print(ord(index), end=',')'''

stroka = input()

p = 0
for letter in stroka:
  if letter == 'p':
    p += 1
