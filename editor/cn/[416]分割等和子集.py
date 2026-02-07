# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
# 
#  Related Topics 数组 动态规划 👍 2321 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        sum_= sum(nums)
        if sum_ // 2 != sum_/2 or nums[-1] > sum_/2:
            return False
        @cache
        def dfs(i,k):
            if i < 0:
                return False
            if nums[i] == k:
                return True
            elif nums[i] > k:
                return dfs(i-1,k)
            return dfs(i-1,k-nums[i]) or dfs(i-1,k)
        return dfs(len(nums)-1,sum_/2)
        
# leetcode submit region end(Prohibit modification and deletion)
