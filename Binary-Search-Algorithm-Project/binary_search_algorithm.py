def binary_search(list_num, element):
    start_index = 0
    end_index = len(list_num) - 1
    middle_index = 0

    while True:
        middle_index = (start_index + end_index) // 2

        if start_index == end_index:
            if list_num[middle_index] != element:
                return 'Element does not appear in the list!'
            else:
                return f'{list_num[middle_index]} occurs in position {middle_index}'
        elif list_num[middle_index] == element:
            return f'{list_num[middle_index]} occurs in position {middle_index}'
        elif list_num[middle_index] > element:
            end_index = middle_index - 1
        elif list_num[middle_index] < element:
            start_index = middle_index + 1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 1))
print(binary_search(my_list, 9))
print(binary_search(my_list, 15))
