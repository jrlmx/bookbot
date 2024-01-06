def main():
    file_path: str = 'books/frankenstein.txt'
    char_dict: dict[str, int] = get_chars_dict()
    contents: str = get_book_contents(file_path)

    contents_in_lowercase = contents.lower()

    for char in contents_in_lowercase:
        if char in char_dict:
            char_dict[char] += 1

    chars_list_sorted = chars_dict_to_sorted_list(char_dict)

    print(f'--- Begin report for {file_path} ---\n')
    print(f'{get_word_count(contents)} words found in the document\n')

    for char, count in chars_list_sorted:
        print(f'The \'{char}\' character was found {count} times')

    print(f'\n--- End report ---')
    

def get_chars_dict() -> dict[str, int]:
    chars = 'abcdefghijklmnopqrstuvwxyz'
    return {char: 0 for char in chars}

def chars_dict_to_sorted_list(chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    char_count_list = list(chars_dict.items())
    return sorted(char_count_list, key=lambda x: x[1], reverse=True)

def get_char_count(contents: str, char: str) -> int:
    return contents.count(char)

def get_word_count(file_contents: str) -> int:
    words = file_contents.split()
    return len(words)

def get_book_contents(path: str) -> str:
    with open(path) as f:
        return f.read()

if __name__ == '__main__':
    main()