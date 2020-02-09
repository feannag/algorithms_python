class MergeSort:
    def __init__(self):
        pass

    @staticmethod
    def merge_lists(list_a, list_b):
        list_a_size = len(list_a)
        list_b_size = len(list_b)
        index_i = 0
        index_j = 0
        auxiliary_list = []

        while index_i < list_a_size and index_j < list_b_size:
            if list_a[index_i] <= list_b[index_j]:
                auxiliary_list.append(list_a[index_i])
                index_i += 1
            elif list_b[index_j] < list_a[index_i]:
                auxiliary_list.append(list_b[index_j])
                index_j += 1

        if index_i == list_a_size:
            auxiliary_list.extend(list_b[index_j:])
        elif index_j == list_b_size:
            auxiliary_list.extend(list_a[index_i:])

        return auxiliary_list

    def partition(self, numbers_list):
        list_size = len(numbers_list)
        m = list_size // 2

        if list_size == 1:
            return numbers_list

        list_a = self.partition(numbers_list[0:m])
        list_b = self.partition(numbers_list[m:list_size])

        auxiliary_list = self.merge_lists(list_a, list_b)
        return auxiliary_list


def main():
    numbers_list = [15, 1, 5, 8, 9, 10, 2, 50, 40, 3, 2, 9, 10, 7, 33, 34]
    ms = MergeSort()

    print(f"unsorted_numbers_list: {numbers_list}")
    sorted_numbers_list = ms.partition(numbers_list)
    print(f"sorted_numbers_list = {sorted_numbers_list}")


if __name__ == "__main__":
    main()
