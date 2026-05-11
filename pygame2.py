#!/usr/bin/env python3
import shelve, random

def guessing_word(stats):
    comp_choice = random.randint(1, 20)
    MAX_TRIES = 3
    TRY_COUNT = 0
    print("You have 3 tries...")

    while TRY_COUNT < MAX_TRIES:
        user_choice = int(input("Enter a number from 1-20: "))
        if user_choice == comp_choice:
            stats['win'] += 1
            print(f"You guessed it! Computer chose {comp_choice}")
            break
        elif user_choice > comp_choice:
            print("Lower...")
        else:
            print("Higher...")
        TRY_COUNT += 1
    else:
        # This else runs only if loop finishes without break
        stats['loss'] += 1
        print(f"Out of tries! Computer chose {comp_choice}")

    print(f"Wins: {stats['win']}  Losses: {stats['loss']}")

def main():
    stats = shelve.open("stati.db")

    for key in ['win', 'loss']:
        if key not in stats:
            stats[key] = 0

    guessing_word(stats)

    stats.close()

if __name__ == "__main__":
    main()

