def word_counter(text):
    """
    Counts the number of words in the given text.
    
    Args:
    text (str): The input text.
    
    Returns:
    int: The number of words in the text.
    """
    # Split the text into words based on whitespace
    words = text.split()
    # Return the count of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    text = input("Enter a sentence or paragraph: ")
    
    # Check for empty input
    if not text:
        print("Error: Empty input!")
        return
    
    # Call the word_counter function to count the words
    word_count = word_counter(text)
    
    # Display the result
    print("Number of words:", word_count)

if __name__ == "__main__":
    main()
