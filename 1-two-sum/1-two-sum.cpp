class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++){
            int missing = target - nums[i];
            if (mp.find(missing) != mp.end()){
                
                res.push_back(mp[missing]);
                res.push_back(i);
            }
            mp[nums[i]] = i;
        }
        
        return res;
    }
};