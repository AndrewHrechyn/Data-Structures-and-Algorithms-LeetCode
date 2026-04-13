def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2  
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1

if __name__ == '__main__':
    target = int(input("Enter the target number: "))
    arr = list(map(int, input("Enter sorted array: ").split()))

    result = binary_search(arr, target)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found")
