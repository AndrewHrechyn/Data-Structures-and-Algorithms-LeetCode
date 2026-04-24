class Solution {
    public:
        int compress(vector<char>& chars) {
            int i = 0, res = 0;
            while (i < chars.size()) {
                int groupLength = 1;
                while (i + groupLength < chars.size() && chars[i + groupLength] == chars[i]) {
                    groupLength++;
                }
                chars[res++] = chars[i];
                if (groupLength > 1) {
                    for (char ch : to_string(groupLength)) {
                        chars[res++] = ch;
                    }
                }
                i += groupLength;
            }
            return res;
        }
    };
    