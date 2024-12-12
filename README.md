# SimpleBot Chatbot

This project demonstrates how to create and train a chatbot using the [ChatterBot](https://chatterbot.readthedocs.io/) library in Python. The chatbot is named **SimpleBot** and is trained on the English corpus provided by ChatterBot.

## Prerequisites

Before running the code, ensure that the following are installed:

1. Python (compatible versions: 3.6–3.8 for best results)
2. Required Python libraries:
   - `chatterbot`
   - `chatterbot_corpus`

Install these dependencies using pip:

```bash
pip install chatterbot chatterbot_corpus
```

## Project Files

- **main.py**: The main Python script to run the chatbot.
- **README.md**: Documentation for the project.

## How to Run

1. Clone or download the project.
2. Navigate to the project directory.
3. Ensure all dependencies are installed.
4. Run the script:

```bash
python main.py
```

5. Interact with SimpleBot in the terminal. Type `exit` to end the chat session.

## Code Explanation

### Import Libraries

```python
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
```
These modules are necessary for creating and training the chatbot.

### Initialize ChatBot

```python
chatbot = ChatBot('SimpleBot')
```
Creates a chatbot instance named `SimpleBot`.

### Training

```python
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')
```
Trains the chatbot using the English language corpus provided by ChatterBot.

### Chat Loop

```python
print("Hello! I am SimpleBot. Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("SimpleBot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print(f"SimpleBot: {response}")
```
A loop that takes user input and generates a response. The loop ends when the user types `exit`.

## Common Issues

1. **Compatibility**:
   ChatterBot is no longer actively maintained and works best with Python 3.6–3.8.

2. **Corpus Download**:
   If you encounter errors regarding missing corpora, download them manually by running:
   ```bash
   python -m chatterbot_corpus.download
   ```

## Future Enhancements

- Add support for more languages.
- Use custom datasets to train the chatbot for specific domains.
- Integrate with a GUI or web application for better usability.

## License

This project is licensed under the MIT License. Feel free to modify and distribute it as needed.
