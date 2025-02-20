def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    #print(count_words(file_contents))
    #print(count_characters(file_contents))
    chars_dict = count_characters(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {"frankenstein.txt"} ---")
    print(f"{count_characters} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_words(main):
    words = main.split()
    return(len(words))

def count_characters(main):
    char_dic = {}
    lower_chars = main.lower()
    for chars in lower_chars:
        if chars in char_dic:
            char_dic[chars] += 1
        else:
            char_dic[chars] = 1
    return(char_dic)


if __name__ == "__main__":
    main()