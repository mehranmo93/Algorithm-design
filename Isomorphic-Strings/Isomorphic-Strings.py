class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):  # If lengths are not equal, they cannot be isomorphic
            return False
        
        mapping_s_t = {}  # Dictionary to store mapping from characters in s to characters in t
        mapping_t_s = {}  # Dictionary to store mapping from characters in t to characters in s
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # If character from s is already mapped but to a different character from t, or vice versa, not isomorphic
            if char_s in mapping_s_t and mapping_s_t[char_s] != char_t:
                return False
            if char_t in mapping_t_s and mapping_t_s[char_t] != char_s:
                return False
            
            # If character from s is not mapped yet, map it to character from t
            if char_s not in mapping_s_t:
                mapping_s_t[char_s] = char_t
            # If character from t is not mapped yet, map it to character from s
            if char_t not in mapping_t_s:
                mapping_t_s[char_t] = char_s
        #print mapping_s_t
        return True