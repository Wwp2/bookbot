import sys

inputwords = sys.argv

try: 
    if len(inputwords) < 2:
        raise ValueError
except:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)


from stats import countwords
from stats import countcharacters

wordcount = countwords()
dictionaryofcharacters = countcharacters()

def main():
    print("""
============ BOOKBOT ============
Analyzing book found at""", inputwords[1], """...
----------- Word Count ----------
Found""", (wordcount), """total words.
--------- Character Count -------""")
    for char, count in dictionaryofcharacters:
        print(f"{char}: {count}")
    print("""============= END ===============""")

def mainpathfinder():
    try: 
        if inputwords[1] >= None:
            return main()
    except:
        return(f"Usage: python3 main.py <path_to_book>")

main()