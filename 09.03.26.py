'''pomidori = True
ogurci = True
smetana = False

if (pomidori or ogurci) and smetana:
    print('сегодня будет салат')
else:
    print('сегодня салата не будет')

salat = True
pomidori = True
kurica = True
suhariki = True
sir = True
sous = True

if salat and pomidori and kurica and suhariki and sir and sous:
    print('цезарь готов')
else:
    print('цезарь не будет')'''

'''red = input('3')
yelloe = input('2')
green = input('1')

if red == 'красный' and yelloe == 'желтый' and green == 'зеленый':
    print('поехали')
else:
    print('стой')'''

игрок1 = input('игрок 1')
игрок2 = input('игрок 2')

if игрок1 == 'камень' and игрок2 == 'ножницы':
    print('игрок 1 выиграл!')
elif игрок1 == 'бумага' and игрок2 == 'камень':
    print('игрок 1 выиграл!')
elif игрок1 == 'ножницы' and игрок2 == 'бумага':
    print('игрок 1 выиграл')
elif игрок1 == 'камень' and игрок2 == 'камень':
    print('ничья')
elif игрок1 == 'бумага' and игрок2 == 'бумага':
    print('ничья')
elif игрок1 == 'ножницы' and игрок2 == 'ножницы':
    print('ничья')
else:
    print('игрок 2 выиграл!')
