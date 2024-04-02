class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert to lowercase and remove non-alphanumeric characters
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the cleaned string is a palindrome
        return cleaned_s == cleaned_s[::-1]