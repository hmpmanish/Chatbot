from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#hmpmanish #hmpmanish
#hmpmanish #hmpmanish
# Create a chatbot instance
chatbot = ChatBot('SimpleBot')

# Train the chatbot with English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')
#hmpmanish
#hmpmanish
#hmpmanish

# Chat loop
print("Hello! I am SimpleBot. Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("SimpleBot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print(f"SimpleBot: {response}")
#hmpmanish #hmpmanish
#hmpmanish #hmpmanish
