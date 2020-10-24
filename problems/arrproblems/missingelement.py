#missing element
# finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])  output - 5 

# def finder(arr1, arr2):
#     counter = {}
    

#     for i in arr1:
#         if i in counter:
#             counter[i] += 1
#         else:
#             counter[i] = 1


#     for j in arr2:
#         if j in counter:
#             counter[j] -= 1
    
#     print(counter)

#     for k in counter:
#         if counter[k] != 0:
#             return k




# def finder(arr1, arr2):
#     arr1 = sorted(arr1)
#     arr2 = sorted(arr2)

#     for i,j in zip(arr1, arr2):
#         if i != j:
#             return i





# from collections import Counter

# def finder(arr1, arr2):
#     arr1 = Counter(arr1)
#     arr2 = Counter(arr2)

#     result = arr1 - arr2
#     for i in result:
#         return i

                               

