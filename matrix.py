def findRotation( mat: list[list[int]], target: list[list[int]]) -> bool:
        n = len(mat)
        count_0, count_90, count_180, count_270 = 0, 0, 0, 0

        for i in range(n):
            for j in range(n):
                # imaging rotating the matrix but without actually doing it, and for
                # each 90 degree rotation, take the new indices of the matrix and
                # compare them to the target

                # both matrices as they are
                if mat[i][j] == target[i][j]:
                    count_0 += 1

                # after rotating mat 90 degrees
                if mat[i][j] == target[j][n - i - 1]:
                    count_90 += 1

                # after rotating mat 180 degrees
                if mat[i][j] == target[n - i - 1][n - j - 1]:
                    count_180 += 1

                # after rotating mat 270 degrees
                if mat[i][j] == target[n - j - 1][i]:
                    count_270 += 1

        return n * n in {count_0, count_90, count_180, count_270}
    
print(findRotation( mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]))    

        