# Day 9/10: Cross-Shard Querying 

## What We Built
In Day 7 & 8, we proved that throwing messages randomly into 3 different coffee shops based purely on the `Message ID` math (hashing) completely solved the hotspot (crashing) problem. 

**However, we discovered a new nightmare:**
When a brand new person walks up to the front door and asks, *"What were the last 10 things people said at the Sports table?"* we have absolutely no idea which of the 3 coffee shops holds those 10 notes. They could literally be anywhere!

To fix this, we created the `QueryShardManager` to do a **Cross-Shard Query**. 

## The Process
Because we completely shuffled the conversation across multiple buildings, our Security Guard Manager was forced to do a lot of physical running around to answer a single question:
1. The guard had to sprint into Shop 0, grab all notes about "Sports."
2. The guard then sprinted into Shop 1, grabbed all notes about "Sports."
3. The guard finally sprinted into Shop 2, grabbed all notes about "Sports."
4. The guard then dumped this massive pile of scattered notes onto the floor, read the exact second each note was written (the timestamp), and manually organized them from oldest to newest.
5. Only then could the guard hand the customer the 10 most recent notes!

## The Conclusion
**Writing** messages with random math hashing is incredibly easy, safe, and balanced. It almost guarantees that a server hotspot will never crash the system.
**Reading** messages under this system is incredibly slow, dangerous, and expensive (often called the Scatter-Gather problem). 

Because our manager had to physically walk to all 3 buildings to stitch one conversation back together, we can clearly see why this system would completely freeze and catch fire if we expanded from 3 coffee shops to 10,000 coffee shops. Every single time a user opened the app, a guard would have to check 10,000 buildings simultaneously!

## How to Run This
Open your terminal and run:
`python3 test_query.py`

You will see exactly how we successfully gathered and stitched back together messages #91 through #100 after they had been randomly scattered to 3 completely different locations!