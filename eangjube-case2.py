def count_chars_words_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
            print(f"Number of characters: {num_chars}")

    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")

def main():
    filename = input("Enter the filename: ")
    count_chars_words_lines(filename)

if __name__ == "__main__":
    main()
