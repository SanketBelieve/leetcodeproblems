def maxCount(m: int, n: int, ops: list[list[int]]) -> int:
        min_y = m
        min_x = n

        for y, x in ops:
            min_y = min(min_y, y)
            min_x = min(min_x, x)

        return min_x * min_y