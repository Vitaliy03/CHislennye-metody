a = -2 #задаем переменную, означающую один конец отрезка
b = 2 #задаем переменную, означающую другой конец отрезка
c1 = 0 #задаем переменную, означающую значение функции в точке a
c2 = 0 #задаем переменную, означающую значение функции в точке b
while (c1 * c2) >= 0: #цикл поиска отрезка, значения на концах которого принимают противоположные знаки
    a += 1 
    b -= 1
    c1 = (a ** 5) - (a ** 3)
    c2 = (b ** 5) - (b ** 3)
d = (a+b)/2 #середина отрезка
c3 = (d ** 5) - (d ** 3) #нахождение значения функции в середине отрезка
if (c3 == 0):
    print (d)
    #продолжаем исследование на двух оставшихся отрезках
    c3 = 1 #меняем значение c3 для дальнейшей работы
    d1 = d
    d2 = d
    while c3 != 0: #поиск корня на одном отрезке
        d1 = (a+d1)/2
        c3 = (d1 ** 5) - (d1 ** 3)
    c3 = 1
    while c3 != 0: #поиск корня на другом отрезке
        d2 = (b+d2)/2
        c3 = (d2 ** 5) - (d2 ** 3)
    print (d1) #вывод результата
    print (d2) #вывод результата
else:
    while c3 != 0:
        if (c1 * c3) < 0: #проверка значений функции на концах одной половины отрезка
            a = a
            b = d #изменение значения конца отрезка
            d = (a+d)/2
            c1 = (a ** 5) - (a ** 3)
            c3 = (d ** 5) - (d ** 3)
        if (c2 * c3) < 0: #проверка значений функции на концах другой половины отрезка
            a = d #изменение значения начала отрезка
            b = b
            d = (d+b)/2
            c2 = (b ** 5) - (b ** 3)
            c3 = (d ** 5) - (d ** 3)
        print (d) #вывод результата