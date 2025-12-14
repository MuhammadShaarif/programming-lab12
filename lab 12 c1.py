def linear_search(datalist, element):
    for index in range(len(datalist)):
        if datalist[index] == element:
            return index
    return "not found"


datalist = [1, 2, 3, 4, 5]
user_search = int(input("Enter a value to search: "))

result = linear_search(datalist, user_search)
print(result)
