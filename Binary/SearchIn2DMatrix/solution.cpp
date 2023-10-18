#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size();
        int col = matrix[0].size();
        int left = 0;
        int right = row*col-1;

        while(left <= right){
            int mid = (right + left) / 2;
            int curr = matrix[mid/row][mid%col];
            if(target == curr)
                return true;
            else if (target < curr)
                right = mid-1;
            else
                left = mid+1;
        }
        return false;
    }
};

int main(){
    Solution s;
    vector<vector<int>> matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    int target = 3; // true
    // cout << s.searchMatrix(matrix,target) << endl;
    // target = 13; // false
    // cout << s.searchMatrix(matrix,target) << endl;
    matrix = {{1,1}};
    target = 2; // false
    cout << s.searchMatrix(matrix,target) << endl;
}