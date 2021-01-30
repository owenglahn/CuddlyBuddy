#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
app = Flask(__name__, template_folder='template', static_folder='static')
#create chatbot
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
training_data = open('training/data.txt').read().splitlines()
#trainer = ChatterBotCorpusTrainer(englishBot)
#trainer.train("chatterbot.corpus.english") #train the chatter bot for english
trainer = ListTrainer(englishBot)
trainer.train(training_data)
#define app routes
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))
if __name__ == "__main__":
    app.run(port=7000)