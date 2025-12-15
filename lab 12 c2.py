def commonCheck(li1, li2):
    for i in li1:
        for j in li2:
            if i == j:
                return True
    
    return False

l1 = list(map(int, input("Enter any numbers by spacing: ").split()))
l2 = list(map(int, input("Enter any numbers by spacing: ").split()))
print(l1)
print(l2)

common = commonCheck(l1, l2)
print(common)