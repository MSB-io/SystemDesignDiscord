import sys
import os

# Allow us to pull in our code from the previous days
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Message
from Day_5.strategies import UserShardManager

def test_influencer_traffic():
    print("--- Welcome Back! We now have rules for our 3 shops! ---")
    
    # We open up our 3 coffee shops.
    # Our new guard manager now directs people perfectly based on who they are.
    manager = UserShardManager(num_shards=3)
    
    print("\nOur new rule: Every person is permanently assigned to their own specific shop.")
    print("User_1 always goes to Shop 1. User_2 goes to Shop 2, etc.")
    
    # ---------------------------------------------
    # Scenario: Normal Friends Chatting
    # ---------------------------------------------
    import random
    
    print("\n[MORNING] A few friends show up and start chatting...")
    # 10 random friends show up, each dropping 5 messages
    for friend_id in range(1, 11):
        for _ in range(5):
            user = f"User_{friend_id}"
            channel = "General_Chat"
            msg = Message(user, channel, "Morning!")
            manager.send_message(msg)
            
    print("Morning check on our 3 shops:")
    manager.show_shard_stats()
    
    print("\nResults: It looks perfectly balanced! Everyone is separated nicely.")

    # ---------------------------------------------
    # Scenario: The Influencer (The Real Problem)
    # ---------------------------------------------
    print("\n[AFTERNOON] An Influencer (User_999) arrives with 5,000 automated messages...")
    
    influencer = "User_999"
    # This single person starts shouting non-stop
    for i in range(5000):
        msg = Message(influencer, "General_Chat", f"Buy my merch! message #{i}")
        manager.send_message(msg)
        
    print("\nAfternoon check on our 3 shops:")
    manager.show_shard_stats()
    
    print("\n--- The Conclusion ---")
    print("Because our rule forces a single person to always use the exact same shop,")
    print("if one person never stops talking, that specific shop will instantly break")
    print("while the other two shops sit completely empty and useless!")

if __name__ == "__main__":
    test_influencer_traffic()