# Store candidates in a list, votes in a dictionary.
# Functions: cast a vote, display results, find winner.
# Use a set to track who has already voted (no double voting).

candidates = ["Kagame", "Habineza", "Barafinda"]
votes = {candidate: 0 for candidate in candidates}
voted_users = set()


def cast_vote(voter_id, candidate_name):
    if voter_id in voted_users:
        print("You have already voted. Double voting is not allowed.")
        return False
    if candidate_name not in votes:
        print("Invalid candidate. Vote not counted.")
        return False

    voted_users.add(voter_id)
    votes[candidate_name] += 1
    print(f"Vote cast for {candidate_name}.")
    return True


def display_results():
    print("\nElection Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} vote{'s' if count != 1 else ''}")


def find_winner():
    max_votes = max(votes.values())
    winners = [name for name, count in votes.items() if count == max_votes]

    if len(winners) > 1:
        print("\nIt's a tie between:")
        for winner in winners:
            print(f"- {winner} ({max_votes} votes)")
    else:
        print(f"\nWinner is {winners[0]} with {max_votes} votes.")


def main():
    print("Voting System")
    print("Candidates: " + ", ".join(candidates))

    while True:
        voter_id = input("\nEnter your voter ID (or 'quit' to finish): ").strip()
        if voter_id.lower() == "quit":
            break

        candidate_name = input("Enter candidate to vote for: ").strip()
        cast_vote(voter_id, candidate_name)

    display_results()
    find_winner()


if __name__ == "__main__":
    main()
