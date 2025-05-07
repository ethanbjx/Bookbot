import sys
import stats 

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    stats.process_book(book_path)

if __name__ == "__main__":
    main()

