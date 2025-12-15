import random
def mergeSorted(li1, li2):
   li1.sort()
   li2.sort()
   print(f"Sorted list 1{li1}, Sorted list 2 {li2}")
   merged = []
   i = 0
   j = 0 
   while i < len(li1) and j < len(li2):
        if li1[i] < li2[j]:
            merged.append(li1[i])   
            i = i + 1
        else:
            merged.append(li2[j])  
            j = j + 1

   while i < len(li1):
        merged.append(li1[i])       
        i = i + 1

   while j < len(li2):
        merged.append(li2[j])      
        j = j + 1

   return merged

li1 = []
li2 = []
for i in range(5):
    li1.append(random.randint(1, 10))
    li2.append(random.randint(1, 10))
print(li1, li2)

result  = mergeSorted(li1, li2)
print(result)