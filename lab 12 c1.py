def search(datalist, userSearch):
    for i in datalist:
        if userSearch == i:
            print("Search Result found!")
            break
    else:
        print("Not found")
datalist = [1, 2, 3, 4, 5]

user_search = int(input("Enter a value to search: "))
search(datalist, user_search)