score=[10,2,5,8,6]
sorted_scores = sorted(score, reverse=True)
print(sorted_scores)



def findRelativeRanks(self, score: list[int]) -> list[str]:
        # Create a copy of the input array and sort it in descending order
        sorted_scores = sorted(score, reverse=True)
        # Create a dictionary to store the rank of each score
        rank_dict = {}
        
        # Loop through the sorted scores and assign ranks
        for i, s in enumerate(sorted_scores):
            if i == 0:
                rank_dict[s] = "Gold Medal"
            elif i == 1:
                rank_dict[s] = "Silver Medal"
            elif i == 2:
                rank_dict[s] = "Bronze Medal"
            else:
                rank_dict[s] = str(i + 1)
        
        # Create a list to store the results
        result = []
        
        # Loop through the input array and append the rank of each score to the result list
        for s in score:
            result.append(rank_dict[s])
        
        # Return the result list
        return result
