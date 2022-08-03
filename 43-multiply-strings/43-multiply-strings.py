class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        boxes = []
        for jx, c1 in enumerate(num2[::-1]):
            buf = [0] * jx
            s, c = 0, 0
            for ix, c2 in enumerate(num1[::-1]):
                s = c + (int(c1) * int(c2))
                c = s // 10
                s = s % 10
                buf.append(s)
            if c != 0:
                buf.append(c)
            boxes.append(buf)
        
        mlen = max(list(map(lambda x: len(x), boxes)))
        for ix, box in enumerate(boxes):
            boxes[ix] = boxes[ix] + [0] * (mlen - len(boxes[ix]))
        
        
        res = []
        c = 0
        for ix in range(mlen):
            s = c
            for jx in range(len(boxes)):
                s = s + boxes[jx][ix]
            c = s // 10
            s = s % 10
            res.append(str(s))
        if c != 0:
            res.append(str(c))
        
        return str(int("".join(res)[::-1]))