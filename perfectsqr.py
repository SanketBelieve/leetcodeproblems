'''def isPerfectSquare(num):
    if num < 0:
        return False

    # Use the square root function and check if it's an integer
    sqrt_num = int(num ** 0.5)
    return sqrt_num * sqrt_num == num

# Example usage:
num = 14
if isPerfectSquare(num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")'''
def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False