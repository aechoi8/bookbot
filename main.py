from stats import get_num_words, get_num_chars, sorted_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        readfile = f.read()
        print(readfile)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_path)} total words")
    print("--------- Character Count -------")
    sorted_counts = sorted_list(get_num_chars(file_path))
    
    for char, counts in sorted_counts:
        if char.isalpha():
            print(f"{char}: {counts}")
            
    print("============= END ===============")

main()