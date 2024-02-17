h = [14,3,19,3]
b = 17
l = 0
# s=0
# for i in range(len(h)-1):
#     if h[i+1]> h[i] and h[i+1]- h[i] < b:
#         b-=h[i+1]- h[i]
        
#     elif h[i+1]> h[i] and h[i+1]- h[i] > b:
#         l-=1
# print(h[i])          
        
# for i in range(len(heights) - 1):
#     if heights[i + 1] > heights[i] and heights[i + 1] - heights[i] <= b:
#         bricks -= heights[i + 1] - heights[i]
#     elif heights[i + 1] > heights[i] and heights[i + 1] - heights[i] > bricks and ladders > 0:
#         bricks = 0
#         ladders -= 1
#     elif ladders == 0:
#         break

# print("Index:", i +2, "Value:", heights[i + 1])
furthest_index = 0
for i in range(len(h) - 1):
    if h[i + 1] > h[i] and h[i + 1] - h[i] <= b:
        b -= h[i + 1] - h[i]
        furthest_index = i + 1
    elif h[i + 1] > h[i] and h[i + 1] - h[i] > b and l > 0:
        b = 0
        l -= 1
        furthest_index = i + 1
    elif l == 0:
        break

print(furthest_index) 
