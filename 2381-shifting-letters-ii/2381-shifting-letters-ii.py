class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff_array = [0] * (len(s) + 1)
        
        for shift in shifts:
            start, end, direction = shift
            
            if direction == 1:
                diff_array[start] += 1
                diff_array[end + 1] -= 1

            else:
                diff_array[start]  -= 1
                diff_array[end + 1] += 1

        prefix_sum = 0
        result = []

        for idx in range(len(s)):
            prefix_sum += diff_array[idx]
            shift = prefix_sum
            new_char = chr((ord(s[idx]) - 97 + shift) % 26 + 97) # 97 is the ord('a')

            result.append(new_char)
        
        return "".join(result)   