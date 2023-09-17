rows = 7
columns = 7

two_dimensional_array = []

for i in range(rows):
    row = []
    for j in range(columns):
        # вибір 1 або 0 в залежності від індексу (парності)
        value = 1 if (i + j) % 2 == 0 else 0
        row.append(value)
    two_dimensional_array.append(row)

for row in two_dimensional_array:
    print(' '.join(map(str, row)))