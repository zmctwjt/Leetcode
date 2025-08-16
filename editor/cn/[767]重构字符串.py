# 给定一个字符串 s ，检查是否能重新排布其中的字母，使得两相邻的字符不同。 
# 
#  返回 s 的任意可能的重新排列。若不可行，返回空字符串 "" 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "aab"
# 输出: "aba"
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "aaab"
# 输出: ""
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 500 
#  s 只包含小写字母 
#  
# 
#  Related Topics 贪心 哈希表 字符串 计数 排序 堆（优先队列） 👍 568 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from heapq import *
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        heap = [[-v, k] for k, v in cnt.items()]
        heapify(heap)
        prev = [0,'']
        ans = []
        while heap[0][0]:
            prev = heapreplace(heap,prev)
            prev[0] += 1
            ans.append(prev[1])
        return '' if prev[0] else ''.join(ans)
# leetcode submit region end(Prohibit modification and deletion)
