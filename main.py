import math
array = list(map(float, input('Введите последовательность чисел через пробел: ').split()))
max = -1.0
c = 3
sum = 0
i1 = 0
proizv = 1
for i in range(0, len(array)):
    if array[i] > c:
        sum = sum + 1
print("Количество чисел большие С=3: ", sum)

for i in range(0, len(array)):
    if abs(array[i]) > max:
        max = abs(array[i])
        i1 = i

for i in range(i1 + 1, len(array)):
    proizv = proizv * array[i]
print("Произведение чисел после максимального по модулю элемента: ", proizv)

def shellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array
print("Сортировка методом Шелла: ", shellSort(array))