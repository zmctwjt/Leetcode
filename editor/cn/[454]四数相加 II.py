# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足： 
# 
#  
#  0 <= i, j, k, l < n 
#  nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# 输出：2
# 解释：
# 两个元组如下：
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1)
#  + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1)
#  + 0 = 0
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums1.length 
#  n == nums2.length 
#  n == nums3.length 
#  n == nums4.length 
#  1 <= n <= 200 
#  -2²⁸ <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2²⁸ 
#  
# 
#  Related Topics 数组 哈希表 👍 1125 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = Counter(a + b for a in nums1 for b in nums2)
        return sum(cnt[-c - d] for c in nums3 for d in nums4)
# leetcode submit region end(Prohibit modification and deletion
