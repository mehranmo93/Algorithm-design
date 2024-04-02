class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Split the string into words by spaces
        words = s.strip().split(' ')
        
        # Get the last word
        last_word = words[-1]
        
        # Return the length of the last word
        return len(last_word)
