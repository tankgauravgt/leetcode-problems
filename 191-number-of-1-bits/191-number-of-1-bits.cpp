class Solution {
public:
    
    int dnc(uint32_t k) {
        return (k == 0 ? 0: 1 + dnc(k & (k - 1)));
    }
    
    int hammingWeight(uint32_t n) {
        return dnc(n);
    }
};