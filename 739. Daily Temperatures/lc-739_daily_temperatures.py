class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = n  * [0]
        s = []

        for i , t in enumerate(temperatures):
            while s and s[-1][1] < t:
                s_index , s_value = s.pop()
                result[s_index] = i - s_index
            s.append((i,t))
        return result

    # Not Optimized solution
    
    # def dailyTemperatures(self, temperatures):
    #     n = len(temperatures)
    #     result = [0] * n
    #     stack = []

    #     for i in range(n):
    #         while stack and temperatures[i] > temperatures[stack[-1]]:
    #             prev = stack.pop()
    #             result[prev] = i - prev

    #         stack.append(i)

    #     return result

    # def dailyTemperatures(self, temperatures):
    #     """
    #     :type temperatures: List[int]
    #     :rtype: List[int]
    #     """
    #     if len(temperatures) == 1  :
    #         return [0]
    #     if len(temperatures) == 0:
    #         return []
    #     i = 0 ; j = i+1
    #     l = []
    #     while i < len(temperatures):
    #         if j == len(temperatures):
    #             j = i+1
    #             l.append(0)
    #             i+=1

    #         if i == len(temperatures):
    #             return l

    #         if temperatures[j] > temperatures[i]:
    #             c = j - i 
    #             l.append(c)
    #             i+=1
    #             j = i+1
    #         else:
    #             j+=1


    # def dailyTemperatures(self, temperatures):
    #     n = len(temperatures)
    #     result = [0] * n
    #     stack = []

    #     for i in range(n):
    #         while stack and temperatures[i] > temperatures[stack[-1]] :
    #             index = stack.pop()
    #             result[index] = i - index
    #         stack.append(i)
    #     return result

if __name__ == "__main__":
    list = [73,74,75,71,69,72,76,73]
    # list =  [30, 40, 50, 60]

    sol = Solution()

    result = sol.dailyTemperatures(list)

    print(result)