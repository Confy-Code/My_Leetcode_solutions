class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        diff_arr = [0] * (len(s) + 1)

        for idx in range(len(shifts)):
            diff_arr[0] += shifts[idx]
            diff_arr[idx + 1] -= shifts[idx]

        prefix = 0
        result = []

        for idx in range(len(s)):
            prefix += diff_arr[idx]
            shift = prefix

            new_char = chr((ord(s[idx]) - 97 + shift) % 26 + 97)

            result.append(new_char)

        return "".join(result)

        