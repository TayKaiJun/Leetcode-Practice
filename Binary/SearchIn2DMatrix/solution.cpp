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
        int curr_row = 0;
        int curr_col = col-1;

        while(curr_row < row && curr_col >= 0){
            if(target == matrix[curr_row][curr_col])
                return true;
            else if (target < matrix[curr_row][curr_col])
                curr_col--;
            else
                curr_row++;
        }
        return false;
    }
};

int main(){
    Solution s;
    vector<vector<int>> matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,60}};
    int target = 3; // true
    cout << s.searchMatrix(matrix,target) << endl;
    target = 13; // false
    cout << s.searchMatrix(matrix,target) << endl;
    matrix = {{1,1}};
    target = 2; // false
    cout << s.searchMatrix(matrix,target) << endl;
}