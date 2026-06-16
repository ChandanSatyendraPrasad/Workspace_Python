sentence = input("Enter a Sentence: ")
# Split the sentence into words
words = sentence.split()
print("The number of words in the sentence is:", len(words))
# Initialize Dictionary
word_count = {}
# Count the frequency of each word
for word in words:
    word = word.lower()  # Convert to lowercase for case-insensitive counting
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("The word frequency is:", word_count)