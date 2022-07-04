class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def bfs(image, sr, sc, color, init, memo):
            if image[sr][sc] != color and image[sr][sc] == init and (sr, sc) not in memo:
                image[sr][sc] = color
                memo[(sr, sc)] = None
                if sr > 0 and (sr - 1, sc) not in memo:
                    bfs(image, sr - 1, sc, color, init, memo)
                if sc > 0 and (sr, sc - 1) not in memo:
                    bfs(image, sr, sc - 1, color, init, memo)
                if sr < len(image) - 1 and (sr + 1, sc) not in memo:
                    bfs(image, sr + 1, sc, color, init, memo)
                if sc < len(image[0]) - 1 and (sr, sc + 1) not in memo:
                    bfs(image, sr, sc + 1, color, init, memo)
                    
        bfs(image, sr, sc, color, image[sr][sc], {})
        return image