"""
check if a number is a palindrome (not supported with minus digits)
"""


# O(n) complexity | O(1) storage
def is_palindrome(input: str):
    is_even_len: bool = len(input) % 2 == 0
    intermediate_str_index: int or tuple[int, int] = (len(input) // 2 - 1, len(input) // 2) if is_even_len else len(
        input) // 2
    if isinstance(intermediate_str_index, tuple):
        left: int = intermediate_str_index[0]
        right: int = intermediate_str_index[1]
    else:
        left: int = intermediate_str_index
        right: int = intermediate_str_index

    for i in range(len(input) // 2):
        if not input[left] == input[right]:
            return False
        left = left - 1
        right = right + 1
    return True


if __name__ == "__main__":
    odd_false_string: str = "4112213"
    even_false_string: str = "41122113"
    second_even_false_string: str = "-10"
    odd_true_string: str = "3122213"
    even_true_string: str = "122221"
    # print(is_palindrome(odd_false_string))
    # print(is_palindrome(even_false_string))
    print(is_palindrome(second_even_false_string))
    # print(is_palindrome(odd_true_string))
    # print(is_palindrome(even_true_string))
