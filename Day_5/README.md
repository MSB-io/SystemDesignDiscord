# Day 5: User-Based Sharding (The Influencer Problem)

## What We Built
In Day 4, our Security Guard (Manager) had no idea where to send customers. So today, we invented our very first rule: **User-Based Routing.**

We created `UserShardManager` inside `strategies.py` and gave our guard a clear command:
*"Look at the person's name (User ID). Do a little math to assign them securely to exactly one shop. Then, make sure they only ever use that specific shop forever."*

For example:
- **User 1** always goes to Shop 1.
- **User 2** always goes to Shop 2.
- **User 3** always goes to Shop 3.

## What Went Right
Initially, things looked fantastic! We ran our test (`test_influencer.py`) and invited 10 random friends to talk. Our math perfectly divided them up among our 3 shops. Each shop had roughly the exact same number of messages (about 15-20 notes each). Everyone was happy that the load was perfectly balanced.

## What Went Terribly Wrong (The First Wrong Decision)
In the real world, not everyone talks an equal amount. 
To prove why our rule was broken, we sent an **"Influencer"** (`User_999`) to our front door in the afternoon. This specific person brought 5,000 automated messages with them.

Because our rule forces a person to *always* go to the exact same shop, our security guard sent all 5,000 of those messages directly to **Shop 0**. 

### The Result
- **Shop 0:** 5015 messages (completely overwhelmed, about to crash and run out of paper again).
- **Shop 1:** 20 messages (bored, employees doing nothing).
- **Shop 2:** 15 messages (also completely empty).

## Conclusion
Routing people based purely on *who* they are (User ID) creates a massive danger of **"load imbalance."** If one person talks ten thousand times more than the average user, they will single-handedly destroy whichever single shop they were randomly assigned to, while the rest of our franchise sits completely useless. We need to think of a better rule!

## How to Run This
Open your terminal and run:
`python3 test_influencer.py`

You will clearly see one coffee shop breaking under the pressure of 5,000 notes, while the other two have only 15-20.