def countwords():
    with open("/home/kalle/workspace/wwp2/bookbot/books/frankenstein.txt") as f:
        booktext = f.read()
        words = booktext.split()
        return(len(words))
    
def countcharacters():
    char_count = {}
    with open("/home/kalle/workspace/wwp2/bookbot/books/frankenstein.txt") as file:
            text = file.read().lower()
            for char in text:
                if char.isalpha():
                    if char in char_count:
                        char_count[char] += 1
                    else:
                        char_count[char] = 1
        
    sorted_char = sorted(char_count.items(), key=lambda x:x[1], reverse=True)
    return sorted_char
