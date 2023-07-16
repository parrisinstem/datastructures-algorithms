# Search list
test_scores = [88, 93, 75, 100, 80, 67, 71, 92, 90, 83]

#Linear Search Algorithm
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index

# Function call
def highest_score(scores):
    highest_score_index = linear_search(scores)

#Prints out the highest score in the list
    if highest_score_index != None:
        highest_score = test_scores[highest_score_index]
        print("The highest score is:", highest_score)
    else:
       print("The list is empty")
    return highest_score

highest_score(test_scores)