# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入： heights = [2,4]
# 输出： 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= heights.length <=10⁵ 
#  0 <= heights[i] <= 10⁴ 
#  
# 
#  Related Topics 栈 数组 单调栈 👍 3162 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        st = [-1]
        ans = 0
        for r,h in enumerate(heights):
            while len(st)>1 and heights[st[-1]] > h:
                cur = st.pop()
                ans = max(ans,heights[cur] * (r-st[-1]-1))
            st.append(r)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
