import sys
import os
import hashlib
import time

# Allow us to pull in our blueprints from the previous days
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_4.shards import ShardManager

# Our new rule (Hash-Based Sharding).
# We realized that picking shops based on WHO is talking (User ID) 
# or WHERE they are talking (Channel ID) always leads to a disaster 
# if one person or channel goes viral.
#
# NEW RULE: "I will look at the MESSAGE ITSELF. Every single message gets
# a unique, mathematically random-looking number. We divide THAT number 
# by 3 to pick the shop. This means every single message has a perfectly 
# equal chance of going to any shop, guaranteed!"

class HashShardManager(ShardManager):

    def get_shard(self, message):
        # We need a string of text that is completely unique for every single message.
        # We combine the person's name, the channel, what they said, and the exact second they said it.
        unique_string = f"{message.user_id}_{message.channel_id}_{message.content}_{time.time()}"
        
        # We put this unique string into our "md5" blender.
        # Think of md5 as a super-powered Bingo Number generator. 
        # It takes any word and instantly spits out a giant number based on that word.
        # Even if two strings are almost identical, the MD5 numbers will be completely different!
        hash_number = int(hashlib.md5(unique_string.encode()).hexdigest(), 16)
        
        # Now we just divide that giant number by the number of shops (3)
        # to pick our table (e.g. remainder 0 goes to Shop 0)
        shop_index = hash_number % len(self.shards)
        
        # Return that perfectly random shop
        return self.shards[shop_index]

    def send_message(self, message):
        # 1. The guard uses our new mathematical blender to pick a perfectly random shop
        target_shop = self.get_shard(message)
        
        # 2. Tell the customer to go to that specific shop!
        target_shop.store(message)
