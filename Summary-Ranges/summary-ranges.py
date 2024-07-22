class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            
            if nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append("{}->{}".format(start, end))
                start = nums[i]
                
        
        # Handle the last range
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append("{}->{}".format(start, nums[-1]))
        
        return ranges