# Day 8: Systems Evolution (The Final Stress & Failure)

## What We Built
In Day 7, our system finally reached perfection for *writing* new messages evenly across all 3 coffee shops. But real-world chat apps aren't just about perfectly storing data. They're about what happens **when things physically break.**

Today we upgraded our manager to become an `AdvancedShardManager` which has two brand new tools to help us observe the real world:
1. **The Hotspot Detector**: The manager walks around to all the coffee shops and prints out a percentage of how much of our entire app they are holding. If a single shop is holding over 50% of our entire business, a massive warning goes off.
2. **The 'Close' Sign**: We gave the manager the physical power to actually close down a specific coffee shop (representing a server crashing or losing electricity).

## What Went Terribly Wrong
We simulated a busy 24-hours for our 3 perfectly-balanced coffee shops.
- **Morning (Normal Day Load):** The shops handle normal traffic easily. The Hotspot detector reads a perfect 33% load on all three.
- **Afternoon (Extreme Spike):** A sudden, massive event happens. 25,000 extra people rush in immediately. The math still works flawlessly, managing roughly 33% on all three over the entire afternoon.
- **Night (Server Crash Simulation):** We finally pull the plug on Coffee Shop 0 (Shard 0) mid-sentence while 5,000 more users are attempting to message.

### The Result
Because our "math rule" strictly decides where a customer MUST go based on the message itself (without checking if the shop actually exists anymore), our rule suddenly fails when reality changes.

- Over 3,300 people successfully walked into Shop 1 and Shop 2.
- However, our manager continued trying to send roughly 1,600 people into the burning remains of Shop 0. **Over 1,600 real-world messages permanently disappeared into thin air without ever saving to the system.**

## Conclusion
Our math successfully distributes traffic without bias, but completely ignored reality. We realized that simple modulus math (`hash_number % 3 shops`) is extremely brittle when real-world factors change (like one of the 3 shops breaking, or attempting to upgrade from 3 to 10 shops suddenly). In a commercial setting, losing 1/3 of an entire application's data is catastrophic.

## How to Run This
Open your terminal and run:
`python3 stress_test.py`

You will see exactly how we handled perfectly balanced spikes, only to drop thousands of real data messages during a sudden physical server crash!