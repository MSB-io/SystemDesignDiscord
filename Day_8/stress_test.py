import sys
import os

# Pull in our code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Day_2.models import Message
from Day_8.advanced_manager import AdvancedShardManager

def simulate_stress_and_failure():
    print("--- Welcome to Day 8! Our New Manager is taking over... ---")
    
    # We open up our 3 safe coffee shops with the smartest math-based routing manager.
    manager = AdvancedShardManager(num_shards=3)
    
    # ---------------------------------------------
    # 1. Normal Day Load Simulation
    # ---------------------------------------------
    print("\n[MORNING] A nice normal, sunny morning in our coffee shops...")
    
    import random
    
    for i in range(1500):
        # 1500 random people say Hello in 50 random channels
        user = f"User_{random.randint(1, 1000)}"
        channel = f"Channel_{random.randint(1, 50)}"
        msg = Message(user, channel, "hello normal world")
        manager.send_message(msg)
        
    print("Let's ask the security guard to scan for hotspots!")
    manager.detect_hotspots()
    
    # ---------------------------------------------
    # 2. Viral Event (Extreme Spike) Simulation
    # ---------------------------------------------
    print("\n[AFTERNOON] An insane global event happens (The 'Spike')!")
    
    # An extra 50,000 people rush through the doors.
    # Our math perfectly routes them because we learned from Day 5/6!
    # ... BUT wait! What if our perfectly random math accidentally points slightly
    # mostly toward one shop? Or more likely, what if a shop burns down?
    
    for i in range(25000):
        user = f"User_{random.randint(1, 10000)}"
        channel = "Global_Event_Channel"
        msg = Message(user, channel, "SPIKE!")
        manager.send_message(msg)
        
    print("\nChecking the load after the Spike:")
    manager.detect_hotspots()

    # ---------------------------------------------
    # 3. Server Crash Simulation
    # ---------------------------------------------
    
    print("\n[NIGHT] Disaster Strikes!")
    # We simulate a power failure at Shop 0
    manager.disable_shard(0)
    
    print("Now, let's see what happens to the next 5,000 customers who try to enter...")
    
    dropped_messages = 0
    saved_messages = 0
    for i in range(5000):
        user = f"User_{random.randint(1, 1000)}"
        channel = "Night_Chat"
        msg = Message(user, channel, "Is anyone awake?")
        
        # The manager tells them to go to a shop. But they don't know it burned down!
        success = manager.send_message(msg)
        if not success:
            dropped_messages += 1
        else:
            saved_messages += 1

    print("\n--- The Conclusion ---")
    print(f"Messages Safe in Shop 1 and 2: {saved_messages}")
    print(f"Messages completely LOST forever in the fire of Shop 0: {dropped_messages}")
    
    print("\nWhy did this happen? Because when we have 3 coffee shops, and one burns down,")
    print("approximately 1/3rd of the messages (and 1/3rd of the customers) are mathematically")
    print("still ordered to go to the burned down shop. Over 1,600 messages just disappeared into thin air!")

if __name__ == "__main__":
    simulate_stress_and_failure()