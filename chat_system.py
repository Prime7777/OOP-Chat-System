# OOP Chat System Project
class User:
    def __init__(self,username):
        self.username=username
    
    def join_chatroom(self):
        print(f"{self.username} joins the chatroom.")
    
    def leave_chatroom(self):
        print(f"{self.username} left the chatroom.")
    
    def send_message(self,send_msg):
        print(f"send message: {send_msg}")
    
class Message:
    def __init__(self,sender,content,timestamp,new_msg):
        self.sender=sender
        self.content=content
        self.timestamp=timestamp
        self.new_msg=new_msg
    def show_display(self):
        print(f"New Message: {self.new_msg}")
    
class Chatroom:
    def __init__(self,room_name,users,chat_history):
        self.room_name=room_name
        self.users=users
        self.chat_history=chat_history
    def add_users(self,add):
        self.users=self.users.append(add)
        print(f"{add} is added by the owner.")
    def remove_user(self,remove):
        self.users = self.users - remove
        print(f"{remove} is removed by the owner.")
    


    


