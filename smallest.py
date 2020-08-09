list1 = [5, 4, 3, 2, 1]

smallest = list1[0]
for num in list1:
    if num < smallest:
        smallest = num

print(smallest)
