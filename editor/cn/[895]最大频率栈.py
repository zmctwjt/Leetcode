# 设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。 
# 
#  实现 FreqStack 类: 
# 
#  
#  
#  FreqStack() 构造一个空的堆栈。 
#  
#  void push(int val) 将一个整数 val 压入栈顶。 
#  
#  int pop() 删除并返回堆栈中出现频率最高的元素。 
#  
#  如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop",
# "pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# 输出：[null,null,null,null,null,null,null,5,7,5,4]
# 解释：
# FreqStack = new FreqStack();
# freqStack.push (5);//堆栈为 [5]
# freqStack.push (7);//堆栈是 [5,7]
# freqStack.push (5);//堆栈是 [5,7,5]
# freqStack.push (7);//堆栈是 [5,7,5,7]
# freqStack.push (4);//堆栈是 [5,7,5,7,4]
# freqStack.push (5);//堆栈是 [5,7,5,7,4,5]
# freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
# freqStack.pop ();//返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
# freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
# freqStack.pop ();//返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= val <= 10⁹ 
#  push 和 pop 的操作数不大于 2 * 10⁴。 
#  输入保证在调用 pop 之前堆栈中至少有一个元素。 
#  
# 
#  Related Topics 栈 设计 哈希表 有序集合 👍 435 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
import heapq


class FreqStack:
    def __init__(self):
        self.cnt = defaultdict(int)
        self.stack = []
    def push(self, val: int) -> None:
        if len(self.stack) <= self.cnt[val]:
            self.stack.append([])
        self.stack[self.cnt[val]].append(val)
        self.cnt[val] += 1

    def pop(self) -> int:
        val = self.stack[-1].pop()
        if not self.stack[-1]:
            self.stack.pop()
        self.cnt[val] -= 1
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# leetcode submit region end(Prohibit modification and deletion)
