def word_count(sentence):
    """
    Counts how many times each word appears in a sentence.
    
    Args:
        sentence (str): The input sentence.
    Returns:
        dict: A dictionary with words as keys and counts as values.
    Raises:
        ValueError: If the input is not a string.
    """
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string.")

    words = sentence.lower().split()
    count = {}
    for word in words:
        word = word.strip(".,!?")  # remove punctuation
        count[word] = count.get(word, 0) + 1
    return count

if __name__ == "__main__":
    text = "Python is fun and Python is powerful!"
    result = word_count(text)
    print("Input:", text)
    print("Word count:", result)
