from stats import num_of_words

def main():
    count = num_of_words("./books/frankenstein.txt")
    print(f"{count} words found in the document")
    
main()