def char_count(string):
    lower_string = string.lower()
    chars_dict = {}
    for char in lower_string:
        if char not in chars_dict:
            chars_dict[char] = 0
        chars_dict[char] += 1  
    return chars_dict 

def main():
    PATH = "books/frankenstein.txt"
    with open(PATH) as f:
        file_contents = f.read()
        print(char_count(file_contents))
main()
