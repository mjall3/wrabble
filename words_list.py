# Open the text file
with open('words.txt', 'r') as file:
    # Read each line, strip any trailing whitespace (like newlines), and store in a list
    WORDS_ARRAY = [line.strip() for line in file]
