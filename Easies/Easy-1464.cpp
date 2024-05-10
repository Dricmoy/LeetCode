class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.size() == 2){
            return (nums[0]-1) * (nums[1]-1);
        }

        int j = *max_element(nums.begin(), nums.end());

        auto iter = std::find(nums.begin(), nums.end(), j);

        if (iter != nums.end()){
            nums.erase(iter);
        }

        int i = *max_element(nums.begin(), nums.end());
        return (i-1) * (j-1);
    }
};


//find the max element make it j, get rid of it if there's more than one instance, second as i
//otherwise get rid of it, and take the next possible max element as i. 