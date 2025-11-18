# 给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：nums = [1,0,0,0,1,0,0,1], k = 2
# 输出：true
# 解释：每个 1 都至少相隔 2 个元素。 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：nums = [1,0,0,1,0,1], k = 2
# 输出：false
# 解释：第二个 1 和第三个 1 之间只隔了 1 个元素。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= k <= nums.length 
#  nums[i] 的值为 0 或 1 
#  
# 
#  Related Topics 数组 👍 49 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
# leetcode submit region end(Prohibit modification and deletion)
