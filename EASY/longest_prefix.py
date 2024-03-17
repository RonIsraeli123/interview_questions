"""
get the longest strings prefix
"""


# O(n + m)  complexity | O(m) storage
def longest_common_prefix(words: list[str]) -> str:
    prefix_result = ""
    # O(n)
    shortest_word: str = min(words, key=len)

    for index_char, shortest_char in enumerate(shortest_word):
        for word in words:
            if shortest_char != word[index_char]:
                return prefix_result
        prefix_result += shortest_char
    return prefix_result


# O(n * log(n))  complexity | O(n) storage
def longest_common_prefix_with_sort(words: list[str]) -> str:
    string_prefix = ""
    words.sort()
    first_word = words[0]
    most_different_word = words[-1]

    for char_index, first_word_char in enumerate(first_word):
        if first_word_char != most_different_word[char_index]:
            return string_prefix
        string_prefix += first_word_char
    return string_prefix


if __name__ == "__main__":
    strings: list[str] = ["preoz", "pre", "preotig"]
    print(longest_common_prefix(strings))

    print(longest_common_prefix_with_sort(strings))
