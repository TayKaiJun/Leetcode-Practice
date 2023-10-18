#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        std::stack<int> ngr;
        ngr.push(0);
        int n = height.size();

        for(int i = 1; i < n; i++){
            if(height[i] >= height[ngr.top()]){
                if(abs(i - ngr.top()) == 1){
                    ngr.pop();
                    ngr.push(i);
                }
                else
                    ngr.push(i);
            }
        }

        std::stack<int> ngl;
        for(int i = n-1; i >= 0; i--){
            if(i == ngr.top())
                break;
            if(ngl.empty()){
                ngl.push(i);
                continue;
            }
            if(height[i] >= height[ngl.top()]){
                if(abs(i - ngl.top()) == 1){
                    ngl.pop();
                    ngl.push(i);
                }
                else
                    ngl.push(i);
            }
        }

        while(!ngl.empty()){
            ngr.push(ngl.top());
            ngl.pop();
        }

        int sum = 0;
        int prev = ngr.top();
        ngr.pop();
        while(!ngr.empty()){
            int curr = ngr.top();
            int min_height = min(height[curr], height[prev]);
            for (int j = prev - 1; j > curr; j--)
                sum += max(min_height - height[j],0);
            ngr.pop();
            prev = curr;
        }
        return sum;
    }
};

int main(){
    Solution s;
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};                      // 6
    // cout << s.trap(height) << endl;
    // height = {4,2,0,3,2,5};                                        // 9
    // cout << s.trap(height) << endl;
    // height = {4,2,3};     // 1
    // cout << s.trap(height) << endl;
    height = {9,6,8,8,5,6,3};     // 3
    cout << s.trap(height) << endl;
}