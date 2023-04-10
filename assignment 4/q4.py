def subset_finder(lst, target):
    def helper(idx, total):
        if total == target:
            return 1
        if idx == len(lst) or total > target:
            return 0
        count = helper(idx+1, total+lst[idx])
        count += helper(idx+1, total)
        return count
    
    return helper(0, 0)

lst = list(map(int, input().split()))
target = int(input())
result = subset_finder(lst, target)
print(result)
