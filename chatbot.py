# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Charlie',
    silence_performance_warning=True
)

chatbot.set_trainer(ListTrainer)

# # Tran the chat bot  with an example conversation
# chatbot.train([
#     "Will you never Go Away?",
#     "No, Never",
# ])

# Train based on the english conversations corpus
chatbot.train("chatterbot.corpus.english.conversations")
print("Waiting for response....")
# Get a response to the input text 'How are you?'
response = chatbot.get_response('What is AI?')

print(response)
