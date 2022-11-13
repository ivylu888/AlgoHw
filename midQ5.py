def removeDuplicates(self, arr:List):
    indexes = []
    if len(arr) == 0: return 0
    slow = fast = 0
    while fast < len(arr):
        if arr[slow] != arr[fast]:
            indexes.append(fast)
            arr[slow] = arr[fast]
            slow += 1           
        
        fast += 1
    return indexes
