# # OOP Chat System Project
# class User:
#     def __init__(self,username):
#         self.username=username
    
#     def join_chatroom(self):
#         print(f"{self.username} joins the chatroom.")
    
#     def leave_chatroom(self):
#         print(f"{self.username} left the chatroom.")
    
#     def send_message(self,send_msg):
#         print(f"send message: {send_msg}")
    
# class Message:
#     def __init__(self,sender,content,timestamp,new_msg):
#         self.sender=sender
#         self.content=content
#         self.timestamp=timestamp
#         self.new_msg=new_msg
#     def show_display(self):
#         print(f"New Message: {self.new_msg}")
    
# class Chatroom:
#     def __init__(self,room_name,users,chat_history):
#         self.room_name=room_name
#         self.users=users
#         self.chat_history=chat_history
#     def add_users(self,add):
#         self.users=self.users.append(add)
#         print(f"{add} is added by the owner.")
#     def remove_user(self,remove):
#         self.users = self.users - remove
#         print(f"{remove} is removed by the owner.")
    


   
class Message:
    message_counter = 1   # simple counter
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1
        def __str__(self):
            return f"({self.id}) {self.sender.username}: {self.content}"
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None
        def join_chatroom(self, chatroom):
            if self.chatroom:
                print(f"{self.username} is already in a chatroom.")
            else:
                chatroom.add_user(self)
                self.chatroom = chatroom
                print(f"{self.username} joined {chatroom.name}")
    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None
        def send_message(self, content):
            if not self.chatroom:
                print(f"{self.username} cannot send a message (not in a chatroom).")
            else:
                self.chatroom.broadcast(self, content)
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []
    def add_user(self, user):
        self.users.append(user)
    def remove_user(self, user):
        self.users.remove(user)
    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)   
    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)

