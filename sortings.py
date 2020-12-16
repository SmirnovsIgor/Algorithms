class Sort:
    @staticmethod
    def bubble_sort(arr):
        for i in range(len(arr) - 1, 0, -1):
            for i in range(i):
                if arr[i]>arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr

    @staticmethod
    def insertion_sort(arr, low, high): 
        for i in range(low + 1, high + 1): 
            key = arr[i] 
            j = i
            while j > low and key < arr[j - 1] : 
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = key 
        return arr

    @staticmethod
    def partition(arr, low, high): 
        i = low - 1
        pivot = arr[high]
        for j in range(low , high): 
            if arr[j] < pivot: 
                i = i + 1 
                arr[i], arr[j] = arr[j], arr[i] 
        arr[i + 1], arr[high] = arr[high], arr[i + 1] 
        return i + 1
    
    @staticmethod
    def quick_sort(arr, low, high): 
        if low < high: 
            pi = Sort.partition(arr, low, high) 
            Sort.quick_sort(arr, low, pi - 1) 
            Sort.quick_sort(arr, pi + 1, high)

    @staticmethod
    def hybrid_sort(arr, low, high): 
        while low < high: 
            if high - low + 1 < 10: 
                Sort.insertion_sort(arr, low, high) 
                break
            else: 
                pivot = partition(arr, low, high) 
                if pivot - low < high - pivot: 
                    hybrid_sort(arr, low, pivot-1) 
                    low = pivot + 1
                else: 
                    hybrid_sort(arr, pivot + 1, high) 
                    high = pivot - 1

    @staticmethod
    def counting_sort(array, max):
        counts = [0] * (max + 1)
        items_before = 0
        sorted_list = [None] * len(array)
        
        for item in array:
            counts[item] += 1

        for i, count in enumerate(counts):
            counts[i] = items_before
            items_before += count

        for item in array:
            sorted_list[ counts[item] ] = item
            counts[item] += 1
        return sorted_list

    @classmethod
    def max(array):
        max = array[0]
        i = 1
        while i < array.length:
            if array[i] > max:
                max = array[i]
            i += 1
        return max

if __name__ == '__main__':
    arr = [1234, 6543, 14326456, 4563456, 64, 4325]
    Sort.hybrid_sort(arr, 0, 5)
    print(arr)