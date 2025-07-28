from stats import count_words
from stats import count_characters

def main():
    count = count_words("./books/frankenstein.txt")
    words = count_characters("./books/frankenstein.txt")
    
    print(f"{count} words found in the document")
    print(f"{words} characters found in the document")
    
main()