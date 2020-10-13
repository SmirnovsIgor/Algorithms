import time

from binary import generate_arr


def interpolation_search(arr, n, x):
    left = 0
    right = (n - 1)

    while left <= right and arr[left] <= x <= arr[right]:
        if left == right:
            if arr[left] == x:
                return left
            return -1

        pos = left + int(((float(right - left) / (arr[right] - arr[left])) * (x - arr[left])))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            left = pos + 1
        else:
            right = pos - 1
    return -1


if __name__ == '__main__':
    array = generate_arr(2 ** 20)
    start = time.time()
    print(interpolation_search(array, 2 ** 20, 1214235))
    print(time.time() - start)
