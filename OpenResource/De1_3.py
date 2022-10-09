def sortTuple(input_list):
    for i in range(len(input_list) - 1):
        for j in range(i + 1, len(input_list)):
            if(input_list[i][1] < input_list[j][1]):
                temp = input_list[i]
                input_list[i] = input_list[j]
                input_list[j] = temp
    return input_list

print(sortTuple([('item1', '12.20'), ('item2', '15.20'), ('item3', '24.20'), ('item4', '12.30')]))