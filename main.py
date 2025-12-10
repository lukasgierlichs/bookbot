import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def main():
    from stats import get_num_words
    from stats import count_characters
    from stats import sort_char_count

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(sys.argv[1])
    print("--------- Character Count --------")
    sorted_chars = sort_char_count(count_characters(sys.argv[1]))
    for char_dict in sorted_chars:
        for char, count in char_dict.items():
            print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()        
