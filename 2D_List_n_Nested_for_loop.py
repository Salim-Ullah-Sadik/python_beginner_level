numbers =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10]
]

print(numbers[0][0])

for row in numbers:
    print(row)

for row in numbers:
    for col in row:
        print(col)
