def main():
    with open("/home/kalle/workspace/wwp2/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

from stats import countwords
from stats import countcharacters


wordcount = countwords()
dictionaryofcharacters = countcharacters()

print("""
============ BOOKBOT ============
Analyzing book found at books/frenkenstein.txt...
----------- Word Count ----------
Found""", (wordcount), """total words.
--------- Character Count -------""")
for char, count in dictionaryofcharacters:
    print(f"{char}: {count}")
print("""============= END ===============""")