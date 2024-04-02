class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        while not haystack.startswith(needle):
            haystack = haystack[1:]
            i += 1
            if not haystack:
                return -1
        return i