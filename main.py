import string

def main():
    file_path = "books/frankenstein.txt"
    content = get_file_content(file_path)
    count_words = get_count_words(content)
    count_characters = get_count_characters(content)
    print_report(file_path, count_words, count_characters)

def get_file_content(file_path):
    with open(file_path) as file:
        return file.read()

def get_count_words(content):
    words = content.split()
    return len(words)

def get_count_characters(content):
    lowered_content = content.lower()
    characters_dict = {}
    for char in lowered_content:
            if char in characters_dict:
                characters_dict[char] += 1
            else:
                characters_dict[char] = 1
    
    return characters_dict

def print_report(file_path, count_words, count_characters):
    print(f"--- Begin report of {file_path} ---")
    print(f"{count_words} words found in the document")

    def sort_by_second(tuple):
        return tuple[1]

    character_tuples = list(count_characters.items())
    character_tuples.sort(key=sort_by_second, reverse=True)

    for tuple in character_tuples:
        if tuple[0].isalpha():
            print(f"The '{tuple[0]}' character was found {tuple[1]} times")

main()