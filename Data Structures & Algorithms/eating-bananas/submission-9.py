class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        min_k = right

        while left <= right:
            mid = (left + right) // 2
        
            hour_count = 0

            for i in piles:
                hour_count += (i + mid - 1) // mid

            if hour_count <= h:
                min_k = mid
                right = mid - 1
        
            elif hour_count > h:
                left = mid + 1

        return min_k