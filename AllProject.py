#VotingSystem
"""candidates = ["Kagame", "Barafinda", "Habineza"]
votes = {candidate:0 for candidate in candidates}
voted_user = set()

# Cast_vote function 
def cast_vote(voter_id, candidate_name):
    if voter_id in voted_user:
        print("You have already voted. Double voting not allowed.")
        return False
    if candidate_name not in votes:
        print("Invalid candidate. Vote not counted")
        return False
    voted_user.add(voter_id)
    votes[candidate_name] += 1
    print(f"Vote cast for {candidate_name}.")
    return True
def display_result():
    print("\n Election Results ")
    for candidate, count in votes.items():
        print(f"{candidate} : {count} vote{'s' if count != 1 else ''}")
    
def find_winner():
    max_votes = max(votes.values())
    winners = [name for name, count in votes.items() if count == max_votes]

    if len(winners) > 1:
        print("\n It's tie between: ")
        for winner in winners:
            print(f"{winner} ({max_votes} votes)")
    else:
        print(f"Winner is {winners[0]} with {max_votes} votes")

def main():
    print("Voting System")
    print("Candidates: "+",".join(candidates))

    while True:

        voter_id = input("Enter Your ID(or 'quit' to finish): ").strip()
        if voter_id.lower() == "quit":
            break
        candidate_name = input("Enter candidate to vote for: ").strip()
        cast_vote(voter_id, candidate_name)
    display_result()
    find_winner()

if __name__== "__main__":
    main()
 """
# 2. WordFrequencyCounter

""" import string

paragraph = input("Enter a words/pararapgh to be counted: ")

# clean paragraph: lowercase/uppercase
cleaned_words = []
for word in paragraph.lower().split():
    cleaned_word = word.strip(string.punctuation)
    if cleaned_word:
        cleaned_words.append(cleaned_word)
# count frequency
word_count = {}
for word in cleaned_words:
    word_count[word] = word_count.get(word,0) + 1
print("\n Words: ", cleaned_words)
print("\n Total Words: ", len(cleaned_words))
print("\n Word frequency: ", word_count)

# Top 5 most used words:
top_5 = sorted(word_count.items(), key = lambda item: item[1], reverse= True)[:5]
print("\n Top 5 most use words: ", top_5) """

# 3. Simple Library System

books = [{"title":"Operating System", "author":"Sifuna", "available":True}]
borrowed_books = []

# function for adding books in system
def adding_books(books, book_title, author, available):
    books.append({"title":book_title, "author":author, "available":available})
    print(f"{book_title} book has been added into the system.")

# function for borrowing books
def borrowing_books(books, book_title):
    for book in books:
        if book["title"] == book_title:
            if book["available"]:
                book["available"] = False
                borrowed_books.append(book_title)
                books.remove(book)
                print(f'Book "{book_title}" has been borrowed')
                return
            else:
                print(f'Book "{book_title}" is not available')
                return
    print(f'Book "{book_title}" was not found in the library.')

# function for returning books 
def return_book(books, book_title, author, available):
    if book_title in borrowed_books:
        books.append({"title":book_title, "author":author, "available":available})
        borrowed_books.remove(book_title)
        print(f'Book "{book_title}" has been returned. ')
    else:
        print(f'Book "{book_title}" has not been borrowed.')

# function for searching book by author
def search_by_author(books, author):
    matches = [book for book in books if book["author"].lower() == author.lower()]
    if matches:
        print(f" Book by {author}: ")
        for book in matches:
            print(f" - {book["title"]}")
    else:
        print(f' No book found for author "{author}"')


print("\nAdding books into system")
adding_books(books, "Python Tutorials", "Gerard", True)
adding_books(books, "Cybersecurity", "Linus", False)
adding_books(books, "Cybersecurity", "Sifuna", True)

print("\nBorrowed books")
borrowing_books(books, "Computer Programming")
borrowing_books(books, "Operating System")

print("\nReturned books")
return_book(books, "Computer Programming", "Sifuna", True)
return_book(books, "Cloud Computing", "Bernard", True)
return_book(books, "Operating System", "Sifuna", True)

print("\nSearch book by author:")
search_by_author(books, "Sifuna")