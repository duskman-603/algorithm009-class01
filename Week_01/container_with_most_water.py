class Solution:
    # 这种方法超时，需要优化
    def maxArea(self, nums):
        n = len(nums)
        res = []
        if n < 2:
            return
        else:
            for i in range(n-1):
                left = i + 1
                for j in range(left, n):
                    area = (j-i)*min(nums[j], nums[i])
                    res.append(area)
            return max(res)
    # leetcode 给出的双指针方法
    def maxArea_01(self, height):
        n = len(height)
        if n < 2:
            return
        max_area = 0
        left = 0
        right = n-1
        while left < right:
            area = min(height[left], height[right])*(right-left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

