class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;   // farthest index we can reach so far

        for (int i = 0; i < nums.size(); i++) {
            // If current index is beyond what we can reach
            if (i > maxReach) {
                return false;
            }

            // Update farthest reachable index
            maxReach = max(maxReach, i + nums[i]);
        }

        return true;
    }
};

