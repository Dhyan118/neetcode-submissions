class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        /*
        nums = [1,2,3,4,5,6,7,8] k = 4
        reverse the entire array 
        nums= [8,7,6,5,4,3,2,1]
        reverse the kth element 
        nums =[5,6,7,8,4,3,2,1]
        reverse the n-k elemtents 
        nums = [5,6,7,8,1,2,3,4]
        */

        int n = nums.size();
        k = k % n; 

        reverse(nums.begin(), nums.end()); // reverse entire array 
        reverse(nums.begin(), nums.begin() + k); //reverse first k element 
        reverse(nums.begin() + k, nums.end()); // reverese remaining elements 
    }
};