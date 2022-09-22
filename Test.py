# powers = [[1, 2, 3], [4, 5, 6]]

# index = 0

# for row in powers:
#     for num in row:
#         num = num ** num
#         print(num)
#     index = index + 1

# print(powers[1][2])


powers = [[1, 2, 3], [4, 5, 6]]

index = 0


for row in powers:
    for num in row:
        # print(row[index])
        row[index] = pow(row[index], row[index])
        print(row[index])
    index = index + 1
    # index = 0

print(powers[1][2])