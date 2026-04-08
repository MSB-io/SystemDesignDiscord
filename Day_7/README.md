# Day 7: Hash-Based Sharding (The Math Approach)

## What We Built
In Day 6, our system completely broke down when one specific channel went viral (a hotspot). So today, we invented our most powerful rule yet: **Hash-Based Routing.**

We updated our security guard manager one last time (`HashShardManager` in `strategies.py`). We realized that picking shops based on **who** is talking (User ID) or **where** they are talking (Channel ID) is always dangerous if things aren't perfectly equal in real life.

**Our New Magical Rule:**
*"I am going to take everything about this message—who sent it, what they said, what channel it belongs to, and even the exact second they sent it. I will throw all of those details into a powerful math blender called 'MD5'."*

MD5 generates a giant, completely random-looking number based on those details. Even if two people say the exact same thing a second apart, their numbers will be totally different. We then just divide that giant number by our number of coffee shops (3). 

## What Went Right (Perfect Balance)
This rule perfectly guarantees that **every single message gets randomly thrown into a different coffee shop**, regardless of who sent it or what channel they use. 

We proved this by introducing our old enemies to the system at the exact same time:
- The **Influencer** who talks too much.
- The **Cricket Final** that went super-viral.

Even with thousands of crazy, uneven messages pouring in, our three coffee shops automatically received almost the exact same workload (around 4,990 notes each). The Hotspot problem is formally solved!

## The Catch
We have completely destroyed bottlenecks and hotspots by totally shuffling our notes like a massive deck of cards across 3 buildings. 
But if we want to ask *"Hey, what were the last 10 messages from the Tech Channel?"...* we no longer know which building holds which piece of the conversation. (We address this nightmare in Day 10).

## How to Run This
Open your terminal and run:
`python3 test_hashing.py`