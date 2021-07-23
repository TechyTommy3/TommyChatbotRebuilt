import pickle
print("TommyChatbot Setup")
print("This will WIPE ALL YOUR TommyChatbot memory. Press enter to confirm, or exit now.")
chatbotname = input("What do you want your chatbot to be named?")
data = {"name": chatbotname, "status": "new"}
memory = open("tommybot.mem", "wb")
pickle.dump(data, memory)
print("Suffeculy set up new TommyChatbot data on file tommybot.mem.")
memory.close()
input()
