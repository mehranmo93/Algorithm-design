class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_index={}
        for i , num in enumerate(nums):
            if num in num_index and i - num_index[num] <= k:
                return True
            num_index[num] = i
        return False