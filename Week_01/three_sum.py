class Solution:
    #我的解答
    def count_3_sums(self, nums):
        def iteration_bc():
            j = 0
            k = -1
            while j-k <= len(nums_bc)-1:
                b = nums_bc[j]
                c = nums_bc[k]
                if j > 0 or k < -1:

                    if b == nums_bc[j - 1]:

                        j += 1
                        continue
                    if c == nums_bc[k + 1]:
                        k -= 1
                        continue
                if a + b + c == 0:
                    j += 1
                    res.append([a, b, c])
                elif a + b + c < 0:
                    j += 1
                elif a + b + c > 0:
                    k -= 1
        nums.sort()
        print(nums)
        res = []
        for i in range(len(nums)):

            if i == 0:
                a = nums[i]
                nums_bc = nums[1:]
                iteration_bc()
            else:
                if nums[i] == nums[i-1]:
                    continue
                else:
                    a = nums[i]
                    nums_bc = nums[i+1:]
                    iteration_bc()
        return res

    def count_3_sum_01(self, nums):
        n = len(nums)
        res = []
        nums.sort()
        if not nums or n < 3:
            return []
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res
