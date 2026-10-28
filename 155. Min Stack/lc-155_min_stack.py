
class MinStack(object):

    def __init__(self):
        self.s = []
        self.stk = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """

        if len(self.stk) == 0 or value <= self.stk[-1]:
            self.stk.append(value)

        return self.s.append(value)
        
    def pop(self):
        """
        :rtype: None
        """

        if self.s[-1] == self.stk[-1]:
            b = self.stk.pop()
            a = self.s.pop()
            return a
        else:
            return self.s.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.stk[-1]

        
# Not OPtimized        
        
# class MinStack(object):

#     def __init__(self):
#         self.s = []
#         self.stk = []

#     def push(self, value):
#         """
#         :type value: int
#         :rtype: None
#         """
         
#         if len(self.stk) > 0:
#             if value > self.stk[-1]:
#                 self.stk.append(value)
#             else:
#                 self.stk.append(value)
#         else:
#             self.stk.append(value)
#         if len(self.stk) > 0:
#             print("STACK : ",self.stk[-1])
#         self.s.append(value)

        

#     def pop(self):
#         """
#         :rtype: None
#         """
#         if len(self.s) == 0:
#             return "empty"
#         print("stack : ",self.stk)
#         a = self.s.pop()
#         if a == self.stk[-1]:
#             self.stk.pop()
#         return a
        

#     def top(self):
#         """
#         :rtype: int
#         """
#         if len(self.s) == 0:
#             return "empty"
        
#         return self.s[-1]
        

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.stk[-1]

#         # if len(self.s) == 0:
#         #     return "empty"
#         # l = []
#         # min = self.s[-1]
#         # while self.s:
#         #     a = self.s.pop()
#         #     l.append(a)
#         #     if min > a:
#         #         min = a
#         # while l:
#         #     a = l.pop()
#         #     self.s.append(a)
#         # return min
#         # return self.minimun
            

# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(value)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()

if __name__ == "__main__":
    stack = MinStack()

    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    print("Minimum:", stack.getMin())  # Expected: -3

    stack.pop()

    print("Top:", stack.top())         # Expected: 0
    print("Minimum:", stack.getMin())  # Expected: -2

    stack.push(-5)

    print("Top:", stack.top())         # Expected: -5
    print("Minimum:", stack.getMin())  # Expected: -5

    stack.pop()

    print("Top:", stack.top())         # Expected: 0
    print("Minimum:", stack.getMin())  # Expected: -2