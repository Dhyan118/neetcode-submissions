class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for ch in s:
            if ch.isalnum():              # keep only letters and digits
                cleaned += ch.lower()      # convert to lowercase for case-insensitive check

        # Step 2: Use two pointers to check palindrome
        l, r = 0, len(cleaned) - 1
        while l < r:
            if cleaned[l] != cleaned[r]:   # mismatch means not a palindrome
                return False
            l += 1
            r -= 1

        # Step 3: If loop completes, it's a palindrome
        return True