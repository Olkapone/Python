# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*
#
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти
if __name__ == '__main__':
    num = int(input())
    if num == 1:
        print('x > 0 and y > 0')
    elif num == 2:
        print('x < 0 and y > 0')
    elif num == 3:
        print('x < 0 and y < 0')
    elif num == 4:
        print('x > 0 and y < 0')
    else:
        print('There`s no such quarter')