#string comprehension
#AAAABBBBCCCCCDDEEEE ouput A4B4C5D2E4

def compress(s):
    output = ''
    store = {}
    
    for i in s:
        if i in store:
            store[i] += 1
        else:
            store[i] = 1

    
    for i,v in store.items():
        merge = i + str(v)
        output += merge

    return output

