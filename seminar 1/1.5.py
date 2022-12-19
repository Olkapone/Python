# . Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# AB = √(xb - xa)2 + (yb - ya)2

from math import sqrt

if __name__ == '__main__':
    xa = int(input())
    ya = int(input())
    xb = int(input())
    yb = int(input())
    ab = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
    print('%.3f' % ab)
