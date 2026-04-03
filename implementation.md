# Implementation Plan: Discord Sharding and Scaling Simulation

This plan outlines the step-by-step implementation for the Discord system design assignment, specifically structured to match the explicit daily deliverables, enabling you to build up a progressive Git commit history.

## Overview
The goal is to simulate a chat system's evolution from a single monolithic server to an advanced sharded architecture, deliberately exposing bottlenecks, hotspots, and handling failure scenarios under load.

## Steps

### Phase 1: Foundation (April 2 - April 4)
1. **April 2 (Day 1): System Thinking Setup** 
   - Define structure and create `docs/system_thinking.md`.
   - Write a 1-page analysis on system bottlenecks (memory, load, hotspots) identifying points of failure during a massive spike without writing logic yet.
2. **April 3 (Day 2): Basic System**
   - Create core `Message` class in `src/models.py` (adding a simple sequence id/timestamp for querying later).
   - Create `ChatServer` in `src/server.py` with global array based on starter code.
   - Run tests showing basic capability: 10 users send messages successfully.
3. **April 4 (Day 3): Scaling Awareness**
   - Implement `tests/load_simulator.py`.
   - Simulate 10,000 users attempting to message a single `ChatServer` instance. Output execution slowdown or memory stats.
   - Create `docs/scaling_observations.md` and append this insight.

### Phase 2: Sharding Strategies (April 5 - April 8)
4. **April 5 (Day 4): Shards Introduction**
   - Implement `Shard` and base `ShardManager` classes in `src/server.py`.
   - Remove global storage completely. Run tests proving shards operate independently.
5. **April 6 (Day 5): User-Based Sharding**
   - Implement `UserShardManager` using modulus shard assignment in `src/strategies.py`.
   - Update simulator with an "influencer" scenario.
   - Print shard counts to demonstrate one severely overloaded shard and mostly empty peers.
6. **April 7 (Day 6): Channel-Based Sharding**
   - Implement `ChannelShardManager`.
   - Simulate a trending cricket final event in a specific channel.
   - Provide command line logs to prove hotspot failure points vs previous days strategy.
7. **April 8 (Day 7): Hash-Based Sharding**
   - Implement `HashShardManager` using standard MD5 hashing in `src/strategies.py`.
   - Evaluate whether to hash user_id, channel_id, or message_id and test for better, yet still imperfect, distribution.

### Phase 3: Advanced Stress, Querying, and Failure (April 9 - April 10)
8. **April 9 (Day 8): Stress & Failure Simulation**
   - Add warning diagnostics in `ShardManager` to detect load imbalances over 50%.
   - Implement `disable_shard(shard_id)` to mock a crashed server. Run simulation simulating "one normal day", "one spike", and "one failure," logging data loss.
9. **April 10 (Day 9): Cross-Shard Queries & Final Analysis**
   - Program the `get_last_10_messages(channel_id)` capability across isolated shards.
   - Add tracking mechanisms printing exactly how many shards had to be checked.
   - Write final system insights in `docs/final_analysis.md` answering what breaks when expanding from 3 -> 10 shards.

## Relevant files
- `docs/system_thinking.md` — Initial systems bottleneck analysis.
- `src/models.py` — Application components (Message class).
- `src/server.py` — Storage components (ChatServer, Shard, ShardManager).
- `src/strategies.py` — Custom router logic (User, Channel, and Hashing logic).
- `tests/load_simulator.py` — Main entry points to trigger daily assignments' stress tests.
- `docs/scaling_observations.md` — Incremental notes for each failed architecture.
- `docs/final_analysis.md` — Responses for final grading checks.

## Verification
1. Ensure the simulation code explicitly outputs `print` statements detailing message-to-shard counts to visually prove the assignment requirement.
2. Ensure the code operates without hidden global state mapping, sticking strictly to independent shards.
3. Verify failure simulations appropriately cause data loss/inconsistency (deliberate failure points intended by assignment goals). 

## Decisions
- Git workflow: Code incrementally every day (starting with Day 1) and push to simulate real daily commits, reflecting natural project progression.
- Implementation logic (Messages): Rely on a simple integer sequence or python timestamp to easily fetch the "last 10 messages" for the cross-shard query. 
- Language: Python, building closely on the provided starter code.
- Scope: Deliberately implementing and testing flawed logic (e.g. User-based routing) based on daily goals.
