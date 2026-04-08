import sys
import os

# Allow us to pull in our code from the previous days
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Message
from Day_6.strategies import ChannelShardManager

def test_viral_table():
    print("--- Welcome to the new 'Channel-Based' system! ---")
    
    # We open up our 3 coffee shops again, this time with our new safety rule.
    manager = ChannelShardManager(num_shards=3)
    
    print("\nOur previous rule (By User) failed because one person talked too much.")
    print("Our new rule: Everyone talking at the 'Tech' table goes to one shop,")
    print("while everyone talking at the 'Sports' table goes to another.")
    print("This should fix the influencer problem, right? Let's see.")
    
    # ---------------------------------------------
    # Scenario: The Influencer is fixed!
    # ---------------------------------------------
    print("\n[MORNING] Our old Influencer shows up, but they are talking in 5 different channels (tables)!")
    
    influencer = "User_999"
    # Even if they talk non-stop, if they spread it across tables, the load splits.
    channels = ["Tech", "Sports", "Gaming", "News", "Movies"]
    for i in range(150):
        channel_name = channels[i % len(channels)]
        msg = Message(influencer, channel_name, "Buy my merch!")
        manager.send_message(msg)
            
    print("Morning check on our 3 shops:")
    manager.show_shard_stats()
    
    print("\nResults: It worked! The Influencer's load was spread across the tables!")
    
    # ---------------------------------------------
    # Scenario: The Viral Event (The Second Wrong Decision)
    # ---------------------------------------------
    print("\n[AFTERNOON] A massive worldwide event happens: The Cricket Final!")
    print("Suddenly, 10,000 completely different people rush in...")
    
    # Thousands of random people show up
    for friend_id in range(1, 10001):
        user = f"User_{friend_id}"
        
        # But wait... they ALL want to sit at the 'Cricket_Final' table!
        msg = Message(user, "Cricket_Final", "WHAT A GAME!")
        manager.send_message(msg)
        
    print("\nAfternoon check on our 3 shops after the viral event:")
    manager.show_shard_stats()
    
    print("\n--- The Conclusion ---")
    print("Because our new rule assigns an entire conversational table (Channel) to just one shop,")
    print("when an event goes entirely viral on a single table, the shop assigned to that table collapses.")
    print("Once again, one single location gets completely crushed while the others sit empty!")

if __name__ == "__main__":
    test_viral_table()