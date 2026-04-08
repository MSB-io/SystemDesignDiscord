# Day 4: Opening More Shops (Introducing Shards)

## What We Built
Because our single, giant coffee shop from Day 3 was getting too crowded and slow, we decided to expand. 
We essentially opened a franchise: 3 smaller coffee shops instead of one massive building. In the software world, separating your storage space like this is called **"Sharding."**

1. **The Small Coffee Shop (`shards.py - Shard class`)**: This represents just one single location. It has its very own private notepad to store messages, completely independent of the others.
2. **The Security Guard (`shards.py - ShardManager class`)**: This represents the overall manager standing at the front door. When a customer walks up to the door with a message, the manager is supposed to tell them exactly which of our 3 shops to go into.

## The Problem
Right now, our manager doesn't have any rules! If you try running `test_shards.py`, a customer walks up to drop a message, but the manager has no idea where to send them. As a result, all 3 shops stay completely empty.

We successfully fixed the problem of having one massive, slow pile of notes by separating our storage, but until we invent a system (a routing rule) to divide the crowd fairly among the 3 shops, our chat app is broken.

## How to Run This
Open your terminal and run:
`python3 test_shards.py`

You will see that 0 messages make it into any of the 3 shops.