import sys
import os

# Allow us to pull in our blueprints from Day 2 and Day 4
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_4.shards import ShardManager

# We create a new type of Security Guard (Manager) that follows our first rule.
# The Rule: "I will look at who is sending the message (User ID) and point them 
# to a specific coffee shop based purely on their ID number!"

class UserShardManager(ShardManager):

    def get_shard(self, user_id):
        # We take the user's ID number and use a little math (modulo) to pick a shop.
        # If we have 3 shops, and User_5 walks up: 5 divided by 3 has a remainder of 2.
        # So User_5 always goes to Shop 2!
        
        # We extract the number from strings like "User_5"
        try:
            numeric_id = int(str(user_id).split("_")[1])
        except:
            numeric_id = hash(user_id) # Fallback if it's a weird name
            
        shop_index = numeric_id % len(self.shards)
        
        # Return that specific shop
        return self.shards[shop_index]

    def send_message(self, message):
        # A customer hands the guard a message...
        
        # 1. The guard looks at who sent it (the User ID) and picks a shop
        target_shop = self.get_shard(message.user_id)
        
        # 2. The guard tells the customer to walk to that specific shop and drop the message!
        target_shop.store(message)