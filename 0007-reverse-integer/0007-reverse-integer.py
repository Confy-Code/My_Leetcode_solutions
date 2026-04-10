class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if len(str(x)) == 1:
            return x

        low = (-2) ** 31
        high = (2 ** 31) - 1

        negative = False
        if x < 0:
            negative = True
            x = x * -1

        x_reversed = str(x)[::-1]

        while x_reversed.startswith("0"):
            x_reversed = x_reversed[1:]

        if negative:
            answer = int(x_reversed) * -1
        else:
            answer = int(x_reversed)
        
        return answer if low <= answer <= high else 0

        