def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_num_letters(text)
    # print(text)
    # print(f"the number of words is: {num_words}")
    # print(f"number of chars:\n{char_dict}")
    get_report(char_dict, book_path, num_words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):
    char_dict = {}
    for char in text:
        c = char.lower()
        if c in char_dict and c.isalpha():
            char_dict[c] += 1
        elif c.isalpha():
            char_dict[c] = 1
    return char_dict

def get_report(dict, path, num_words):
    chars_sorted_list = chars_dict_to_sorted_list(dict)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document\n")
    for item in chars_sorted_list:
      print(f"The '{item['char']}' character was found {item['num']} times")
    print("\n--- End of report ---")
    
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for c in num_chars_dict:
        sorted_list.append({"char": c, "num": num_chars_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]   

main()
