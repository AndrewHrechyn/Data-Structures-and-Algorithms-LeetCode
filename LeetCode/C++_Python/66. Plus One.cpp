#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for (int i = n - 1; i >= 0; --i) {
            if (digits[i] == 9) {
                digits[i] = 0;
            } else {
                digits[i]++;
                return digits;
            }
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};

int main() {
    Solution solution;
    vector<int> digits;
    int n, val;
    
    cout << "Enter number of digits: ";
    cin >> n;
    cout << "Enter the digits: ";
    for (int i = 0; i < n; ++i) {
        cin >> val;
        digits.push_back(val);
    }
    
    vector<int> result = solution.plusOne(digits);
    cout << "Result: ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}
