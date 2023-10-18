#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> operands;
        for(int i = 0; i < tokens.size(); i++){
            if(isdigit(tokens[i][0]) || (tokens[i][0] == '-' && isdigit(tokens[i][1]))){
                operands.push(stoi(tokens[i]));
            }
            else{
                int second = operands.top();
                operands.pop();
                int first = operands.top();
                operands.pop();
                switch(tokens[i][0]){
                    case '+':
                        operands.push(first + second);
                        break;
                    case '-':
                        operands.push(first - second);
                        break;
                    case '/':
                        operands.push(int(first / second));
                        break;
                    case '*':
                        operands.push(first * second);
                        break;
                }
            }
        }
        return operands.top();
    }
};


int main(){
    Solution s;
    vector<string> tokens = {"2", "1", "+", "3", "*"};                      // 9
    // cout << s.evalRPN(tokens) << endl;
    // tokens = {"4","13","5","/","+"};                                        // 6
    // cout << s.evalRPN(tokens) << endl;
    tokens = {"10","6","9","3","+","-11","*","/","*","17","+","5","+"};     // 22
    cout << s.evalRPN(tokens) << endl;
}