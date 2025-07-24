# 给你一组多米诺骨牌 dominoes 。 
# 
#  形式上，dominoes[i] = [a, b] 与 dominoes[j] = [c, d] 等价 当且仅当 (a == c 且 b == d) 或者 
# (a == d 且 b == c) 。即一张骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌。 
# 
#  在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i,
#  j) 的数量。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= dominoes.length <= 4 * 10⁴ 
#  dominoes[i].length == 2 
#  1 <= dominoes[i][j] <= 9 
#  
# 
#  Related Topics 数组 哈希表 计数 👍 174 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        d = defaultdict(int)
        for i in dominoes:
            a = tuple(sorted(i))
            ans += d[a]
            d[a] += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
