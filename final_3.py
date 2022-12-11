#T:O(n), S:O(1)
class Solution:
    def removeParentheses(self, s):
        s_list = list(s)
        flag = 0
        for i in range(len(s_list)):
            if s_list[i] = "(":
                flag += 1
            elif  s_list[i] = ")":
                if flag > 0:
                    flag -= 1
            else:
                s_list[i] = ""

       flag = 0
       for i in range(len(s_list)-1, -1, -1):
            if s_list[i] = ")":
                flag += 1
            elif s_list[i] = "(":
                if flag > 0:
                    flag -= 1
            else:
                s_list[i] = ""

       return "".join(s_list)
