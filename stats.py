def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def sort_on(items):
    return items["num"]

def dict_sort(dic):
    new_list = []
    for d in dic:
        new_list.append({"char": d, "num": dic[d]})
    new_list.sort(reverse=True,key=sort_on)
    return new_list

def count_char(book):
    lowered = book.lower()
    count = {}

    for char in lowered:

        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count