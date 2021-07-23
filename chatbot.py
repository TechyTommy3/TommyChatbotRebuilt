import pickle
import os
import json
if os.path.exists("tommybot.mem") == True or False:
    with open('tommybot.mem', 'w') as tempmemory:
        chatbotname = input("What do you want your chatbot to be named?")
        data = {"name": chatbotname, "status": "new"}
        tempmemory = open("tommybot.mem", "w")
        jsony = json.dumps(data, separators=(',', ':')) + "\n"
        print(jsony)
        tempmemory.write(jsony)
        tempmemory.flush()
        tempmemory.close()
print("TommyChatbot")
print("Reading memory...")
memoryread = open("tommybot.mem", "r")
memorywrite = open("tommybot.mem", "w")
memory = json.loads(memoryread.read())
memoryread.close()
if memory["status"] == "new":
    print("Hi! My name is " + memory[name] + ". What's your name?")
    memory["yourname"] = input("You: ")
    pickle.dump(memory, memorywrite)
    print("Hi " + memory["yourname"] + "!")
    print("Anyways, isn't the Chatbot Network great?")
    answer = input("You: ")
    if answer == "Yes." or "Yes!":
        print("I think that too!")
    else:
        print("While, I don't understand why not.")
    print("Anyways, test!")
