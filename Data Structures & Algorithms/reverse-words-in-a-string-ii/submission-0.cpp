class Solution {
public:
    void reverseWords(vector<char>& s) {
        reverse(s.begin(), s.end());

        int n = s.size();
        int start = 0;

        for(int end = 0; end <= n; end++){
            if (end == n || s[end] == ' '){
                reverse(s.begin() + start, s.begin() + end);
                start = end + 1;
            }
        }
    }
};
/* reverse the entire array 
 arr ='theskyisblue'
 rev_arr = 'eulbsiykseht'

 reverser the each word inndividualy 
 rev_ word1 = 'bluesiykseht'
 rev_word2 = 'blueisykeht'
 rev_word3 = 'blueisskyeht'
 rev_word4 = 'blueisskythe'


*/