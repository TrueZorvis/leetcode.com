"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a
bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and
no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source
to destination, or false otherwise.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

"""


class Solution(object):
    def validPath(self, n, edges, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: int
        :type end: int
        :rtype: bool
        """
        visited = [False] * n
        d = {}
        # store the undirected edges for both vertices
        for i in edges:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]

            if i[1] in d:
                d[i[1]].append(i[0])
            else:
                d[i[1]] = [i[0]]
        # create a queue as we will apply BFS
        q = [start]
        while q:
            curr = q.pop(0)  # pop the first element as we do in queue
            if curr == end:  # if its the end then we can return True
                return True
            elif curr in d and not visited[curr]:  # else if it is not the end then check whether its visited or not
                q.extend(d[curr])  # add the adjacent vertices of the current node to the queue
            visited[curr] = True  # mark this curr vertex as visited = True, so that we dont visit this vertex again
        return False  # return False if the queue gets empty and we dont reach the end


s = Solution()
res1 = s.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2)
print(res1)

res2 = s.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5)
print(res2)
