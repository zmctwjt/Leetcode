# 有 n 个项目，每个项目或者不属于任何小组，或者属于 m 个小组之一。group[i] 表示第 i 个项目所属的小组，如果第 i 个项目不属于任何小组，则 
# group[i] 等于 -1。项目和小组都是从零开始编号的。可能存在小组不负责任何项目，即没有任何项目属于这个小组。 
# 
#  请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表： 
# 
#  
#  同一小组的项目，排序后在列表中彼此相邻。 
#  项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个
# 项目左侧）应该完成的所有项目。 
#  
# 
#  如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[
# 3,6],[],[],[]]
# 输出：[6,3,4,1,5,2,0,7]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[
# 3],[],[4],[]]
# 输出：[]
# 解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m <= n <= 3 * 10⁴ 
#  group.length == beforeItems.length == n 
#  -1 <= group[i] <= m - 1 
#  0 <= beforeItems[i].length <= n - 1 
#  0 <= beforeItems[i][j] <= n - 1 
#  i != beforeItems[i][j] 
#  beforeItems[i] 不含重复元素 
#  
# 
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 👍 256 👎 0
from collections import deque, defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m+= 1
        group_g = [[] for _ in range(m+1)]
        group_in_degree = [0] * (m+1)
        items_g = [[] for _ in range(n+1)]
        items_in_degree = [0] * (n+1)
        group_of_items = defaultdict(set)
        for item in range(n):
            gp = group[item]
            group_of_items[gp].add(item)
            for bitem in beforeItems[item]:
                if gp != group[bitem]:
                    group_g[group[bitem]].append(gp)
                    group_in_degree[gp] += 1
                items_g[bitem].append(item)
                items_in_degree[item] += 1
        group_sort = []
        group_dq = deque(gp for gp,d in enumerate(group_in_degree) if not d)
        while group_dq:
            gp = group_dq.popleft()
            group_sort.append(gp)
            for p in group_g[gp]:
                group_in_degree[p] -= 1
                if not group_in_degree[p]:
                    group_dq.append(p)
        if len(group_sort) != m+1:
            return []
        ans =[]
        for gp in group_sort:
            item_dq = deque(item for item in group_of_items[gp] if not items_in_degree[item])
            while item_dq:
                item = item_dq.popleft()
                ans.append(item)
                for i in items_g[item]:
                    items_in_degree[i]-=1
                    if not items_in_degree[i] and i in group_of_items[gp]:
                        item_dq.append(i)
        return ans if len(ans) == n else []


# leetcode submit region end(Prohibit modification and deletion)
