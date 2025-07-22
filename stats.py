def get_book_text(path):
    with open(path) as f:
        return f.read()

def num_of_words(path):
        book = get_book_text(path)
        return len(book.split())