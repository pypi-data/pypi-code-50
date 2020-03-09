def countSort(array):
    output = [0 for i in range(256)]
    count = [0 for i in range(256)]
    ans = ["" for _ in array]
    for i in array:
        count[ord(i)] += 1
    for i in range(256):
        count[i] += count[i-1]
    for i in range(len(array)):
        output[count[ord(array[i])]-1] = array[i] 
        count[ord(array[i])] -= 1
    for i in range(len(array)):
        ans[i] = output[i] 
    
    return ans

print(countSort("ok"))
