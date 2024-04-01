def maxAreaOfSquare(bottomLeft, topRight):
    n = len(bottomLeft)
    max_side = 0

    for i in range(n):
        for j in range(i+1, n):
            # Find the intersecting region
            intersect_bottom = [max(bottomLeft[i][0], bottomLeft[j][0]), max(bottomLeft[i][1], bottomLeft[j][1])]
            intersect_top = [min(topRight[i][0], topRight[j][0]), min(topRight[i][1], topRight[j][1])]

            # Check if there is an intersection
            if intersect_bottom[0] < intersect_top[0] and intersect_bottom[1] < intersect_top[1]:
                # Calculate the maximum side of a square that can fit in the intersection
                side = min(intersect_top[0] - intersect_bottom[0], intersect_top[1] - intersect_bottom[1])
                max_side = max(max_side, side)

    return max_side * max_side
bottomLeft = [[1,1],[2,2],[3,1]]
topRight = [[3,3],[4,4],[6,6]]
print(maxAreaOfSquare(bottomLeft, topRight))  # Output: 1
