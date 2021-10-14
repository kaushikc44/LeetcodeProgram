#Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            string = s
            listwithcharacters = []
            def looping(k, j):
                while k != len(string):

                    chartse = string[k]
                    if j == len(string):
                        break
                    else:
                        for i in range(j, len(string)):
                            if string[i] in chartse:
                                listwithcharacters.append(chartse)
                                chartse = ""


                            else:chartse += string[i]
                    j += 1
                    k += 1
                    looping(k,j)

                looping(0, 1)
                a_list = max(set(listwithcharacters),key=len)
                return len(a_list)
