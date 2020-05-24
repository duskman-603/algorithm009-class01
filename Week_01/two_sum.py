class Solution:
    #先排序
    def two_sum(self, nums, target):
        n = len(nums)
        left = 0
        right = n-1
        new_list = [(nums[index], index) for index in range(n)]
        new_list.sort(key=lambda x: x[0])
        while left < right:
            v = new_list[left][0] + new_list[right][0]
            res = (new_list[left][1], new_list[right][1])
            if v == target:
                return res
            elif v > target:
                right -= 1
            else:
                left += 1
