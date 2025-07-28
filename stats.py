def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(path):
        book_text = get_book_text(path)
        return len(book_text.split())

def count_characters(path):
    book_text = get_book_text(path)
    lower_book = book_text.lower()
    count_dict = {}
    
    for each_char in lower_book:
        if each_char not in count_dict:
            count_dict[each_char] = 1
        else:
            count_dict[each_char] += 1

    for each_char in lower_book:
        count_dict[each_char] = 1 if each_char not in count_dict else count_dict[each_char] + 1

    return count_dict