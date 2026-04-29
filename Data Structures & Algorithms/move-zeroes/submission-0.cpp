class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int po = 0;

        for(int i = 0; i < nums.size(); i++){
            if(nums[i] != 0){
                nums[po] = nums[i];
                po++;
            }
        }
        while( po < nums.size()){
            nums[po] = 0;
            po++;
        }        
        
    }
};

/*
        nums = [0,0,1,2,0,5]
                    po
                           i
        nums[pos] = nums[i] = nums= [1,0,1,2,0,5]
                              nums = [1,2,1,2,0,5]
                              nums = [1,2,5,2,0,5]
                              nums = [1,2,5,0,0,0]

        */