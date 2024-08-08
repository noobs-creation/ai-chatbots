from minichat import minichat

chatbot = minichat.Minichat()

while True:
    question = input("You: ")
    answer = chatbot.chat(question)
    print("Bot:", answer)