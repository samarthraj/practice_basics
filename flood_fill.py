class Solution:
    def dfs(self, sr, sc, ans, image, newColor, delRow, delCol, initial_color):
        # first fill the initial one with the new color
        ans[sr][sc] = newColor
        n = len(image)
        m = len(image[0])

        for i in range(4):
            new_row = sr + delRow[i]
            new_col = sc + delCol[i]
            if 0 <= new_row < n and 0 <= new_col < m and image[new_row][new_col] == initial_color and ans[new_row][new_col] != newColor:
                self.dfs(new_row, new_col, ans, image, newColor,
                         delRow, delCol, initial_color)

    def floodFill(self, image, sr, sc, newColor):
        initial_color = image[sr][sc]
        # copy of the image array
        ans = [row[:] for row in image]
        delRow = [-1, 0, 1, 0]  # clockwise
        delCol = [0, 1, 0, -1]  # clockwise
        self.dfs(sr, sc, ans, image, newColor, delRow, delCol, initial_color)
        return ans


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
ff = Solution()
print(ff.floodFill(image, sr, sc, newColor))
# [[2,2,2],[2,2,0],[2,0,1]] answer
