def waterArea(height: list[int]) -> int:
    maxArea = 0
    left, right = 0, len(height)-1

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        maxArea = max(area, maxArea)
        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1

    return maxArea


answer = waterArea(height=[1, 2, 3, 4, 5])
print("answer is", answer)
