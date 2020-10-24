#pairsum([1,3,2,2], 4) return (1,3) and (2,2)

def pair_sum(arr, k):
    seen = set()
    output = set()

    for i in arr:
        target = k - i
        if target in seen:
            output.add((target, i))
        else:
            seen.add(i)

    return len(output)       
