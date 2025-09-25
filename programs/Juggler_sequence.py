class Solution:
    def jugglersequence(self, n):

        if n%2==0:
            return n^1/2
            a=n^1/2
        else:
            return n^3/2
jug=Solution()
jug.jugglersequence(9)
