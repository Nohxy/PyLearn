# игра 21 или в простонародье "очко"
import random
kol = [6,7,8,9,10,2,3,4,11]*4
random.shuffle(kol)
print('Сыграем в очко')
count = 0

while True:
    choice = input('будете брать карту?\n(y - да, n - нет)')
    if choice == 'y':
        current = kol.pop()
        print('Ваша карта = %d' %current)
        count += current
        if count > 21:
            print('Больше чем 21, повезет в другой раз')
            break
        elif count == 21:
            print('Вы выйграли %d' %count)
            break
        else:
            print('У вас %d очков' %count)
    elif choice == 'n':
        print('У вас %d очков и игра закончена' %count)
        break

print('Спасибо за игру')