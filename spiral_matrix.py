
'''Матрица заполненная числами с 1 по n^2, начинающая с левого верхнего угла и закрученной по часовой стрелке'''

n = int(input())
matrix = [[None] * n for i in range(n)] # генерируем матрицу
num = 1    # число которое присваиваем элементам массива
start = 0  # точка старта для цикла
end = n    # конечная итерация
for i in range(end):    # проходим по верхней не заполненной части
    for j in range(start, end):
        if num > n**2: break    # если число  больше его квадрата, значит матрица заполнена и прерываем цикл
        matrix[i][j] = num
        num += 1
        if j + 1 == end:        # если следующая итерация вызодит за пределы матрицы или ячейка уже заполнена, меняем направление
            for k in range(start+1, end):   # то же самое по правой части
                if num > n**2: break
                matrix[k][j] = num
                num += 1
                if k + 1 == end:
                    for l in range(end-2, start-1, -1): # по нижней(справа налево)
                        if num > n**2: break
                        matrix[k][l] = num
                        num += 1
                        if l - 1 == start-1:
                            for m in range(end-2, start, -1):   # левая часть(снизу наверх)
                                if num > n**2: break
                                matrix[m][l] = num
                                num += 1
    start += 1 # увеличиваем точку старта для цикла, чтобы не присвоить другое значение заполненной ячейке
    end -= 1   # уменьшаем по той же причине
for i in range(n):
    for j in range(n):                      # выводим результат
        print(matrix[i][j], end='\t')
    print()