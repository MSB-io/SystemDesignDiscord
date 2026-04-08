import sys
import os
import time

# Pull in our code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_8.advanced_manager import AdvancedShardManager

# Today we tackle the hardest part of our Math-Based (Hash) Routing.
# Because we threw every single message to a totally random coffee shop,
# when a customer asks "What was the last thing said at the Sports table?",
# we have absolutely no idea which shop has the answer!

class QueryShardManager(AdvancedShardManager):
            
    def get_last_10_messages(self, channel_id):
        # A customer walked up and asked for the last 10 messages from a specific table (channel)
        print(f"\n[QUERY] Customer requested the last 10 messages for '{channel_id}'")
        
        all_found_messages = []
        shops_checked = 0
        
        # 1. Because we used random math (hashing) to scatter the messages, 
        # the Security Guard HAS to go physically check every single shop.
        for shard in self.shards:
            # Skip shops that burned down
            if not shard.is_active:
                continue
                
            shops_checked += 1
            
            # The guard looks through this specific shop's notepad
            # and gathers anything written for this specific table
            for msg in shard.messages:
                if msg.channel_id == channel_id:
                    all_found_messages.append(msg)
                    
        print(f"  -> To find these, the guard had to physically search through {shops_checked} different shops!")
        
        # 2. We now have a giant pile of scattered notes from different shops.
        # We must organize them by the exact physical time they were written down.
        # (Assuming we wrote a timestamp on each note when creating the message)
        all_found_messages.sort(key=lambda m: m.timestamp, reverse=True)
        
        # 3. Hand the top 10 most recent notes back to the customer
        last_10 = all_found_messages[:10]
        
        # We will return them in chronological order so they read like a normal book (oldest to newest)
        return list(reversed(last_10))

