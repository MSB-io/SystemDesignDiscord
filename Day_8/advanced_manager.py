import sys
import os

# Pull in our code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_7.strategies import HashShardManager
from Day_4.shards import Shard

# Day 8 is all about advanced things like detecting overloading shops
# and testing what happens if a coffee shop physically burns down (crashes).
# So we add some new skills to our old Security Guard manager from Day 7.

class AdvancedShardManager(HashShardManager):
    def __init__(self, num_shards):
        # Build our original math-based shops...
        super().__init__(num_shards)
        
        # But this time, add a tiny little sign to the front door of each shop saying "OPEN FOR BUSINESS"
        for shard in self.shards:
            shard.is_active = True
            
    def send_message(self, message):
        # 1. The guard uses our mathematical blender to pick a perfectly random shop
        target_shop = self.get_shard(message)
        
        # 2. Before pointing the customer to go to that shop, check the sign on the door!
        if not target_shop.is_active:
            # If the shop physically crashed, we drop their message (Data Loss!).
            # In a real system, you might redirect them, but right now, the message goes into a black hole.
            return False
            
        # 3. If everything is fine, store the message.
        target_shop.store(message)
        return True
        
    def detect_hotspots(self):
        # A new trick for the manager: Walk around and count the load.
        total_messages = sum(len(s.messages) for s in self.shards)
        if total_messages == 0: 
            return # Nobody is here yet
        
        print("\n[SECURITY CAMERA] Hotspot Detection Scan:")
        for shard in self.shards:
            # Calculate the percentage of total notes inside this specific shop
            load_percentage = (len(shard.messages) / total_messages) * 100
            print(f"Shop {shard.id} is managing {load_percentage:.1f}% of the workload.")
            
            # If one shop is holding more than HALF of the entire burden... that's a dangerous hotspot!
            if load_percentage > 50:
                print(f"  --> [WARNING] HOTSPOT DETECTED! Shop {shard.id} is dangerously overloaded! <--")
                
    def disable_shard(self, shard_id):
        # Oh no! The power went out in one of the shops!
        print(f"\n[DISASTER] Shop {shard_id} just caught fire and crashed! Turning off the 'OPEN' sign.")
        # Find the specific shop
        for shard in self.shards:
            if shard.id == shard_id:
                shard.is_active = False 
                break