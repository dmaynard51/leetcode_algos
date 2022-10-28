class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> res;
        unordered_map<int,int> hash;
        
        for (int i = 0; i < nums.size(); i++){
            int findNum = target - nums[i];
            
            if (hash.find(findNum) != hash.end()){
                res.push_back(i);
                res.push_back(hash[findNum]);
                return res;
            }
            hash[nums[i]] = i;
        }
        
        return res;
    }
};