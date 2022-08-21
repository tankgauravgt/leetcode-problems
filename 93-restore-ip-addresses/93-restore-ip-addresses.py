class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def valid(ip):
            nums = ip.split('.')
            if len(nums) != 4 or '' in nums:
                return False
            for num in nums:
                if len(num) > 1 and num[0] == '0':
                    return False
                elif len(num) >= 1 and int(num) not in range(0, 256):
                    return False
            return True
        
        out = []
        def btrack(ix, c, buf):
            nonlocal out
            if c > 3:
                return
            if ix == len(s):
                if valid("".join(buf)):
                    out.append("".join(buf))
                return
            else:
                buf.append(s[ix])
                btrack(1 + ix, c, buf)
                buf.pop()
                buf.append('.')
                btrack(ix, 1 + c, buf)
                buf.pop()
        
        btrack(0, 0, [])
        return out