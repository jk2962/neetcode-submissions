class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) - 1

        while left < right:

            if heights[left] < heights[right]:
                area = max(area, heights[left] * (right-left))
                left += 1

            else:
                area = max(area, heights[right] * (right-left))
                right -= 1

            
        return area

            



        