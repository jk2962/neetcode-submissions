class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for x in nums:
            if x in freq_map:
                freq_map[x] += 1 
            else:
                freq_map[x] = 1
        
        res = []

        for _ in range(k):
            max_ = None

            for x in freq_map:
                if max_ is None:
                    max_ = x
                    continue

                if freq_map[x] > freq_map[max_]:
                    print(x)
                    max_ = x

            res.append(max_)
            del freq_map[max_]

        return res
                

