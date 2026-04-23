import sys
import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

# import and create a Conll extractor to use later 
extractor = ConllExtractor()

print('Hello, I am Marvin, the simple robot.\nYou can end this conversation at any time by typing "bye"\nAfter typing each answer, press "enter"\nHow are you today?')

random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

responseid = random.randint(0,len(random_responses)-1)
phrase = input("> ")

while "bye" not in phrase.lower().split():
    phrase_blob = TextBlob(phrase, np_extractor=extractor)
    np = phrase_blob.noun_phrases
    polarity = phrase_blob.polarity

    if polarity <= -0.5:
        response = "Oh, that sounds bad! "
    elif polarity <= 0:
        response = "Meh... "
    elif polarity <= 0.5:
        response = "That sounds good. "
    else:
        response = "Well, life is life! "
    
    print(np)
    if np:
        response += "Tell me more about " + np[0].pluralize() + '.'
    else:
        response += "Tell me more !"
    #responseid = random.randint(0,len(random_responses)-1)
    print(response)
    phrase = input("> ")

print("It was nice talking to you, goodbye!")