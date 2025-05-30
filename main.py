
from stats import get_num_words
from stats import get_num_char
from stats import sort_list
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(filepath):
    # takes a filepath as input and returns the contents of the file as a string
    with open(filepath) as f:
        return f.read()
    

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count -----------")
    print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count ---------")
        
    # print(f'{get_num_words(get_book_text(sys.argv[1]))} words found in the document')
    # print(get_num_char(get_book_text(sys.argv[1])))
    dict_list = sort_list(get_num_char(get_book_text(sys.argv[1])))

    for dict in dict_list:
        if dict['char'].isalpha():
            print(f'{dict['char']}: {dict['num']}')
        
    print('============= END =============')


main()
