class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1 # initalize the two pointers

        while l < r:
            while l < r and not s[l].isalnum(): # .isalnum skips invalid
                l += 1
            while l < r and not s[r].isalnum(): # same but for right
                r -=1
            if s[l].lower() != s[r].lower(): # never is true if palindrome
                return False
            l += 1 # continues moving the pointers
            r -= 1

        return True


