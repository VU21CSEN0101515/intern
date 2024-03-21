def count_words(text):
    # Split the text into words
    words = text.split()
    # Return the number of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    text = input("Enter a sentence or paragraph: ")

    # Check if the input is empty
    if not text:
        print("Error: Please enter some text.")
        return

    # Call the count_words function to count the words
    word_count = count_words(text)

    # Display the word count
    print("Word count:", word_count)

if __name__ == "__main__":
    main()