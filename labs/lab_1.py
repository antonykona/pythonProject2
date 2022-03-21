x, y = float(input('Введите Х точки=')), float(input('Введите Y точки='))
xs1, ys1 = float(input('Х1 прямой=')), float(input('Y1 прямой='))
xs2, ys2 = float(input('X2 прямой=')), float(input('Y2 прямой='))
k = float((ys1 - ys2) / (xs1 - xs2))
b = float(ys2 - k * xs2)
print('y=', k, '*x+', b)
teor_y = k * x + b
if y == k * x + b:
    print('Точка лежит на прямой')
elif y > teor_y:
    print('Точка выше заданной прямой')
else:
    print('Точка ниже заданной прямой')

xp1, yp1 = float(input('X1 прямоугольник=')), float(input('Y1 прямоугольника='))
xp2, yp2 = float(input('X2 прямоугольника=')), float(input('Y2 прямоугольника'))
if xp1 < xp2 and yp1 > yp2:
    if (x > xp1) and (y > yp2) and (x < xp2) and (y < yp1):
        print('Точка лежит внутри прямоугольника')
    elif (x == xp1 and y >= yp2 and y <= yp1) or (x == xp2 and y >= yp2 and y <= yp1) or (
            y == yp1 and x >= xp1 and x <= xp2) or (y == yp2 and x >= xp1 and x <= xp2):
        print('Точка лежит на границе прямоугольника')
    else:
        print('Точка находится вне прямоугольника')
elif xp1 < xp2 and yp1 < yp2:
    if (x > xp1) and (y > yp1) and (x < xp2) and (y < yp2):
        print('Точка лежит внутри прямоугольника')
    elif (x == xp1 and y >= yp1 and y <= yp2) or (x == xp2 and y <= yp2 and y >= yp1) or (
            y == yp1 and x >= xp1 and x <= xp2) or (y == yp2 and x >= xp1 and x <= xp2):
        print('Точка лежит на границе прямоугольника')
    else:
        print('Точка находится вне прямоугольника')
elif xp1 > xp2 and yp1 < yp2:
    if (x > xp2) and (y > yp1) and (x > xp2) and (y < yp2):
        print('Точка лежит внутри прямоугольника')
    elif (x == xp1 and y >= yp1 and y <= yp2) or (x == xp2 and y >= yp1 and y <= yp2) or (
            y == yp1 and x >= xp2 and x <= xp1) or (y == yp2 and x >= xp2 and x <= xp1):
        print('Точка лежит на границе прямоугольника')
    else:
        print('Точка находится вне прямоугольника')
elif xp1 > xp2 and yp1 > yp2:
    if (x > xp2) and (y > yp2) and (x < xp1) and (y < yp1):
        print('Точка лежит внутри прямоугольника')
    elif (x == xp1 and y >= yp2 and y <= yp1) or (x == xp2 and y >= yp2 and y <= yp1) or (
            y == yp1 and x >= xp2 and x <= xp1) or (y == yp2 and x >= xp2 and x <= xp1):
        print('Точка лежит на границе прямоугольника')
    else:
        print('Точка находится вне прямоугольника')
else:
    print('Это нихера не прямоугольник,а точка')
x = float(x)
y = float(y)
print("Введите центр окружности и его радиус: ")
r = float(input("R = "))
xk = float(input("x(k) = "))
yk = float(input("y(k) = "))
if r>0:
    if (x - xk) ** 2 / r ** 2 + (y - yk) ** 2 / r ** 2 < 1:
        print("Точка находится внутри окружности")
    elif (x ** 2) + (y ** 2) == r ** 2:
        print('Точка лежит на окружности')
    else:
        print("Точка не принадлежит окружности")
else:
    print('Радиус не может быть отрицательным или равным 0')