import random
from unicodedata import name

from ch7 import respond

bot_template = "BOT : {0}"
name = "Bot"
weather = "cloudy"

responses = {
    "what's your name?" : [
        "my name is {0}".format(name),
        "they call me {0}".format(name),
        "I am {0}".format(name)
    ],
    "what's today's weather?": [
        "the wather is {0}".format(weather),
        "it's {0} today".format(weather),
    ],
    "default" : ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
    # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
    # Return a random "default" response
        bot_message = random.choice(responses["default"])
    return bot_message

def sent_message(message):
    response = respond(message)
    print(bot_template.format(response))

print(bot_template.format("Hi!"))
value = input("USER : ")
sent_message(value)