arr = [2,7,11,15]
arr1 = [3,2,4]
def solution_1(arr, target):

    for i in range(len(arr)-1):
        tmp = target - arr[i]
        for j in range(i+1, len(arr)):
            if tmp == arr[j]:
               return [i,j] 
    else:
        return []

# print(solution_1(arr, 9))

def solution_2(arr, target):
    hashmap = dict()
    for i, val in enumerate(arr):
        tmp = target - val
        if tmp < 0:
            continue
        else:
            if val in hashmap:
                return [hashmap[val], i]
            else:
                hashmap[tmp] = i
    return []