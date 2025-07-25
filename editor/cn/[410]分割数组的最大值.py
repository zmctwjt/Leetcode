# 给定一个非负整数数组 nums 和一个整数 k ，你需要将这个数组分成 k 个非空的连续子数组，使得这 k 个子数组各自和的最大值 最小。 
# 
#  返回分割后最小的和的最大值。 
# 
#  子数组 是数组中连续的部份。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [7,2,5,10,8], k = 2
# 输出：18
# 解释：
# 一共有四种方法将 nums 分割为 2 个子数组。 
# 其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,4,5], k = 2
# 输出：9
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,4,4], k = 3
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 10⁶ 
#  1 <= k <= min(50, nums.length) 
#  
# 
#  Related Topics 贪心 数组 二分查找 动态规划 前缀和 👍 1058 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
