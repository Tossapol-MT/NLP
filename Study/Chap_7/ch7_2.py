from urllib import response
# Define variables
bot_template = "BOT : {0}"

# Define a dictionary with the predefined responses
name = "Bot"
weather = "cloudy"
responses = {
    "what's your name?" : "my name is {0}".format(name),
    "what's today's weather?" : "the weather is {0}".format(weather),
    "default" : "default message"
}

    # Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
    # Return the matching message
        bot_message = responses[message]
    else:
    # Return the "default" message
        bot_message = responses["default"]
    return bot_message

def sent_message(message):
    response = respond(message)
    print(bot_template.format(response))

print(bot_template.format("Hi!"))
value = input("USER : ")
sent_message(value)