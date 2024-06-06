def char_count(string):
    lower_string = string.lower()
    chars_dict = {}
    for char in lower_string:
        if char.isalpha():
            if char not in chars_dict:
                chars_dict[char] = 0  # creates a new key with a value of 0.
            chars_dict[char] += 1  
    return chars_dict 

def sort_dict(dict): # sorts by largest value.
    sorted_list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_list

def final_print(list, word_count, file):
    print(f"""--- Begin report of {file} ---
    \r{word_count} words found in the document\n""")
    for l in list:
        print(f"The '{l[0]} character was found {l[1]} times'")
    print("--- End report ---")

def main():
    PATH_TO_TEXT = "books/frankenstein.txt" # use text of your own.
    with open(PATH_TO_TEXT) as f:
        file_contents = f.read()
        words = len(file_contents.split())
        
        chars = char_count(file_contents)
        sorted_chars = sort_dict(chars)
        final_print(sorted_chars, words, PATH_TO_TEXT)
main()
