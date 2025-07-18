# 给定一个正整数数组 nums和一个整数 k，返回 nums 中 「好子数组」 的数目。 
# 
#  如果 nums 的某个子数组中不同整数的个数恰好为 k，则称 nums 的这个连续、不一定不同的子数组为 「好子数组 」。 
# 
#  
#  例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。 
#  
# 
#  子数组 是数组的 连续 部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,1,2,3], k = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,1,3,4], k = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  1 <= nums[i], k <= nums.length 
#  
# 
#  Related Topics 数组 哈希表 计数 滑动窗口 👍 515 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = left1 = left2 = 0
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        for num in nums:
            cnt1[num] += 1
            cnt2[num] += 1
            while len(cnt1) > k:
                temp = nums[left1]
                cnt1[temp] -= 1
                if not cnt1[temp]:
                    del cnt1[temp]
                left1 += 1
            while len(cnt2) >= k:
                temp = nums[left2]
                cnt2[temp] -= 1
                if not cnt2[temp]:
                    del cnt2[temp]
                left2 += 1
            ans += left2 - left1
        return ans
# leetcode submit region end(Prohibit modification and deletion)
