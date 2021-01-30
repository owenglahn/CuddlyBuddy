#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
app = Flask(__name__, template_folder='template', static_folder='static')

#create chatbot
catBot = ChatBot("Camilla", storage_adapter="chatterbot.storage.SQLStorageAdapter")
bunnyBot = ChatBot("Benny", storage_adapter="chatterbot.storage.SQLStorageAdapter")

training_data = open('training/data.txt').read().splitlines()

catTrainer = ListTrainer(catBot)
catTrainer.train(training_data)
bunnyTrainer = ListTrainer(bunnyBot)
bunnyTrainer.train(training_data)

cat_bool = False
bunny_bool = False

#define app routes
@app.route("/cat", methods=['GET', 'POST'])
def cat():
    cat_bool = True
    return render_template("cat.html")
@app.route("/bunny", methods=['GET', 'POST'])
def bunny():
    bunny_bool = True
    return render_template("bunny.html")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    if cat_bool:
        bot = catBot
    elif bunny_bool:
        bot = bunnyBot
    else:
        bot = bunnyBot
    return str(bot.get_response(userText))
if __name__ == "__main__":
    app.run(port=7000)