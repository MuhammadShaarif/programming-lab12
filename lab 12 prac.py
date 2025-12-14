# Function to perform Selection Sort
def selection_sort(arr):
 # Loop through all elements in the array
 for i in range(len(arr)):
 # Assume the current position holds the minimum
  min_index = i
 # Loop to find the smallest element in the remaining unsorted array
  for j in range(i + 1, len(arr)):
     if arr[j] < arr[min_index]:
       min_index = j # Update min_index if smaller element found

 # Swap the found minimum element with the first unsorted element
  arr[i], arr[min_index] = arr[min_index], arr[i]

 return arr
# Take input from user at runtime
nums = list(map(int, input("Enter numbers separated by space: ").split()))
# Call selection_sort and print the result
print("Sorted list:", selection_sort(nums))