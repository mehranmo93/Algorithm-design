class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Count occurrences of each letter in ransomNote and magazine
        ransomNoteCounts = {}
        magazineCounts = {}
        
        for char in ransomNote:
            ransomNoteCounts[char] = ransomNoteCounts.get(char, 0) + 1
        
        for char in magazine:
            magazineCounts[char] = magazineCounts.get(char, 0) + 1
        
        # Check if magazine has enough of each letter to construct ransomNote
        for char, count in ransomNoteCounts.items():
            if magazineCounts.get(char, 0) < count:
                return False
        
        return True