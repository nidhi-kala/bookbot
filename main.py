def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"the book has {num_words} words")
    letters = get_letters(text)
    sorted_list = get_list(letters)
    for item in sorted_list:
        print(f"{item[0]} : {item[1]}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_letters(text):
    letters = {}
    for letter in text:
        lowered = letter.lower()
        if not lowered in letters:
            letters[lowered] = 1
        else:
            letters[lowered] += 1
    return letters

def get_list(letters):
    lst = []
    for letter in letters:
        lst.append([letter, letters[letter]])
    lst.sort()
    return lst
        


main()