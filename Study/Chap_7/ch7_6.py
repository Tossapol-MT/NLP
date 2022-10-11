import re
import random
bot_template = "BOT : {0}"

rules = {
'do you think (.*)': [
    'if{0}? Absolutely.',
    'No chance'],
'do you remember (.*)': [
    'Did you think I would forget{0}',
    "Why haven't you been able to forget{0}",
    'What about{0}',
    'Yes .. and?'],
'I want (.*)': [
    'What would it mean if you got{0}',
    'Why do you want{0}',
    "What's stopping you from getting{0}"],
'if (.*)': [
    "Do you really think it's likely that{0}",
    'Do you wish that{0}',
    'What do you think about{0}',
    'Really--if{0}']
}

def match_rule(rules, message):
    response, phrase = "default", None
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response.format(phrase)

def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
    # Replace 'me' with 'you'
        message = re.sub("me","you", message)
    if 'my' in message:
    # Replace 'my' with 'your'
        message = re.sub("my","your", message)
    if 'your' in message:
    # Replace 'your' with 'my'
        message = re.sub("your","my", message)
    if 'you' in message:
    # Replace 'you' with 'me'
        message = re.sub("you","me", message)
    if 'i' in message:
    # Replace 'me' with 'you'
        message = re.sub("i","you", message)
    return message

def respond(message):
    # Call match_rule
    ____ = ____
    ____ = ____

    if '{0}' in response:
    # Replace the pronouns in the phrase
    phrase = replace_pronouns(message)
    # Include the phrase in the response
    response = 
    return response

def sent_message(message):
    response = respond(message)
    print(bot_template.format(response))

print(bot_template.format("Hi!"))
value = input("USER : ")
sent_message(value)

# Send the messages
send_message("do you remember my last birthday")
# send_message("do you think humans should be worried about AI")
# send_message("I want a robot friend")
# send_message("what if you could be anything you wanted")