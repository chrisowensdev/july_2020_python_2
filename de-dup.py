list1 = [1, 2, 3, 4, 4, 4, 5, 5]
unique = []

for num in list1:
    if num not in unique:
        unique.append(num)
    else:
        continue

print(unique)
