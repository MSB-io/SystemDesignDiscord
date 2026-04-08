import sys
import os
import time

# Pull in our code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Message
from Day_9.query_manager import QueryShardManager

def test_cross_shard_query():
    print("--- Welcome to Day 9/10! The Final Nightmare of Math-Based Routing ---")
    
    # Open up 3 coffee shops again under our math-based manager
    manager = QueryShardManager(num_shards=3)
    
    import random
    
    print("\n[MORNING] A nice normal, sunny morning in our coffee shops...")
    # Several friends talk in one channel, but because of our math, their messages 
    # get thrown randomly into all 3 different coffee shops.
    
    for i in range(1, 101):
        user = f"User_{random.randint(1, 10)}"
        channel = "VIP_Chat"
        content = f"This is message #{i}"
        
        msg = Message(user, channel, content)
        # We manually write the exact second they dropped the note, so we can organize it later
        msg.timestamp = time.time()
        
        # Add a tiny, microscopic pause so the timestamps are perfectly unique
        time.sleep(0.0001) 
        
        manager.send_message(msg)

    print(f"\nAll 100 messages for 'VIP_Chat' have been randomly thrown across {len(manager.shards)} shops.")
    manager.show_shard_stats()
    
    # Now, a new person walks in and wants to read the previous conversation.
    print("\n[LUNCH] A new friend arrives at the front door:")
    print("'Hey! What were the last 10 things people said at the VIP_Chat table?'")
    
    # ---------------------------------------------
    # Cross-Shard Query Demonstration
    # ---------------------------------------------
    
    # The guard literally has no idea which shop the latest messages are in because of the 
    # random math hashing. So he has to run to EVERY single shop and gather all the notes.
    last_10 = manager.get_last_10_messages("VIP_Chat")
    
    print("\n[GUARD] Here are the last 10 messages across all our buildings, stitched back together:")
    print("--------------------------------------------------")
    for msg in last_10:
        print(f"[{msg.user_id}] says: {msg.content}")
    print("--------------------------------------------------")

    print("\n--- The Conclusion ---")
    print("Writing messages with perfectly random math is incredibly easy and safe (no hotspots!)")
    print("But READING messages becomes incredibly slow and expensive!")
    print("To answer one simple question ('last 10 messages'), our manager had to physically walk")
    print("to 3 different buildings, gather 100 scattered notes, manually sort them by time on the floor,")
    print("and then pass back the top 10.")
    print("Imagine doing this with 10,000 coffee shops. The system would freeze every time someone opened the chat!")

if __name__ == "__main__":
    test_cross_shard_query()