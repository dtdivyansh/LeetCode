class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while(len(self.q1)>1):
            self.q2.append(self.q1.pop(0))
        a = self.q1.pop(0)
        self.q1 = self.q2.copy()
        self.q2 = []
        return a
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if(self.q1):
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
