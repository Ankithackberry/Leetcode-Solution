class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        print("operations : ",operations)
        stack = []

        for opr in operations:
            if opr == "+":
                stack.append(stack[-1] + stack[-2])
            elif opr == "D":
                stack.append(stack[-1]*2)
            elif opr == "C":
                stack.pop()
            else:
                stack.append(int(opr))

        print(stack)
        return sum(stack)
        # total = 0
        # for i in stack:
        #     total = total +i
        # return total
# ---------- Test Code ----------
if __name__ == "__main__":
    operations = ["5","-2","4","C","D","9","+","+"]
    
    sol = Solution()
    result = sol.calPoints(operations)
    
    print("Input:", operations)
    print("Output:", result)