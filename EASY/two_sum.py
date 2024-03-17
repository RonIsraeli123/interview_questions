"""
get the index's that have the sum of the target input
"""


# O(n) complexity | O(n) storage
def two_sum(numbers: list[int], sum_target: int):
    # mapping the entire list to access the difference in O(1) complexity
    mapping_numbers: dict[int, int] = {}
    for index, number_value in enumerate(numbers):
        # if number not exists in dict add it.
        if not mapping_numbers.get(number_value):
            mapping_numbers[number_value] = index

    # search if the list has the difference list's value | passing the array = O(n)
    for index, number_value in enumerate(numbers):
        other_number: int = sum_target - number_value
        if number_value != other_number and mapping_numbers.get(other_number):
            return [index, mapping_numbers[other_number]]
    return False


if __name__ == "__main__":
    numbers: list[int] = [5, 2, 3, 8, 7]
    target_sum = 10
    print(two_sum(numbers, target_sum))
