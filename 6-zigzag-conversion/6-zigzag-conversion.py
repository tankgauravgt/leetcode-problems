class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        # buckets for each row characters:
        buckets = {i: [] for i in range(numRows)}
            
        cr = 0
        vec = 'u'
        
        for c in s:
            # if boundary, change the direction of vec
            if (cr == 0) or (cr == (numRows - 1)):
                vec = 'u' if vec == 'd' else 'd'
            
            # add char to bucket pointed by `cr`:
            buckets[cr] += [c]
                
            # change current row position:
            cr = ((cr + 1) if vec == 'd' else (cr - 1))
            
        # join all bucket result into final string:
        return ''.join([''.join(buckets[i]) for i in range(numRows)])