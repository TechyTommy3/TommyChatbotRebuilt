import json
print("Notice: TommyChatbot 1.0 does not have proper saving.")
print("TommyChatbot Setup")
print("This will WIPE ALL YOUR TommyChatbot memory. Press enter to confirm, or exit now.")
chatbotname = input("What do you want your chatbot to be named?")
data = {"name": chatbotname, "status": "new"}
jsondat = json.dumps(data, separators=(',', ':'))
#print("Suffeculy set up new TommyChatbot data on file tommybot.mem.")
print("Needed data: " + jsondat)
input()
