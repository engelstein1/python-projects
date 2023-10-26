from Test import test


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]

    print(array)


array = [3, 5, 17, 3, -1, -9, -999, 6, 8, 10, 3]


# bubble_sort(array)
# print(array)


# bubble_sort(a)

# print(arr)


# test(bubble_sort, 10000)


def counting_sort(array):
    if len(array) == 0:
        return "try"
    maxed = max(array)
    mine = min(array)
    count = 0
    counting_list = []
    for i in range(maxed - mine + 1):
        counting_list.append(0)
    for element in array:
        counting_list[element - mine] += 1
    for j in range(len(counting_list)):
        if counting_list[j] != 0:
            for each in range(counting_list[j]):
                array[count] = j + mine
                count += 1


array = [3, 5, 17, 3, -1, -9, -999, 6, 8, 10, 3]


# counting_sort(array)
# print(array)


#
# test(counting_sort,10000)

def merge_sort_rec(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_rec(array, start, mid)
        merge_sort_rec(array, mid + 1, end)
        merge(array, start, mid, end)


def merge_sort(array):
    merge_sort_rec(array, 0, len(array) - 1)


def merge(array, start, mid, end):
    merged = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if array[i] <= array[j]:
            merged.append(array[i])
            i += 1
        else:
            merged.append(array[j])
            j += 1
    if i <= mid:
        merged += array[i:mid + 1]
    if j <= end:
        merged += array[j:end + 1]
    for i in range(len(merged)):
        array[i + start] = merged[i]


# a = [1, 3, 2, 4, -2, 4, 6, 8, 7.8]
#
# merge_sort(a)
#
# print(a)


# test(merge_sort, 100000)


def find_max(array):
    maxi = array[0]
    for element in array:
        if element > maxi:
            maxi = element
    print(maxi)

    # find_max(array)

    for i in range(len(str(maxi))):
        str_maxi = str(maxi)
        print(str(str_maxi[i]))
find_max(array)

