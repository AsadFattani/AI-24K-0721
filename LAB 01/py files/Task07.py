def find_repeated_numbers(nums):
    repeated = []
    for i in range(len(nums)):
        if nums[i] not in repeated:
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count > 1:
                repeated.append(nums[i])
    return repeated

numbers = [1, 2, 3, 2, 4, 3, 1, 6]
result = find_repeated_numbers(numbers)
print("Repeated numbers:", result)
