import sys
import os

# A little trick to allow our Day 4 code to find the Coffee Shop we built in Day 2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Message
from Day_4.shards import ShardManager

def test_multiple_shops():
    print("--- Welcome to our new multiple Coffee Shop franchise! ---")
    
    # We decided to expand. We open 3 coffee shops (Shards)
    manager = ShardManager(num_shards=3)
    
    print("\nOur Security Guard (Manager) is standing out front.")
    print("However... we haven't given the guard any rules yet on where to send people.")
    print("So when we hand a message to the guard:")
    
    # A friend comes to drop a message
    user = "User_1"
    channel = "General_Chat"
    content = "Hello from the new shops!"
    msg = Message(user, channel, content)
    
    # We hand the note to the guard manager... but they don't know what to do!
    manager.send_message(msg)
    
    print("\n--- The End of the Day ---")
    
    # Check the shops to see what happened.
    manager.show_shard_stats()
    
    print("\nConclusion: Our shops are completely separate now (No Global Storage).")
    print("But until we give the guard (ShardManager) instructions on *where* people should go (routing),")
    print("nobody is actually able to deliver any messages!")

if __name__ == "__main__":
    test_multiple_shops()