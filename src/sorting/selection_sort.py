class SelectionSort:
    def selection_sort(self, items_list):

        for i in range(0, len(items_list) - 1):
            smallest_element = items_list[i]
            index = 0
            swap_flag = False

            for j in range(i+1, len(items_list)):
                if items_list[j] < smallest_element:
                    smallest_element = items_list[j]
                    index = j
                    swap_flag = True

            if swap_flag is True:
                temp = items_list[i]
                items_list[i] = smallest_element
                items_list[index] = temp


def main():
    items_list = [5, 4, 3, 2, 1]
    print(f"list of items before sorting: {items_list}")

    ss = SelectionSort()
    ss.selection_sort(items_list)
    print(f"list of items after sorting: {items_list}")


if __name__ == "__main__":
    main()

