import pickle
import os
import json
chatbotdata = input("Enter in your chatbot data: ")
print("TommyChatbot")
print("Decoding data...")
memory = json.loads(chatbotdata)
if memory["status"] == "new":
    print("Hi! My name is " + memory[name] + ". What's your name?")
    memory["yourname"] = input("You: ")
    chatbotdata["yourname"] = memory["yourname"]
    print("Hi " + memory["yourname"] + "!")
    print("Anyways, isn't the Chatbot Network great?")
    answer = input("You: ")
    if answer == "Yes." or "Yes!":
        print("I think that too!")
    else:
        print("While, I don't understand why not.")
    print("Anyways, test!")
