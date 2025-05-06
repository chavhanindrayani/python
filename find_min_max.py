def find_min_max(numbers):
    if not numbers:
        return None
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

nums = [4,1,9,7,3]
result = find_min_max(nums)
if result:
    print("smallest :{result[0]}, largest :{result[1]}")
else:
    print("the list is empty.")
    
    
    
# find the second last largest number
"""nums = [10, 20, 4, 45, 99]
nums.sort()
print(nums[-2])"""
