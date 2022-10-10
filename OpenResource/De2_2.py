def mergeDict(input_list):
    result = {}
    for i in range(len(input_list)):
        for key, value in input_list[i].items():
            result[key] = value
    return result
print(mergeDict([{"1": 10, "2": 20}, {"1": 30, "4": 40}, {"5": 50, "6": 60}]))
