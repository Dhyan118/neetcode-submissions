class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size() - 1; // Two pointers
        int leftMax = 0, rightMax = 0;           // Track max heights
        int totalWater = 0;                      // Store total trapped water

        while (left < right) {
            // If left bar is shorter, process left side
            if (height[left] < height[right]) {
                if (height[left] >= leftMax)
                    leftMax = height[left];      // Update left max
                else
                    totalWater += leftMax - height[left]; // Add trapped water
                left++;                          // Move left pointer
            } 
            // Otherwise, process right side
            else {
                if (height[right] >= rightMax)
                    rightMax = height[right];    // Update right max
                else
                    totalWater += rightMax - height[right]; // Add trapped water
                right--;                         // Move right pointer
            }
        }

        return totalWater;
    }
};