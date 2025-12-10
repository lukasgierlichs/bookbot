def get_num_words(path_to_file):
    """
    Takes a file path, reads the text, and prints the total number of words.
    """
    with open(path_to_file) as f:
        book_text = f.read()

    num_words = len(book_text.split())
    print(f"Found {num_words} total words")

def count_characters(path_to_file):
    """
    Takes a file path, reads the text, and returns a dictionary with the count
    of each character (including symbols and spaces).
    Characters are converted to lowercase to avoid duplicates.
    """
    with open(path_to_file) as f:
        book_text = f.read()
    
    char_count = {}
    book_text_lower = book_text.lower()
    
    for char in book_text_lower:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
                
    return char_count

def sort_char_count(char_count):
    """
    Takes a character count dictionary and returns a list of dictionaries sorted
    by character count in reverse order (highest to lowest).
    """
    sorted_list = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    return [{char: count} for char, count in sorted_list]
   