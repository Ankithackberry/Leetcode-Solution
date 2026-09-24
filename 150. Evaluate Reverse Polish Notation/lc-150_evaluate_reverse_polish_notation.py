class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        for t in tokens:
            if t in "+-*/":
                b , a = stk.pop() ,stk.pop()
            if t == '+':
                stk.append(a+b)
            elif t == '-':
                stk.append(a-b)
            elif t == '*':
                stk.append(a*b)
            elif t == '/':
                stk.append(int(a/b))
            else:
                stk.append(int(t))
        return stk.pop()

# LeetCode-style test runner
if __name__ == "__main__":

    solution = Solution()
    
    result = solution.evalRPN(["10","6","9","3","+","-11","/","17","+","5","+"])
    print("Test Case", ":", result)
