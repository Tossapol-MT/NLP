from matplotlib.pyplot import text
from textblob import TextBlob

# text = "To day is so shy"
def sentiment_check(text):
    #สร้างtext object
    blob_response_msg = TextBlob(text)
    
    if blob_response_msg.sentiment[0] > 0:
        show = "Positive (+)"
    elif blob_response_msg.sentiment[0] == 0:
        show = "Neutral (=)"
    else:
        show = "Negative (-)"
    return(show)

# print(sentiment_check(text))