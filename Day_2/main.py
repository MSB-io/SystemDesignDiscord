from models import Message # We need to import the Message class from our models file to create message objects
from server import ChatServer # We need to import the ChatServer class from our server file to create a chat server instance

def test_basic_system():
    print("Welcome to our Chat App (Single Server)")
    print("We are opening the doors for a small group of friends.")
    
    # We open up our single server
    # what does this do ? It creates a new instance of the ChatServer class, which initializes an empty list to store messages. This server will be responsible for handling all incoming messages and keeping track of them in the notepad (the list).
    coffee_shop = ChatServer()
    
    # 10 friends enter the shop and start sending messages
    for i in range(1, 11):
        user = f"User_{i}"
        channel = "General_Chat"
        content = "Hey everyone! How is it going?"
        
        # Create a new message note
        # what does this do ? It creates a new instance of the Message class with the specified user, channel, and content. This message object represents a single message that a user wants to send to the chat server. The message object will have properties like user_id, channel_id, and content that store the information about the message.
        msg = Message(user, channel, content)
        
        # Hand the note to the server reception
        # what does this do ? It calls the send_message method of the ChatServer instance (coffee_shop) and passes the message object (msg) as an argument. This method will add the message to the server's notepad (the list of messages). The server will keep track of all messages sent by users, and we can later check how many messages have been recorded.
        coffee_shop.send_message(msg)
        print(f"[{user}] dropped a message in [{channel}]")
    
    # \n is a special character that creates a new line in the output, so this will print a blank line before the next message.
    print("\n--- End of the Day ---")
    # See how the server is doing
    # what does this do ? It calls the stats method of the ChatServer instance (coffee_shop) to check how many messages have been recorded in the notepad. The stats method will print the total number of messages that have been sent to the server, which gives us an idea of how active the chat was during the day.
    coffee_shop.stats()

# This is a common Python idiom that checks if the script is being run directly (as the main program) rather than imported as a module in another script. If this condition is true, it will execute the code inside this block, which in this case is calling the test_basic_system() function to run our chat app simulation.
if __name__ == "__main__":
    test_basic_system()
