import time
import random


def generate_arr(qty):
    return [random.randint(0, qty) for _ in range(qty)]


def lin_search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1


if __name__ == '__main__':
    arr = generate_arr(2 ** 20)
    start = time.time()
    print(lin_search(arr, 2 ** 20, 1214235))
    print(time.time() - start)

