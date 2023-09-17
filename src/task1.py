def even_index_array():
    array = input('Введіть значення масиву через пробіл: ').split()
    array = [int(x) for x in array]
    
    total = 0

    for i in range(len(array)):
        if i % 2 == 0:
            total += array[i]

    return total

result = even_index_array()
print(f'Сума елементів з парними індексами: {result}')
