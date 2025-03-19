import sys

inputwords = sys.argv

def countwords():
    try:
        with open(inputwords[1]) as f:
            booktext = f.read()
            words = booktext.split()
            return(len(words))
    except FileNotFoundError:
        print(f"Error: File '{inputwords[1]}' not found.")
        return 0
    
def countcharacters():
    char_count = {}
    with open(inputwords[1]) as file:
            text = file.read().lower()
            for char in text:
                if char.isalpha():
                    if char in char_count:
                        char_count[char] += 1
                    else:
                        char_count[char] = 1
    char_dictionary = dict(char_count)
        
    sorted_char = sorted(char_dictionary.items(), key=lambda x:x[-1], reverse=True)
    return sorted_char
