class BinarySearch:

    @staticmethod
    def binary_search(item, items_list, left, right):
        if left > right:
            return -1
        else:
            middle = (left + right) // 2

            if items_list[middle] == item:
                return middle

            elif items_list[middle] < item:
                left = middle + 1
                return BinarySearch.binary_search(item, items_list, left, right)

            elif items_list[middle] > item:
                right = middle - 1
                return BinarySearch.binary_search(item, items_list, left, right)


def main():
    items_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    item = -1

    left = 0
    right = len(items_list) - 1
    middle = (left + right) // 2
    result = BinarySearch.binary_search(item, items_list, left, right)

    if result != -1:
        print(f"element found at index: {result}")
    else:
        print(f"item not found")


if __name__ == "__main__":
    main()
