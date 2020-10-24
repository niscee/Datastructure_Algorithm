#Anagram check
# "public relations" is anagram of "crap built of lies."

a = "public relations"
a1 = "crap built on lies"


def anagramCheck(s1, s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    counter = {}

    #check edge case
    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

           

    for j in s2:
        if j in counter:
            counter[j] -= 1
        else:
            counter[j] = 1   
    

    for k in counter:
        if counter[k] != 0:
            return False

    return True                              








