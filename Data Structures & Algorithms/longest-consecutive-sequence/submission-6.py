class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums) # create our hash set
        longest = 0 # set longest as 0

        for n in nums: # go through each number in nums
            if (n-1) not in numSet: # if number prior not in set, new sequence
                length = 0 # set length of this sequence to 0
                while (n + length) in numSet:
                    length += 1 # update length to see how long sequence is
                longest = max(longest, length) # update longest at sequence
          
        return longest
