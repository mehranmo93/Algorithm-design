class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        jumps = 0
        farthest = 0
        current_end = 0
        
        for i in range(n - 1):  # No need to check the last element
            farthest = max(farthest, i + nums[i])  # Update the farthest we can reach
            if i == current_end:  # Time to make a jump
                jumps += 1
                current_end = farthest  # Update the current range
                if current_end >= n - 1:  # If we can reach or exceed the last index, stop
                    break
        
        return jumps






