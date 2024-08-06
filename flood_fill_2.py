class Solution:

    def dfs(self, image, sr, sc, newColor, initial_color, new_array, del_row, del_col, k):
        new_array[sr][sc] = newColor
        n = len(image)
        m = len(image[0])
        k[0] = 20
        for i in range(4):
            new_row = sr + del_row[i]
            new_col = sc + del_col[i]

            if 0 <= new_row < n and 0 <= new_col < m and image[new_row][new_col] == initial_color and new_array[new_row][new_col] != newColor:
                self.dfs(image, new_row, new_col, newColor,
                         initial_color, new_array, del_row, del_col, k)

    def floodFill(self, image, sr, sc, newColor):
        initial_color = image[sr][sc]
        new_array = [color[:] for color in image]
        k = [0]
        del_row = [-1, 0, 1, 0]
        del_col = [0, 1, 0, -1]

        self.dfs(image, sr, sc, newColor, initial_color,
                 new_array, del_row, del_col, k)
        return new_array, k


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
ff = Solution()
print(ff.floodFill(image, sr, sc, newColor))
# [[2,2,2],[2,2,0],[2,0,1]] answer
