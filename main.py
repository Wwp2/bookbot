def main():
    with open("/home/kalle/workspace/wwp2/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

from stats import countwords
from stats import countcharacters

wordcount = countwords()
dictionaryofcharacters = sorted(countcharacters())



print((wordcount), f"words found in the document")
print(dictionaryofcharacters)