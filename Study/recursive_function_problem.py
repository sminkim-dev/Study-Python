def flatten(data):
    extra_list = []
    for i in data:
        if type(i) == list:
            extra_list += flatten(i)
        else:
            extra_list.append(i)
    return extra_list
example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본 : ", example)
print("변환 : ",flatten(example))