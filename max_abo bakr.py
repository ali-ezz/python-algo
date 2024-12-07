
def MaximumProduct(nums):
    max1 = max2 = max3 = float()
    min1 = min2 = float()
    for num in nums:
        if num > max1:
            max3, max2, max1 = max2, max1, num
        elif num > max2:
            max3, max2 = max2, num
        elif num > max3:
            max3 = num
        if num < min1:
            min2, min1 = min1, num
        elif num < min2:
            min2 = num
    prod1 = max1 * max2 * max3
    prod2 = max1 * min1 * min2
    if prod1 > prod2:
        return prod1
    else:
        return prod2

s = int(input("Enter size of array: "))
nums = [float(input(f"Enter element {i + 1}: ")) for i in range(s)]
if s <= 3:  # best case
    maxp = 1
    for i in range(s):
        maxp *= nums[i]
    print(f"The maximum product is:{maxp}")
else:
    print(f"The maximum product is: {MaximumProduct(nums):.1f}")