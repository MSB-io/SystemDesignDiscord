# This represents our single coffee shop (single server)
# where everything happens in one place.

class ChatServer:
    # __init__ is a special function that runs when we create a new Message object
    # self is a reference to the object being created, and we use it to set up the properties of the message
    def __init__(self):
        # The single notepad where we write down every single message
        # This is a global list that holds everything.
        self.messages = []
    
    def send_message(self, message):
        # A user says something, and we write it down at the bottom of the notepad
        self.messages.append(message)

    def stats(self):
        # Check how many messages we have recorded so far
        print("Total messages on the notepad:", len(self.messages))
