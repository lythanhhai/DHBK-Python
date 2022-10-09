def ReplaceList(list1, list2):
    list3 = []
    for i in range(0, len(list1)):
        if i != len(list1) - 1:
            list3.append(list1[i])
    return list3+ list2

print(ReplaceList([1, 3, 5, 7, 9, 10], [2, 4 , 6, 8]))