# 给你一个整数数组 arr 和一个整数 k 。现需要从数组中恰好移除 k 个元素，请找出移除后数组中不同整数的最少数目。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [5,5,4], k = 1
# 输出：1
# 解释：移除 1 个 4 ，数组中只剩下 5 一种整数。
#  
# 
#  示例 2： 
# 
#  输入：arr = [4,3,1,1,3,3,2], k = 3
# 输出：2
# 解释：先移除 4、2 ，然后再移除两个 1 中的任意 1 个或者三个 3 中的任意 1 个，最后剩下 1 和 3 两种整数。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  1 <= arr[i] <= 10^9 
#  0 <= k <= arr.length 
#  
# 
#  Related Topics 贪心 数组 哈希表 计数 排序 👍 131 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = sorted(Counter(arr).values())
        ans = len(cnt)
        for v in cnt:
            k -= v
            if k < 0:
                break
            ans -= 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)
