def subset(cap, items):
    if cap <= 0 or items == []:
        return 0
    elif items[0] > cap:
        return subset(cap, items[1:])
    else:
        use_it = items[0] + subset(cap - items[0], items[1:])
        lost_it = subset(cap, items[1:])
        return max(use_it, lost_it)

print(subset(42, [10, 23, 30, 18, 5]))