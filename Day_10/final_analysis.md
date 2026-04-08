# Day 10: Final Analysis

This completes the assignment logic! Here is the final written analysis for the remaining questions as requested in the assignment brief.

## 1. Which shard failed first and why?
In **Day 5 (User-Based Sharding)**, Shard 0 failed first.
Because our routing mathematical rule dictated that people with the same User ID always went to the exact same server (coffee shop), the moment an "Influencer" arrived and spammed 5,000 messages non-stop, the specific single server they were assigned to (`User_999` % 3 = `0`) completely collapsed under 5,000+ messages while Shards 1 and 2 sat completely empty with roughly 20 messages each.

## 2. Which strategy looked good but failed under spike?
In **Day 6 (Channel-Based Sharding)**, the rule looked fantastic at first. By routing traffic based on the conversation topic (the Channel/Table), our Influencer from Day 5 was spread out evenly across the 3 servers because they talked about different topics. The load looked perfectly balanced.

However, it instantly failed when the real-world spike hit: The Cricket Final went viral. 10,000 completely different people rushed the servers. Because they ALL wanted to talk about the exact same topic (`Cricket_Final`), the routing math sent all 10,000 people to a single server (Shard 1). The server acting as a "hotspot" for that channel completely collapsed, despite 10,000 unique users participating.

## 3. What happens if shards increase from 3 → 10?
If we suddenly bought 7 more coffee shops (expanding from 3 to 10 servers), our entire mathematical system (Modulo Hashing) would instantly break. 

Our security guard (Shard Manager) uses simple math: `hash_number % 3`. 
If `User_5 % 3` sends a user to Shop 2 today, and we change the math to `User_5 % 10` tomorrow, that exact same user is now suddenly told to go to Shop 5. 
When they arrive at Shop 5, all of their previous message history (which is sitting locked inside Shop 2) will be completely missing. This is known as a **Rehashing Nightmare**. Expanding the servers breaks all previous routing destinations, causing massive data loss from the user's perspective.

## 4. What breaks when one shard goes down?
In **Day 8 (Stress & Failure Simulation)**, we physically turned off the "OPEN" sign for Shard 0 (simulating a fire or power outage at that coffee shop). 
Because our mathematical routing rules (User, Channel, or Hash) strictly demand where a customer goes before even checking if the server is still alive, our system continued to throw exactly 1/3rd of our traffic directly into the "burning building".

The result? Out of 5,000 incoming messages during the nighttime spike, over 1,600 real-world messages completely vanished into thin air (Data Loss). The math distributed the pain evenly, but it couldn't adapt to reality.