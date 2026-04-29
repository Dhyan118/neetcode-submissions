class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end()); // sorted by start time
        vector<vector<int>> res;

        for( auto& interval : intervals){
            if(res.empty() || res.back()[1] < interval[0]){
                res.push_back(interval);
            } else{
                res.back()[1] = max(res.back()[1], interval[1]);
            }
        }
        return res; 

    }
};
        /*
        sort = [[1,3],[1,5],[6,7]]
        curr_int = [1,3]
        next= [1,5] 1 <= 3
        merge = [1,5]
        next = [6,7] 6 <= 5


        
        */