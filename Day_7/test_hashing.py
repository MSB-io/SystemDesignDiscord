import sys
import os

# Pull in our code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Message
from Day_7.strategies import HashShardManager
from Day_5.strategies import UserShardManager
from Day_6.strategies import ChannelShardManager

def test_hash_balancing():
    print("--- Welcome to our new Math-Based (Hash) Routing System! ---")
    
    # We open up our 3 coffee shops, and put our smartest mathematically-minded guard at the door.
    manager = HashShardManager(num_shards=3)
    
    print("\nOur previous rules failed because they bunched similar things together.")
    print("By giving every single message an MD5 number, we theoretically solve BOTH problems!")
    print("Let's bring in the Influencer (Day 5 Problem) AND the Viral Cricket game (Day 6 problem) at the same time.")
    
    # ---------------------------------------------
    # Scenario: The Ultimate Stress Test (Influencer + Viral Channel)
    # ---------------------------------------------
    import random
    
    influencer = "User_999"
    viral_channel = "Cricket_Final"
    
    print("\n[AFTERNOON] An Influencer starts spamming 5,000 messages AND the Cricket game goes viral with 10,000 people!")
    
    # Send 5000 messages from ONE user (The Day 5 problem)
    for i in range(5000):
        msg = Message(influencer, "General_Chat", "I am the influencer!")
        manager.send_message(msg)
        
    # Send another 10,000 messages from random users in ONE channel (The Day 6 problem)
    for friend_id in range(1, 10001):
        user = f"User_{friend_id}"
        msg = Message(user, viral_channel, "WOW WHAT A HIT!")
        manager.send_message(msg)
        
    print("\nAfternoon check on our 3 shops:")
    manager.show_shard_stats()
    
    print("\n--- The Conclusion ---")
    print("It's perfectly balanced! Because we put every individual message into a giant math blender (md5 hashing),")
    print("we guaranteed that every message gets thrown randomly across all 3 shops, completely bypassing")
    print("any 'one user' or 'one channel' bottlenecks.")
    print("\nHowever... if we completely randomize where everything goes, how will we ever find a customer's history later? ;)")

if __name__ == "__main__":
    test_hash_balancing()