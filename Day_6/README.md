# Day 6: Channel-Based Sharding (The Viral Table Problem)

## What We Built
In Day 5, we learned that sending customers based on *who* they are (User-Based Routing) was a disaster. If one person never stops talking, they destroy whatever coffee shop they were assigned to.

So today, we invented a brand new rule and updated our security guard (`ChannelShardManager` in `strategies.py`):
*"Forget about who they are. Look at which conversation table (the Channel ID) they want to join, and assign that entire table permanently to one specific coffee shop!"*

For example:
- Every conversation at the "Sports" table is kept at **Shop 0**.
- Every conversation at the "Gaming" table is kept at **Shop 1**.

## What Went Right
Initially, things looked fantastic again! We invited our old "Influencer" (who had broken our system yesterday) back. Since the influencer talked equally across 5 different tables, our new rule sent their messages to all 3 shops. The load was shared perfectly, and the influencer problem was completely fixed.

## What Went Terribly Wrong (The Second Wrong Decision)
In the real world, massive events happen that cause the entire planet to want to talk about the exact same thing at the exact same time.

To prove why our new rule was *still* broken, we simulated a viral afternoon: **The Cricket Final**. 

A massive crowd of 10,000 completely different people rushed in. The problem? Every single one of them wanted to talk at the "Cricket_Final" table. 
Because our rule forces a single table (Channel) to *always* stay inside the exact same shop, our security guard sent all 10,000 of those people directly to **Shop 1**.

### The Result
- **Shop 0:** 60 messages (empty, employees bored).
- **Shop 1:** 10,060 messages (completely overwhelmed, the notepad is out of space).
- **Shop 2:** 30 messages (also completely empty).

## Conclusion
Routing people based on their conversation topic (Channel ID) just moves the problem. If an event goes completely viral on a single channel, that specific channel becomes a massive **"hotspot."** 
It will single-handedly destroy whichever coffee shop it was assigned to, while the rest of our franchise sits completely useless. 

## How to Run This
Open your terminal and run:
`python3 test_viral_channel.py`

You will clearly see our Shops perfectly balanced in the morning, and then completely crushed by a 10,000-message viral hotspot in the afternoon!