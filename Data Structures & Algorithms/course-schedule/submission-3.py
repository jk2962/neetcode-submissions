class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph as adjacency list
        graph = defaultdict(list)
        # build in-degree array
        in_degree = [0] *numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        # queue = all courses with in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        # count = 0
        count = 0

        # while queue not empty:
        while queue:
            # course = queue.pop()
            course = queue.popleft()
            # count += 1
            count += 1
            # for neighbor in graph[course]:
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses
        