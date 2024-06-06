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
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict

def main():
    PATH = "books/frankenstein.txt" # use text of your own.
    with open(PATH) as f:
        file_contents = f.read()
        dict = char_count(file_contents)
        print(dict)
        print(sort_dict(dict))
main()
