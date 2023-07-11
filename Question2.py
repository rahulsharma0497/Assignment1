def removeElement(nums, val):
    k = 0  # variable to store the count of elements not equal to val

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k


# Example usage
nums = [3, 2, 2, 3]
val = 3
result = removeElement(nums, val)
print("Output:", result)
print("Modified nums:", nums[:result] + ["_*"] * (len(nums) - result))