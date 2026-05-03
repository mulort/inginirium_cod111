'''from_user = input('привет, что нового?')
if len(from_user) > 30:
    print('мне сейчас некогда читать столько много букв..')
    print('мама зовёт кушать, чуть позже обязательно прочту')
else:
    print('Оу, вот оно что.. ну здорово')'''

'''mood = input('привет, как ты?')
if 'хорошо' in mood:
    print('ура')
elif 'отлично' in mood:
    print('ура')
elif 'плохо' in mood:
    print('Всё будет хорошо')'''

'''print(chr(125))
print(ord('%'))
print(chr(ord('a') + 3))'''

'''name = input('')
if len(name) < 4:
    print('ошибка')
else:
    print(name[3])'''

name1 = input('введите слово')
name2 = input('введите слово')
print(name1[-1])
print(name2[0])
if name1[-1] == name2[0]:
    print('верно')
else:
    print('ошибка')