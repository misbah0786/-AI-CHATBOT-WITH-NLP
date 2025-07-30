import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a simple NLP Chatbot created for an internship task."]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, but I'm doing great!", "Feeling chatty!"]
    ],
    [
        r"what can you do ?",
        ["I can answer basic questions. Try asking about the weather, time, or general queries."]
    ],
    [
        r"(.*) your internship task",
        ["Yes, I am a part of the CodTech internship Task 3 for NLP Chatbot."]
    ],
    [
        r"bye|exit",
        ["Goodbye!", "Have a nice day!", "Exiting..."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you rephrase?"]
    ]
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Run chatbot
print("Hi! I am your internship NLP Chatbot. Type 'bye' to exit.")
chatbot.converse()
