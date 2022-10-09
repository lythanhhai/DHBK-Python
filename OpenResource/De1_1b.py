def findMaxList(input_list):
    list1 = []
    for i in range(0, len(input_list)):
        sum1 = sum(input_list[i])
        # for j in range(0, len(input_list[i])):
        #     sum += input_list[i][j]
        list1.append(sum1)
    for i in range(len(list1)):
        if list1[i] == max(list1):
            return input_list[i]

print(findMaxList([[1, 2, 3], [4, 5 , 6], [10, 11, 12], [7, 8, 9]]))