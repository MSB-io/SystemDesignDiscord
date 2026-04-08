# This file holds the logic for our new "Multiple Servers" setup.
# Think of it as buying more coffee shops.

class Shard:
    # A single Shard is just like one single Coffee Shop from Day 2.
    # It has its own, completely separate notepad for messages.
    def __init__(self, shard_id):
        # A name or number to identify this specific shop (like "Shop #1")
        self.id = shard_id
        
        # This shop's own private notepad. It does not share this list with anyone else!
        self.messages = []

    def store(self, message):
        # Someone drops a message in THIS specific shop
        self.messages.append(message)


class ShardManager:
    # The ShardManager is like a security guard standing at our new main entrance.
    # When a customer arrives with a message, the guard figures out which of our 
    # multiple coffee shops the customer should actually go to.
    def __init__(self, num_shards):
        # We start by opening up a certain number of new shops.
        # For example, if num_shards is 3, we open Shop 0, Shop 1, and Shop 2.
        self.shards = [Shard(i) for i in range(num_shards)]

    def send_message(self, message):
        # A customer arrived and handed the guard a message.
        # But wait! Do we send them to Shop 0, Shop 1, or Shop 2?
        # 
        # (This is intentionally left blank for now! We haven't decided the rules 
        # for where people should go yet. That's for Day 5 and beyond.)
        pass
        
    def show_shard_stats(self):
        # The manager checks every single shop to see how many notes are on their notepads.
        for shard in self.shards:
            print(f"Shop (Shard) {shard.id} has {len(shard.messages)} notes.")