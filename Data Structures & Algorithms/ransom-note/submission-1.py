class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hashMap = {}

        for c in magazine:
            hashMap[c] = hashMap.get(c, 0) + 1
        
        for c in ransomNote:
            if hashMap.get(c, 0) == 0:
                return False
            hashMap[c] -= 1
        
        return True