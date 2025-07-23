from stats import num_of_words
from stats import num_of_characters

def main():
    count = num_of_words("./books/frankenstein.txt")
    words = num_of_characters("./books/frankenstein.txt")
    print(f"{count} words found in the document")
    print(f"{words} characters found in the document")
    
main()