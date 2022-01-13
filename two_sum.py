class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution 1: O(N^2) time
        # length = len(nums)
        # for i in range(length - 1):
        #     for j in range(i + 1, length):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        # Solution 2: O(N) time 
        length = len(nums)
        h = dict()
        for i in range(length): # O(N) time
            h.update({nums[i] : i}) # O(1) time
        
        for i in range(length): # O(N) time
            new_num = h.get(target - nums[i]) # O(1) time
            if new_num and new_num != i:
                return [i, new_num]
        
