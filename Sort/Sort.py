import random
from tqdm import tqdm


def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    for j in range(start, end + 1):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    return i


def quick_sort_recursion(array, start, end):
    if start < end:
        pivot_index = partition(array, start, end)
        quick_sort_recursion(array, start, pivot_index - 1)
        quick_sort_recursion(array, pivot_index + 1, end)


def quick_sort(array):
    quick_sort_recursion(array, 0, len(array) - 1)


# a = [-3, -17, 4, 6, 78, -20]
# print(a)
# quick_sort(a)
# print(a)


def test(sorting_function, num_of_tests):
    for _ in tqdm(range(num_of_tests)):
        random_length = random.randint(0, 1000)
        random_list = [random.randint(-2000, 2000) for _ in range(random_length)]
        copy = random_list[:]
        sorting_function(random_list)
        expected = sorted(copy)
        if random_list != expected:
            print("FAIL!")
            print("your output is:", random_list)
            print("expected output is:", expected)
            print("try debugging using:", copy)
            return False
    print("You are a king!!")
    return True


test(quick_sort, 100000)
