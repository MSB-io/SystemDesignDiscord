import sys
import os

# Allow us to pull in our blueprints from Day 2 and Day 4
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_4.shards import ShardManager

# We create another new type of Security Guard (Manager).
# Our last rule (User-Based) failed because one person talked too much.
# So, the New Rule: "I will look at which table (Channel) the message belongs to,
# and send the customer to a specific coffee shop just for that table!"

class ChannelShardManager(ShardManager):

    def get_shard(self, channel_id):
        # We take the table's name (channel_id) and use some math to pick a shop.
        # This means all messages for "General_Chat" always go to the same shop,
        # and all messages for "Sports_Chat" always go to another shop.
        
        # Turn the channel name into a number so we can divide it
        numeric_id = sum(ord(char) for char in channel_id)
            
        shop_index = numeric_id % len(self.shards)
        
        # Return that specific shop
        return self.shards[shop_index]

    def send_message(self, message):
        # A customer hands the guard a message...
        
        # 1. The guard looks at the table destination (Channel ID) and picks a shop
        target_shop = self.get_shard(message.channel_id)
        
        # 2. The guard tells the customer to walk to that specific shop and drop the message!
        target_shop.store(message)
