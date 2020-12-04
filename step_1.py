candy = ['Шоколадная', 'Каромельная', 'Мармеладная', 'Смешаная', 'Трюфельная']
print('Шоколадная - 1, Каромельная - 2, Мармеладная - 3, Смашаня - 4, Трюфельная - 5')
hp = input('Если какая-то конфета не нравится напиши её номер, начиная с 0:')
if hp == '1':
    candy.pop(0)
    print(candy)
elif hp == '2':
    candy.pop(1)
    print(candy)
elif hp == '3':
    candy.pop(2)
    print(candy)
elif hp == '4':
    candy.pop(3)
    print(candy)
elif hp == '5':
    candy.pop(4)
    print(candy)
else:
    print('Такого нет в спске!')
gh = input('Желаете увеличить список?')
if gh == 'Нет':
    print('Наслаждайтесь тем что есть!')
elif gh == 'нет':
    print('Наслаждайтесь тем что есть!')
elif gh == 'Да':
    fv = input('Какую кофету вы хотите добавить?')
elif gh == 'да':
    fv = input('Какую кофету вы хотите добавить?')
else:
    print('Вы ошиблись!')
candy.append(fv)
print(candy)
