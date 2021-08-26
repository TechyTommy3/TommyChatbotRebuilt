import os
import json
import time
if os.path.isfile("tommybot.mem") == False:
    print("Welcome to the TommyChatbot setup wizard!")
    print("This program makes a new TommyChatbot database that is saved to as you speak.")
    print("To make your copy portable, copy chatbot.py and tommybot.mem over.")
    print("First, what do you want your chatbot to be named?")
    chatbotname = input("You: ")
    print("Now, this file is named tommybot.mem and is in JSON format.")
    print("YOU must not rename this file!")
    print("If you do, than this will appear again.")
    print("Now, your sign-up request is at number #30.")
    print("See you when you are at #1!")
    for x in range(30):
        print(x)
        time.sleep(0.2)
    print("OK!")
    #This is because w+ does not create a file for us to work with automaticlly.
    rtempchatbot = open("tommybot.mem", "w")
    rtempchatbot.close()
    tempchatbot = open("tommybot.mem", "r+")
    chatbot = {"name": chatbotname, "status": "new"}
    tempchatbot.write(json.dumps(chatbot, separators=(',', ':')))
    tempchatbot.close()
    time.sleep(5)
    print("You are now registered!")
    print("Enjoy TommyChatbot and the whole Chatbot Network!")
    print("(Chatbot Network is a fictional name.)")
    print("(If Chatbot Network is a real name, than that is a coindence that Tommy did not mean to happen.)")
    print("(We are not affilated with the website chatbot.net, which goes under the name Chatbot Network.)")
print("TommyChatbot")
print("Decoding and loading data...")
chatbotdata = open("tommybot.mem", "r")
memory = json.loads(chatbotdata.read())
def save():
    global chatbotdata
    chatbotdata.close()
    chatbot = open("tommybot.mem", "w")
    chatbot.write(json.dumps(memory, separators=(',', ':')))
    chatbot.close()
    chatbotdata = open("tommybot.mem", "r")
if memory["status"] == "new":
    print("Hi! My name is " + memory["name"] + ". What's your name?")
    memory["yourname"] = input("You: ")
    memory["yourname"] = memory["yourname"].replace(".", "").replace("?", "").replace("!", "")
    print("Hi " + memory["yourname"] + "!")
    save()
    print("Anyways, isn't the Chatbot Network great?")
    answer = input("You: ")
    if "Yes" in answer:
        print("I think that too!")
        memory["cblike"] = "yes"
    else:
        print("While, I don't understand why not.")
        memory["cblike"] = "no"
    save()
    #Replaced all other charters in a line above
    print("Anyways, thanks for talking to me today, " + memory["yourname"] + "!")
    memory["status"] = "littlenewer"
    save()
    print("Let's chat!")
if memory['status'] == "littlenewer":
    print("What should we talk about?")
    answer = input("You: ")
    if "OSFirstTimer" in answer:
        print("OSFirstChatbot!")
        memory['talkbot'] = "OSFirstTimer"
        memory['status'] = "morenewer"
        save()
        print("Now, remeber that video where Phil was seeing if Ubuntu 12.10 could replace Windows 7?")

    elif "Technology" in answer:
        print("Wow, you like technology?")
        print("Let's talk about that!")
        memory['talkbot'] = "Technology"
        memory['status'] = 'morenewer'
        save()
    elif "IRC" in answer:
        print("That means the communcation protocol called IRC, right?")
        answer = input("You: ")
        if "Yes" in answer:
            print("OK!")
            memory['talkbot'] = "IRC"
            save()
        elif "No" in answer:
            print("I don't know what else is called IRC.")
        else:
            print("OK!")