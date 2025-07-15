# 给你一个非负整数数组 nums 和一个整数 target 。 
# 
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ： 
# 
#  
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。 
#  
# 
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], target = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 20 
#  0 <= nums[i] <= 1000 
#  0 <= sum(nums[i]) <= 1000 
#  -1000 <= target <= 1000 
#  
# 
#  Related Topics 数组 动态规划 回溯 👍 2116 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    target = None
    nums = None
    visited = set()
    zero = set()
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.target = target
        self.nums = nums
        for i,num in enumerate(nums):
            if num == 0:
                self.nums[i] = 1
                self.zero.add(i)
        return self.dfs(0)

    def sum(self):
        res = 0
        for i,num in enumerate(self.nums):
            if i not in self.zero:
                res += num
        return res
    def dfs(self,index):
        count = 0
        if self.sum() == self.target and tuple(self.nums) not in self.visited:
            self.visited.add(tuple(self.nums))
            count += 1
        if index >= len(self.nums):
            return count
        count += self.dfs(index + 1)
        self.nums[index] = -self.nums[index]
        count += self.dfs(index + 1)
        self.nums[index] = -self.nums[index]
        return count

a = Solution()
print(a.findTargetSumWays([0], 0))
# leetcode submit region end(Prohibit modification and deletion)
