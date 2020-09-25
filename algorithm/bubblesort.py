""" bubble sort algorithm """ 

def bubblesort(array):
    n = len(array)

    for i in range(n):

        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] 
        print(i+1,array)        


array = [21,4,1,3,9,20,25,6,21,14]
bubblesort(array)
print(array)