class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> memo({0});
        for(int ix=1; ix<=n; ix++)
            memo.push_back((ix % 2) + memo[ix / 2]);
        return memo;
    }
};