# 给你一个数组 target 和一个整数 n。 
# 
#  给你一个空栈和两种操作： 
# 
#  
#  "Push"：将一个整数加到栈顶。 
#  "Pop"：从栈顶删除一个整数。 
#  
# 
#  同时给定一个范围 [1, n] 中的整数流。 
# 
#  使用两个栈操作使栈中的数字（从底部到顶部）等于 target。你应该遵循以下规则： 
# 
#  
#  如果整数流不为空，从流中选取下一个整数并将其推送到栈顶。 
#  如果栈不为空，弹出栈顶的整数。 
#  如果，在任何时刻，栈中的元素（从底部到顶部）等于 target，则不要从流中读取新的整数，也不要对栈进行更多操作。 
#  
# 
#  请返回遵循上述规则构建 target 所用的操作序列。如果存在多个合法答案，返回 任一 即可。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：target = [1,3], n = 3
# 输出：["Push","Push","Pop","Push"]
# 解释：一开始栈为空。最后一个元素是栈顶。
# 从流中读取 1 并推入数组 -> [1]
# 从流中读取 2 并推入数组 -> [1,2]
# 从栈顶删除整数 -> [1]
# 从流中读取 3 并推入数组 -> [1,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：target = [1,2,3], n = 3
# 输出：["Push","Push","Push"]
# 解释：一开始栈为空。最后一个元素是栈顶。
# 从流中读取 1 并推入数组 -> [1]
# 从流中读取 2 并推入数组 -> [1,2]
# 从流中读取 3 并推入数组 -> [1,2,3]
#  
# 
#  示例 3： 
# 
#  
# 输入：target = [1,2], n = 4
# 输出：["Push","Push"]
# 解释：一开始栈为空。最后一个元素是栈顶。
# 从流中读取 1 并推入数组 -> [1]
# 从流中读取 2 并推入数组 -> [1,2]
# 由于栈（从底部到顶部）等于 target，我们停止栈操作。
# 从流中读取整数 3 的答案不被接受。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= target.length <= 100 
#  1 <= n <= 100 
#  1 <= target[i] <= n 
#  target 严格递增 
#  
# 
#  Related Topics 栈 数组 模拟 👍 130 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        target_index = 0
        q = []
        for i in range(1,n+1):
            if target_index >= len(target):
                break
            q.append("Push")
            if target[target_index] == i:
                target_index += 1
                stack.append(i)
            else:
                q.append("Pop")
        return q



# leetcode submit region end(Prohibit modification and deletion)
