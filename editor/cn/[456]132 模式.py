# 给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足
# ：i < j < k 和 nums[i] < nums[k] < nums[j] 。 
# 
#  如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：false
# 解释：序列中不存在 132 模式的子序列。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,1,4,2]
# 输出：true
# 解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [-1,3,2,0]
# 输出：true
# 解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 2 * 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics 栈 数组 二分查找 有序集合 单调栈 👍 896 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from math import inf

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = -inf
        for j in range(len(nums)-1,-1,-1):
            if nums[j]< k:
                return True
            while stack and stack[-1] < nums[j]:
                k = max(k,stack.pop())
            stack.append(nums[j])
        return False

# leetcode submit region end(Prohibit modification and deletion)
