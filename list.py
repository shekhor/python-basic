def sum_of_elements(nums):
    total = 0
    for num in nums:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
result = sum_of_elements(numbers)
print(result)  # Prints 15
