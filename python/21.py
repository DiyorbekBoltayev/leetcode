def mergeTwoLists(list1, list2) -> list:
    list1+=list2
    list1.sort()
    return list1


print(mergeTwoLists([1,2,3],[1,3,4]))

