list1 = [2, 4, 5]
list2 = [2, 3, 6]
multiplied_list = []

i = 0
while i < len(list1):
    multiplied_list.append(list1[i] * list2[i])
    i += 1

print(str(list1) + " X " + str(list2) + " = " + str(multiplied_list))
