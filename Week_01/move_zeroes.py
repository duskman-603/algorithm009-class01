class Solution:

    def move_list(self, nums):
        zero_list = []
        for item in enumerate(nums):
            index, value = item
            if value == 0:
                zero_list.append(0)
                del nums[index]
        return nums + zero_list

    def move_list_01(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
                if i != j:
                    nums[i] = 0
                # print(nums)
        return nums

    def move_list_02(self, nums):
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
        return nums

    def move_zero_03(self, nums):
        i = 0
        k = 0
        while i < len(nums):
            if nums[i] == 0:
                k += 1
                nums.pop(i)
            else:
                i += 1
        nums.extend([0] * k)
        return nums
