class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        vector<int> count(26, 0);
        
        for(char a: s) count[a - 'a']++;
        for(char a: t) count[a - 'a']--;
        
        for(int i = 0; i < 26; i++){
            if(count[i] != 0) return false;
        }
        return true;
    }   

};
