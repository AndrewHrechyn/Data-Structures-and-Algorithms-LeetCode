#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        int n = a.size(), m = b.size();
        if (n < m)
            return addBinary(b, a);

        string result;
        int carry = 0, j = m - 1;

        for (int i = n - 1; i >= 0; --i) {
            if (a[i] == '1') ++carry;
            if (j >= 0 && b[j--] == '1') ++carry;

            result.push_back((carry % 2) ? '1' : '0');
            carry /= 2;
        }

        if (carry == 1) result.push_back('1');

        reverse(result.begin(), result.end());
        return result;
    }
};

int main() {
    Solution solution;
    string a, b;
    
    cout << "Enter first binary string: ";
    cin >> a;
    cout << "Enter second binary string: ";
    cin >> b;
    
    string result = solution.addBinary(a, b);
    cout << "Sum: " << result << endl;
    
    return 0;
}
