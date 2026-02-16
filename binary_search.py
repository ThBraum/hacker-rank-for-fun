arr = [3, 1, 4, 2, 5, 6, 10, 35, 23, 7, 87, 32, 65, 99, 100, 54, 76, 45, 34, 12]
target = 23

def binary_search(arr, target):
    sorted_items = sorted(((value, index) for index, value in enumerate(arr)), key=lambda item: item[0])
    left, right = 0, len(sorted_items) - 1

    while left <= right:
        middle = left + (right - left) // 2
        middle_value, original_index = sorted_items[middle]
        if middle_value == target:
            return original_index
        if middle_value > target:
            right = middle - 1
        else:
            left = middle + 1

    return -1

print(f"O target {target} está no index ", binary_search(arr, target))
            