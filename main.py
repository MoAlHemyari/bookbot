import sys
from stats import count_words, count_char

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(item):
    return item["num"]

def order_char(char_stat):
    char_stat_list = []
    for key in char_stat:
        char_stat_list.append({
            "name": key,
            "num": char_stat[key]
        })

    char_stat_list.sort(reverse=True, key=sort_on)

    return char_stat_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    # "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    
    print("----------- Word Count ----------")
    print(count_words(text))

    print("--------- Character Count -------")
    char_stat = count_char(text)
    ordered_char_stat = order_char(char_stat)
    for i in ordered_char_stat:
        if i["name"].isalpha() == False:
            continue
        print(f"{i["name"]}: {i["num"]}")

    print("============= END ===============")


main()
