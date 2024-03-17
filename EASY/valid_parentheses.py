# O(n) complexity | O(n) storage
def is_valid(string: str):
    symbolize_chars: dict[str, int] = {
        '{': 1,
        '}': -1,

        '(': 2,
        ')': -2,

        '[': 3,
        ']': -3,
    }

    # parse parentheses to numbers (easier to understand)
    num_list: list[int] = []
    for char in string:
        if symbolize_chars.get(char):
            num_list.append(symbolize_chars[char])

    stack: list[int] = []
    for num in num_list:
        # meaning open parentheses came
        if num > 0:
            stack.append(num)
        # close parentheses came before a open parentheses or wrong close came
        elif len(stack) == 0 or stack[-1] + num != 0:
            return False
        # parentheses close
        else:
            stack.pop()
    # all parentheses close
    if len(stack) == 0:
        return True
    return False


if __name__ == "__main__":
    first_true_string: str = "(){}{}()[]"
    second_true_string: str = "(){()}[]"
    first_false_string: str = "(){}{)(}[]"
    second_false_string: str = "(){}{()[]"
    print(is_valid(first_true_string))
    print(is_valid(second_true_string))
    print(is_valid(first_false_string))
    print(is_valid(second_false_string))
