import time

from linear_search import generate_arr


def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1


if __name__ == '__main__':
    arr = generate_arr(2 ** 20)
    start = time.time()
    print(binary_search(arr, 0, (2 ** 20) - 1, 1214235))
    print(time.time() - start)

