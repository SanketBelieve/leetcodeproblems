
# # cnt = 0
# # for i in range(len(n)):
# #     if (i % 2 == 0 and int(n[i]) % 2 == 0) and (i % 2 != 0 and int(n[i]) % 2 != 0):
# #         cnt += 1
# # print(cnt)
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# def is_good_digit_string(s):
#     for i in range(len(s)):
#         digit = int(s[i])
#         if i % 2 == 0:  # Even index
#             if digit % 2 != 0:  # Check if even
#                 return False
#         else:  # Odd index
#             if not is_prime(digit):  # Check if prime
#                 return False
#     return True

# # Test cases
# print(is_good_digit_string("2582"))  # Output: True
# print(is_good_digit_string("3245"))  # Output: False


def is_even(num):
  if num%2 == 0:
    return True

def is_good_digit_string(s):
    for i in range(len(s)):
        digit = int(s[i])
        if i % 2 == 0:  # Even index
            if digit % 2 != 0:  # Check if even
                return False
        else:  # Odd index
            if not is_prime(digit):  # Check if prime
                return False
    return True


n = 4
ran = 10**n
count = 0
for i in range(1,ran+1):
    if is_good_digit_string(str(i)):
        count += 1
        # print(i)
    elif is_good_digit_string(str(i)):
        count +=1
        # print(i)

print(count)