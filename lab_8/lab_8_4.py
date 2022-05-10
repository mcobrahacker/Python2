def merge(list1, list2):
    index1 = 0
    index2 = 0
    merged_list = []
    for _ in range(len(list1 + list2)):
        if index1 + 1 > len(list1):
            merged_list.append(list2[index2])
            index2 += 1
        elif index2 + 1 > len(list2):
            merged_list.append(list1[index1])
            index1 += 1
        elif list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1
    return merged_list
 
 
numbers1 = [int(i) for i in input().split()]
numbers2 = [int(i) for i in input().split()]
print(*merge(numbers1, numbers2))