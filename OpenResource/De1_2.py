def splitStringToDict(input_string):
    dic = dict()
    for w in input_string:
        if w in dic.keys():
            dic[w] = dic[w]+1
        else:
            dic[w] = 1
    return dic

print(splitStringToDict("w3resource"))