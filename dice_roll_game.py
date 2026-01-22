# My first python script for GitHub
import random
import time

def roll_dice():
    min_val = 1
    max_val = 6
    
    print("Rolling the dice...")
    # Add a small delay to make it dramatic
    time.sleep(1)
    
    # Get a random number
    result = random.randint(min_val, max_val)
    
    print(f"The values are: {result}")
    
    # Fun extra: Print a message for 6 or 1
    if result == 6:
        print("🎉 Amazing roll!")
    elif result == 1:
        print("😢 Better luck next time!")

if __name__ == "__main__":
    roll_again = "yes"
    while roll_again.lower() == "yes" or roll_again.lower() == "y":
        roll_dice()
        roll_again = input("\nRoll the dice again? (yes/y): ")