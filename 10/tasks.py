numbers = [2, 4, 6, 8, 10]
product = 1
for n in numbers:
    if n % 4 == 0:
        product *= n
print(product)
