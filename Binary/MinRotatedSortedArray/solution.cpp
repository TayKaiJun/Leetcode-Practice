#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int start = 0;
        int end = nums.size()-1;
        while(start < end){
            int mid = (start+end)/2;
            if(mid+1 < nums.size() && nums[mid]>nums[mid+1])
                return nums[mid+1];
            if(mid-1 >= 0 && nums[mid-1]>nums[mid])
                return nums[mid];
            if(nums[mid] < nums[end])
                end = mid;
            else
                start = mid;
        }
        return nums[start];
    }
};

int main(){
    Solution s;
    vector<int> nums = {3,4,5,1,2};
    cout << s.findMin(nums) << endl;
    nums = {4,5,6,7,0,1,2};
    cout << s.findMin(nums) << endl;
    nums = {11,13,15,17};
    cout << s.findMin(nums) << endl;
    nums = {2,1};
    cout << s.findMin(nums) << endl;
    nums = {3,1,2};
    cout << s.findMin(nums) << endl;
    nums = {4,5,1,2,3};
    cout << s.findMin(nums) << endl;

}