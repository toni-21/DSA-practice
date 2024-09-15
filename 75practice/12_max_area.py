def maxArea(height: list[int]) -> int:
    maxArea = 0
    i = 0
    j = len(height) - 1

    while i < j:
        l = min(height[i], height[j])
        b = j - i
        maxArea = max(maxArea, (l * b))
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return maxArea


answer = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print("answer is:")
print(answer)
