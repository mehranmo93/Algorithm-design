class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        max_reachable = 0  # This variable keeps track of the farthest index we can reach
        
        for i, jump in enumerate(nums):
            # If we reach a point that is beyond our maximum reachable point, return False
            if i > max_reachable:
                return False
            
            # Update the maximum reachable point from the current position
            max_reachable = max(max_reachable, i + jump)
            
            # If we can already reach or surpass the last index, return True
            if max_reachable >= len(nums) - 1:
                return True
        
        # In case we complete the loop and haven't returned, check if we can reach the last index
        return max_reachable >= len(nums) - 1
            

        