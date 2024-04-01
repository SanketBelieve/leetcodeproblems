# people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# print(sorted(people))
# p=[]
# for i in range(len(people)):
#     s=people[i][0]+people[i][1]
#     p.append(s)
# print(sorted(p))    

people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

# Sort the list of people based on the sum of each subarray
sorted_people = sorted(people, key=lambda x:(-x[0],x[1]))
print(sorted_people)

# Create a new list to store subarrays with the lowest sums
result = []

# Append subarrays with the lowest sums to the end of the new list

for person in sorted_people:
    print(person[1])
    result.insert(person[1],person)
print(result)



