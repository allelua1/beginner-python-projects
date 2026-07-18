#Take a paragraph as input
#Split into a list of words, count frequency using a dictionary
#Function to find the top 5 most used words using lambda + sorted()

"""word = "Hello Ally. I love you."
Word_split = word.split(" ")
print(Word_split)
print(len(Word_split))

paragraph = input("Enter your words/paragraph to be counted: ")
splitted_paragraph = paragraph.split(" ")
print(len(splitted_paragraph))"""

import string

paragraph = input("Enter your words/paragraph to be counted: ")

# .clean the paragraph: lowercase and remove punction
cleaned_words = []
for word in paragraph.lower().split():
    cleaned_word = word.strip(string.punctuation)
    if cleaned_word:
        cleaned_words.append(cleaned_word)

# count word frequency
word_count = {}
for word in cleaned_words:
    word_count[word] = word_count.get(word, 0) + 1
print("Words:", cleaned_words)
print("TOtal words:", len(cleaned_words))
print("Word frequency:", word_count)

# get the top 5 most frequenct words using lambda + sorted()
top_5 = sorted(word_count.items(), key = lambda item: item[1], reverse = True)[:5]
print("Top 5 most used words:", top_5)
