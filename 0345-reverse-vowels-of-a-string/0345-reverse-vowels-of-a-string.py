class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = [char for char in s]

        vowels = set('aeiouAEIOU')
        left, right = 0, len(arr) - 1

        while left < right:
            #move the left pointer till we reach the vowel
            while left < right and arr[left] not in vowels:
                left += 1

            #move the right pointer till we reach a vowel to swap with the one under the left pointer
            while left < right and arr[right] not in vowels:
                right -=1

            # we swap the vowels at which both pointers stand over
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

        return "".join(arr)

         

        