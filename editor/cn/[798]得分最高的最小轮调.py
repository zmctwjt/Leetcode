# 给你一个数组 nums，我们可以将它按一个非负整数 k 进行轮调，这样可以使数组变为 [nums[k], nums[k + 1], ... nums[
# nums.length - 1], nums[0], nums[1], ..., nums[k-1]] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。 
# 
#  
#  例如，数组为 nums = [2,4,1,3,0]，我们按 k = 2 进行轮调后，它将变成 [1,3,0,2,4]。这将记为 3 分，因为 1 > 0 
# [不计分]、3 > 1 [不计分]、0 <= 2 [计 1 分]、2 <= 3 [计 1 分]，4 <= 4 [计 1 分]。 
#  
# 
#  在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 k 。如果有多个答案，返回满足条件的最小的下标 k 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,1,4,0]
# 输出：3
# 解释：
# 下面列出了每个 k 的得分：
# k = 0,  nums = [2,3,1,4,0],    score 2
# k = 1,  nums = [3,1,4,0,2],    score 3
# k = 2,  nums = [1,4,0,2,3],    score 3
# k = 3,  nums = [4,0,2,3,1],    score 4
# k = 4,  nums = [0,2,3,1,4],    score 3
# 所以我们应当选择 k = 3，得分最高。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,3,0,2,4]
# 输出：0
# 解释：
# nums 无论怎么变化总是有 3 分。
# 所以我们将选择最小的 k，即 0。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] < nums.length 
#  
# 
#  Related Topics 数组 前缀和 👍 260 👎 0
from itertools import accumulate


# leetcode submit region begin(Prohibit modification and deletion)
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= i & -i
        return ans

    def range(self,l,r):
        if l > r:
            return 0
        l = max(l, 1)
        r = min(r, self.n)
        return self.query(r) - self.query(l-1)

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        a = max(nums)
        b = min(nums)
        perfix_right = Fenwick(a+n-b+1)
        for i,num in enumerate(nums):
            perfix_right.update(i-num+a+1,1)
        perfix_left = Fenwick(a+n-b+1)
        max_ = 0
        ans = 0
        for i,num in enumerate(nums):
            t = perfix_right.range(i+a+1,a+n-b+1) +perfix_left.range(i-n+a+1,a+n-b+1)
            perfix_right.update(i-num+a+1,-1)
            perfix_left.update(i-num+a+1,1)
            if t > max_:
                max_ =  t
                ans = i
        return ans
# leetcode submit region end(Prohibit modification and deletion)
