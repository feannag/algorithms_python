class BinarySearch:

    @staticmethod
    def binary_search(item, items_list):
        left = 0
        right = len(items_list) - 1

        while left <= right:
            middle = (left + right) // 2

            if items_list[middle] == item:
                return middle

            elif items_list[middle] < item:
                left = middle + 1

            elif items_list[middle] > item:
                right = middle - 1

        return -1


def main():
    items_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    item = 10

    result = BinarySearch.binary_search(item, items_list)

    if result != -1:
        print(f"element found at index: {result}")
    else:
        print(f"item not found")


if __name__ == "__main__":
    main()
