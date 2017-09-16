lijst = [4,0,1,-2]

def swap(lst):
    if len(lst) > 1:
        lst[0], lst[3] = lst[3], lst[0]
        return lst
res = swap(lijst)
print(res)
