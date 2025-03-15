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
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
    return char_count