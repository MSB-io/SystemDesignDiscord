# Day 2: The Basic System

## What We Built
Today, we set up the very foundation of our chat application. We created three simple parts:
1. **The Note (`models.py`)**: A simple way to structure a message with a sender, a destination (the channel), and the actual text.
2. **The Coffee Shop (`server.py`)**: A "single server" that basically acts as a giant notepad. Every time someone sends a message, it gets added directly to the bottom of a single, continuous list.
3. **The Test Run (`main.py`)**: A short script that opens the doors to 10 friends. They walk in, drop a message in the "General Chat", and we count the messages at the end of the day.

## Observations
Right now, the system creates the illusion of being "complete."
- Every message sent is successfully stored. 
- When we ask for the total count, it gives us the perfectly correct number (10). 
- It processes everything instantly because it is only handling 10 people.

If we stop here, we might mistakenly believe we have finished building a real-time chat application, but as we discussed in Day 1, we know this single notepad will not survive an actual crowd.

## How to Run This
Open your terminal and run:
`python3 main.py`

You will see 10 users drop their messages and a final confirmation that all 10 were recorded successfully.