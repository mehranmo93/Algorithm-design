class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Initialize the prefix to the first string in the list
        prefix = strs[0]
        
        # Iterate over the list of strings
        for s in strs[1:]:
            # Reduce the length of the prefix until it matches the start of the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
        