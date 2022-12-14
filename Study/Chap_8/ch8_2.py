import re
bot_template = "BOT : {0}"
user_template = "USER : {0}"

def find_name(message):
    name = None
    # Create a pattern for checking if the keywords occur
    name_keyword = re.compile('name|call')
    # Create a pattern for finding capitalized words
    name_pattern = re.compile('[A-Z]{1}[a-z]*')
    if name_keyword.search(message):
    # Get the matching words in the string
        name_words = name_pattern.findall(message)
        if len(name_words) > 0:
        # Return the name if the keywords are present
            name = ' '.join(name_words)
    return name


# Define respond()
def respond(message):
# Find the name
    name = find_name(message)
    if name is None:
        return "Hi there!"
    else:
        return "Hello, {0}!".format(name)


# Send messages
def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

responses = {'greet': 'Hello you! :', 'goodbye': 'goodbye for now','thankyou': 'you are very welcome', 'default': 'default message'}
# Send messages
send_message("my name is David Copperfield")
send_message("call me Ishmael")
send_message("people call me Cassandra")
send_message("I walk to school")