a = input()
b = input()
 
if a == b:
    print('ничья')
elif a == 'камень' and b == 'ножницы':
    print('первый')
elif a == 'ножницы' and b == 'бумага':
    print('первый')
elif a == 'бумага' and b == 'камень':
    print('первый')
elif a == 'камень' and b == 'бумага':
    print('второй')
elif a == 'бумага' and b == 'ножницы':
    print('второй')
elif a == 'ножницы' and b == 'камень':
    print('второй')
elif a == 'камень' and b == 'ром':
    print('первый')
elif a == 'ром' and b == 'пират':
    print('первый')
elif a == 'пират' and b == 'ножницы':
    print('первый')
elif a == 'ножницы' and b == 'ром':
    print('первый')
elif a == 'ром' and b == 'бумага':
    print('первый')
elif a == 'пират' and b == 'камень':
    print('первый')
elif a == 'ром' and b == 'камень':
    print('второй')
elif a == 'пират' and b == 'ром':
    print('второй')
elif a == 'ножницы' and b == 'пират':
    print('второй')
elif a == 'ром' and b == 'ножницы':
    print('второй')
elif a == 'бумага' and b == 'ром':
    print('второй')
elif a == 'камень' and b == 'пират':
    print('второй')
elif a == 'бумага' and b == 'пират':
    print('первый')
elif a == 'пират' and b == 'бумага':
    print('второй')