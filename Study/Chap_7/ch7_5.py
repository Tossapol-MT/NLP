import re
# Define replace_pronouns()
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
    
print(replace_pronouns("my last birthday"))
print(replace_pronouns("go with me to Florida"))
print(replace_pronouns("I had my own castle"))