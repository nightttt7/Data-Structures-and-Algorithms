# Brute Force, O(n^2)
def maxArea(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = (j-i)*min(height[i], height[j])
            if area > max_area:
                max_area = area
    return max_area


# two pointers, O(n), the key is to get clear why it works
def maxArea(height):
    max_area = 0
    left = 0
    right = len(height)-1
    while left < right:
        area = (right-left)*min(height[right], height[left])
        if area > max_area:
            max_area = area
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area
