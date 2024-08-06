class Solution:
    def dfs(self, image, sr, sc, newColor, initialColor, new_ans, delRow, defCol):
        # change that color for the initial
        new_ans[sr][sc] = newColor
        n = len(image)  # row length in mtx
        m = len(image[0])  # col length in mtx
        for i in range(4):  # coz we have 4 directions
            new_row = sr + delRow[i]
            new_col = sc + defCol[i]
            if 0 <= new_row < n and 0 <= new_col < m and image[new_row][new_col] == initialColor and new_ans[new_row][new_col] != newColor:
                self.dfs(image, new_row, new_col, newColor,
                         initialColor, new_ans, delRow, defCol)

    def floodFill(self, image, sr, sc, color):
        # you need to define an initial color
        initialColor = image[sr][sc]
        new_ans = [row[:] for row in image]

        # define delta rows and columns to traverse in the matrix
        delRow = [-1, 0, 1, 0]
        defCol = [0, 1, 0, -1]

        self.dfs(image, sr, sc, color, initialColor, new_ans, delRow, defCol)
        return new_ans


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
ff = Solution()

print(ff.floodFill(image, sr, sc, color))
