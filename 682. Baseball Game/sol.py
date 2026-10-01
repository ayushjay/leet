class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum_list = []
        for i in range(len(operations)):
            if operations[i] == "+":
                new_scr = sum_list[-1] + sum_list[-2]
                sum_list.append(int(new_scr))
            elif operations[i] =="D":
                new_scr = sum_list[-1] * 2
                sum_list.append(int(new_scr))
            elif operations[i] == "C":
                sum_list.pop()
            else:
                sum_list.append(int(operations[i]))
        
        return sum(sum_list)

        
"""
easy!!
"""