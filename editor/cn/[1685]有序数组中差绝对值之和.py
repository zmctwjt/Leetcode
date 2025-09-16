# 给你一个 非递减 有序整数数组 nums 。 
# 
#  请你建立并返回一个整数数组 result，它跟 nums 长度相同，且result[i] 等于 nums[i] 与数组中所有其他元素差的绝对值之和。 
# 
#  换句话说， result[i] 等于 sum(|nums[i]-nums[j]|) ，其中 0 <= j < nums.length 且 j != i （
# 下标从 0 开始）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,5]
# 输出：[4,3,5]
# 解释：假设数组下标从 0 开始，那么
# result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4，
# result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3，
# result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,4,6,8,10]
# 输出：[24,15,13,15,21]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= nums[i + 1] <= 10⁴ 
#  
# 
#  Related Topics 数组 数学 前缀和 👍 78 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from itertools import accumulate


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        perfix = list(accumulate(nums))
        return [(nums[i]*(i+1)-sum_)+(perfix[-1]-sum_-(len(perfix)-i-1)*nums[i])  for i,sum_ in enumerate(perfix)]
# leetcode submit region end(Prohibit modification and deletion)
