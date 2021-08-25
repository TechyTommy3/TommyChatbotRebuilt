import json
print("TommyChatbot Memory Editor")
print("This program lets you edit your TommyChatbot memory.")
print("NOTICE: This pulls statuses straight from the JSON.")
chatbotdata = open("tommybot.mem", "r")
memory = json.loads(chatbotdata.read())
print("----- Current Chatbot Data -----")
print("Status: " + memory['status'])
print("Name: " + memory['name'])
if 'yourname' in memory:
    print("Creator's Name: " + memory['yourname'])
if 'talkbot' in memory:
    print("Mainly talks about: " + memory['talkbot'])
if 'engine' in memory:
    print("Engine: TommyChatbot Framework")
else:
    print("Engine: TommyChatbot")