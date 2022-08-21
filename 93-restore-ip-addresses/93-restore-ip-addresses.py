class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def valid(ip):
            nums = ip.split('.')
            for num in nums:
                if len(num) == 0:
                    return False
                elif len(num) > 1 and num[0] == '0':
                    return False
                elif len(num) >= 1 and int(num) not in range(0, 256):
                    return False
            return True
        
        out = []
        def btrack(ix, c, buf):
            nonlocal out
            if ix == len(s):
                return
            elif c == 3:
                if valid("".join(buf) + s[ix::]):
                    out.append("".join(buf) + s[ix::])
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