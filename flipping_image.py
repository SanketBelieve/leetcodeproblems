def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
        res = []
        for i in image:
            res.append([x ^ 1 for x in i[::-1]])
        return res




