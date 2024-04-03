# code your iterative algorithm here
def binary_search(data, el):
    first = 0
    last = len(data)-1
    found = False

    while first <= last and not found:
        mid = (first+last) // 2

        if data[mid] == el:
            found = True
        else:
            if el < data[mid]:
                last = mid - 1
            else:
                first = mid + 1
        
    return found

test_lst = [33, 51, 98, 101, 110, 273, 851]

print(binary_search(test_lst, 101))