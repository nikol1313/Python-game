#!/usr/bin/env python3

import random, shelve


def play_round(user_choice, stats):
    comp_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("Tie!")
        stats['ties'] += 1
    elif (user_choice == "rock" and comp_choice == "scissors") or \
            (user_choice == "paper" and comp_choice == "rock") or \
            (user_choice == "scissors" and comp_choice == "paper"):
        print("You win!")
        stats['wins'] += 1
    else:
        print("Computer wins!")
        stats['losses'] += 1


def main():
    stats = shelve.open("rpsStats")
    for key in ["wins", "losses", "ties"]:
        if key not in stats:
            stats[key] = 0

    print(f"Current stats: Wins={stats['wins']}, Losses={stats['losses']}, Ties={stats['ties']}")

    user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
    if user_choice in ["rock", "paper", "scissors"]:
        play_round(user_choice, stats)
    else:
        print("Invalid choice!")

    print(f"Updated stats: Wins={stats['wins']}, Losses={stats['losses']}, Ties={stats['ties']}")

    stats.close()


if __name__ == "__main__":
    main()

