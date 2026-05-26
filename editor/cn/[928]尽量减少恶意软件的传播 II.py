# 给定一个由 n 个节点组成的网络，用 n x n 个邻接矩阵 graph 表示。在节点网络中，只有当 graph[i][j] = 1 时，节点 i 能够直接
# 连接到另一个节点 j。 
# 
#  一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传
# 播将继续，直到没有更多的节点可以被这种方式感染。 
# 
#  假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。 
# 
#  我们可以从 initial 中 删除一个节点，并完全移除该节点以及从该节点到任何其他节点的任何连接。 
# 
#  请返回移除后能够使 M(initial) 最小化的节点。如果有多个节点满足条件，返回索引 最小的节点 。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输出：0
#  
# 
#  示例 2： 
# 
#  
# 输入：graph = [[1,1,0],[1,1,1],[0,1,1]], initial = [0,1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1]
# 输出：1
#  
# 
#  
# 
#  提示： 
#  
# 
#  
#  n == graph.length 
#  n == graph[i].length 
#  2 <= n <= 300 
#  graph[i][j] 是 0 或 1. 
#  graph[i][j] == graph[j][i] 
#  graph[i][i] == 1 
#  1 <= initial.length < n 
#  0 <= initial[i] <= n - 1 
#  initial 中每个整数都不同 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 数组 哈希表 👍 114 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def dfs(node):
            nonlocal vis,tag
            res = True
            for i,t in enumerate(graph[node]):
                if t and i not in vis and i != tag:
                    if i in initial:
                        if tag == -1:
                            tag = i
                        else:
                            return False
                    else:
                        vis.add(i)
                        res &= dfs(i)
            return res

        initial = set(initial)
        cnt = defaultdict(set)
        ans = min(initial)
        mx = 0
        for node in range(len(graph)):
            if node not in initial:
                vis = set([node])
                tag = -1
                if dfs(node) and tag != -1:
                    cnt[tag] |= vis
                    if len(cnt[tag]) == mx:
                        mx = len(cnt[tag])
                        ans = min(tag,ans)
                    elif len(cnt[tag]) > mx:
                        ans = tag
                        mx  = len(cnt[tag])

        return ans

# leetcode submit region end(Prohibit modification and deletion)
