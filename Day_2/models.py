# This file contains the basic building blocks of our chat app

class Message:
    # __init__ is a special function that runs when we create a new Message object
    # self is a reference to the object being created, and we use it to set up the properties of the message
    # user_id: who sent the message
    # channel_id: which room or channel the message belongs to
    # content: the actual text of the message
    def __init__(self, user_id, channel_id, content):
        # Who sent the message
        self.user_id = user_id
        
        # Which room or channel the message belongs to
        self.channel_id = channel_id
        
        # The actual text of the message
        self.content = content
