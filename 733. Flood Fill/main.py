import copy

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        res_image = copy.deepcopy(image)
        def filler(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
            if sr - 1 >= 0 and image[sr][sc] == image[sr - 1][sc] and res_image[sr - 1][sc] != color:
                res_image[sr][sc] = color
                filler(image, sr - 1, sc, color)
            if sr + 1 < len(image) and image[sr][sc] == image[sr + 1][sc] and res_image[sr + 1][sc] != color:
                res_image[sr][sc] = color
                filler(image, sr + 1, sc, color)
            if sc - 1 >= 0 and image[sr][sc] == image[sr][sc - 1] and res_image[sr][sc - 1] != color:
                res_image[sr][sc] = color
                filler(image, sr, sc - 1, color)
            if sc + 1 < len(image[0]) and image[sr][sc] == image[sr][sc + 1] and res_image[sr][sc + 1] != color:
                res_image[sr][sc] = color
                filler(image, sr, sc + 1, color)
            res_image[sr][sc] = color
            return res_image
        return filler(image, sr, sc, color)