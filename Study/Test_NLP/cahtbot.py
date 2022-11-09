from urllib import response
import webbrowser
import datetime
import wikipedia
import re
import random

user_template = "USER : {0}"
bot_template = "BOT : {0}"

name = "Bot"

def theDay():
# This function is for the day
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {
    1: 'Monday', 2: 'Tuesday',
    3: 'Wednesday', 4: 'Thursday',
    5: 'Friday', 6: 'Saturday',
    7: 'Sunday'
    }
    if day in Day_dict.keys():
        weekday = Day_dict[day]
    return ("it's " + weekday)

def theTime():
    # This function is for time
    time = str(datetime.datetime.now())
    # time needs to be sliced for
    # better audio comprehension
    print(time)
    hour = time[11:13]
    min = time[14:16]
    return ("The time right now is " + hour + "Hours and " + min + " Minutes")   

def respond(message):
    bot_message = ''
    if "what's your name" in message:
        bot_message = "I'am {0}".format(name)
    elif "what day is it" in message:
        bot_message = theDay()

    elif "what time is it" in message:
        bot_message = theTime()
    elif "open google" in message:
        print(bot_template.format("Opening Google..."))
        message = message.replace("google search", "")
        webbrowser.open("https://www.google.co.th/search?q="+message)

    elif "wikipedia summary" in message:
        print(bot_template.format("Checking the wikipedia..."))
        message = message.replace("wikipedia summary", " ")
        result = wikipedia.summary(message, sentences=4)
        print("As per wikipedia")
        print(result)

    elif "youtube search" in message:
        print(bot_template.format("Checking the Youtube..."))
        message = message.replace("youtube search", " ")
        webbrowser.open("https://www.youtube.com/"+message)
    return bot_message


def send_message(message):
    response = respond(message)
    print(bot_template.format(response))

print(bot_template.format("Hi!"))
value = input("USER : ")
send_message(value)
