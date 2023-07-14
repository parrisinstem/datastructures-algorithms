def appear_in_both(arr1,arr2):
    #sort the lists
    arr1.sort() 
    arr2.sort()

    #empty array for values that appear in both
    appear_in_both = []

    #pointers
    i = 0
    j = 0 
    #compare values in both array until there are no more values
    while i < len(arr1) and j < len(arr2):
        #if value in arr1 is smaller
        if arr1[i] < arr2[j]:
            #move to next index
            i += 1
        #if values in arr2 is smaller
        elif arr1[i] > arr2[j]:
            #move to next index
            j += 1
        #otherwise values are the same and therefore appear in both
        else:
            #confirm it is not already in the array to avoid duplicates
            if not appear_in_both or arr1[i] != appear_in_both[-1]:
                #append the common value
                appear_in_both.append(arr1[i])
            #move to next index
            i += 1
            j+= 1
            
    return appear_in_both


#testcases
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
# expected output: [4, 5]

arr3 = [3, 5, 7, 9, 11]
arr4 = [2, 4, 6, 8, 10]
# expected output: []

arr5 = [1, 2, 3, 4, 5]
arr6 = [1, 2, 3, 4, 5]
#expected output: [1, 2, 3, 4, 5]

arr7 = [7,4,5,7]
arr8 = [9,2,7]
#expected output: [7]

print(appear_in_both(arr1, arr2))
print(appear_in_both(arr3, arr4))
print(appear_in_both(arr5, arr6))
print(appear_in_both(arr7, arr8))