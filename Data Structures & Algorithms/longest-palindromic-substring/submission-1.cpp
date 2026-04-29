class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        if (n == 0) return "";

        int start = 0;     // starting index of longest palindrome
        int maxLen = 1;    // length of longest palindrome

        // helper function to expand around center
        auto expand = [&](int left, int right) {
            while (left >= 0 && right < n && s[left] == s[right]) {
                left--;
                right++;
            }
            return right - left - 1; // length of palindrome
        };

        // check each index as a potential center
        for (int i = 0; i < n; i++) {
            int len1 = expand(i, i);       // odd-length palindrome
            int len2 = expand(i, i + 1);   // even-length palindrome
            int len = max(len1, len2);

            if (len > maxLen) {
                maxLen = len;
                start = i - (len - 1) / 2;
            }
        }

        return s.substr(start, maxLen);
    }
};