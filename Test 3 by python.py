num = input("Введите количество элементов ")
n = list(range(0, int(num)))
result = []
for i in n:
    if ((i % 3) == 0):
        result.append(i)
print( "кратные 3","=" , (result))