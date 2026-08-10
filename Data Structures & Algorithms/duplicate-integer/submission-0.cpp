class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> dupsTracker;

        for(auto i : nums) {
            if (dupsTracker.find(i) == dupsTracker.end()) {
                dupsTracker.insert(i);
            } else {
                return true;
            }
        }

        return false;
    }
};