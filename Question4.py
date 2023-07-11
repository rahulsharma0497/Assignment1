def plusOne(digits):
    n = len(digits)
    carry = 1  # Initial carry is 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry

        if digits[i] <= 9:
            carry = 0
            break
        else:
            digits[i] = 0

    if carry == 1:
        digits.insert(0, 1)

    return digits


# Example usage
digits = [1, 2, 3]
result = plusOne(digits)
print("Output:", result)