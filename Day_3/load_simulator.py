import time
import sys
import os

# A little trick to allow our Day 3 code to find the Coffee Shop we built in Day 2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Message
from Day_2.server import ChatServer

def simulate_huge_crowd():
    print("--- Opening the Coffee Shop for the Big Event ---")
    
    # We open our single, normal-sized coffee shop
    coffee_shop = ChatServer()
    
    print("\nSuddenly, 50,000 people rush in to talk about the Cricket Final!")
    
    # We start a stopwatch to see how long it takes to listen to everyone
    start_time = time.time()
    
    # 50,000 people rush through the door one by one
    for i in range(1, 50001):
        # Give every person a unique name
        user = f"User_{i}"
        
        # Everyone wants to shout in the exact same room
        channel = "Cricket_Match_Final"
        
        # What they are shouting
        content = "WHAT A COMEBACK! DID YOU SEE THAT?!"
        
        # We write down their message on a new note
        msg = Message(user, channel, content)
        
        # We hand the note to the single server (reception) to add to the giant notepad
        coffee_shop.send_message(msg)
        
        # Print a quick update every 10,000 people so we know our shop hasn't completely frozen yet
        if i % 10000 == 0:
            print(f"... {i} people have shouted their messages ...")

    # Stop the stopwatch
    end_time = time.time()
    time_taken = end_time - start_time
    
    print("\n--- The Rush is Over ---")
    # Ask the coffee shop how many messages it ended up writing down
    coffee_shop.stats()
    print(f"Time taken to write down 50,000 messages on one notepad: {time_taken:.4f} seconds.")
    
    # Let's check how heavy the notepad has gotten
    # We calculate the physical memory (RAM) our single list is eating up
    list_memory_size = sys.getsizeof(coffee_shop.messages)
    
    # Plus the weight of the actual ink (text content) on those notes
    total_memory = list_memory_size + sum(sys.getsizeof(m.content) for m in coffee_shop.messages)
    
    print(f"Memory (paper) used up by the notes: ~{total_memory / 1024:.2f} Kilobytes.")
    
    print("\n--- The Real Problem: Finding Things in a Massive Pile ---")
    print("Now, let's try to find 'User_49999's message in this massive stack of notes...")
    
    # Start a new stopwatch for searching
    search_start = time.time()
    
    # Because we only have one giant pile of paper, the only way to find a specific note 
    # is to violently flip through every single page from the top to the bottom.
    found = False
    for note in coffee_shop.messages:
        if note.user_id == "User_49999":
            found = True
            break  # We found it, so we can stop searching
            
    search_end = time.time()
    print(f"Time taken to search through the massive pile: {search_end - search_start:.5f} seconds.")
    
    print("\nConclusion: Just writing things down is fast, but storing it all in one spot eats up memory,")
    print("and searching through a single, giant stack of notes becomes visibly slower as it grows!")

if __name__ == "__main__":
    simulate_huge_crowd()