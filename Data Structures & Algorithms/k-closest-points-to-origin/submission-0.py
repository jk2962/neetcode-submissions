class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #create a max-heap
        max_heap = []
        #for each point in points:
        for (x, y) in points:
            #calculate distanc frm origin
            dist = -(x * x + y * y)
            #push (-distance, point) into heap
            heapq.heappush(max_heap, (dist, [x, y]))
            #if heap size > k:
            if len(max_heap) > k:
                #pop from heap
                heapq.heappop(max_heap)
        #return points from heap
        return [point for (_, point) in max_heap]

        
        