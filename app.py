#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
app = Flask(__name__, template_folder='template', static_folder='static')

#create chatbot
catBot = ChatBot("Camilla", storage_adapter="chatterbot.storage.SQLStorageAdapter")
bunnyBot = ChatBot("Benny", storage_adapter="chatterbot.storage.SQLStorageAdapter")
dogBot = ChatBot("Domino", storage_adapter="chatterbot.storage.SQLStorageAdapter")
slothBot = ChatBot("Sammy", storage_adapter="chatterbot.storage.SQLStorageAdapter")
penguinBot = ChatBot("Penelope", storage_adapter="chatterbot.storage.SQLStorageAdapter")
pandaBot = ChatBot("Pax", storage_adapter="chatterbot.storage.SQLStorageAdapter")

training_data = open('training/data.txt').read().splitlines()

catTrainer = ListTrainer(catBot)
catTrainer.train(training_data)
bunnyTrainer = ListTrainer(bunnyBot)
bunnyTrainer.train(training_data)
dogTrainer = ListTrainer(dogBot)
dogTrainer.train(training_data)
slothTrainer = ListTrainer(slothBot)
slothTrainer.train(training_data)
penguinTrainer = ListTrainer(penguinBot)
penguinTrainer.train(training_data)
pandaTrainer = ListTrainer(pandaBot)
pandaTrainer.train(training_data)

cat_bool = False
bunny_bool = False
dog_bool = False
sloth_bool = False
penguin_bool = False
panda_bool = False

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cat")
def cat():
    cat_bool = True
    return render_template("cat.html")

@app.route("/dog")
def dog():
    dog_bool = True
    return render_template("dog.html")

@app.route("/sloth")
def sloth():
    sloth_bool = True
    return render_template("sloth.html")

@app.route("/penguin")
def penguin():
    penguin_bool = True
    return render_template("penguin.html")

@app.route("/panda")
def panda():
    panda_bool = True
    return render_template("panda.html")

@app.route("/bunny")
def bunny():
    bunny_bool = True
    return render_template("bunny.html")


@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    if cat_bool:
        bot = catBot
    elif bunny_bool:
        bot = bunnyBot
    elif dog_bool:
        bot = dogBot
    elif sloth_bool:
        bot = slothBot
    elif penguin_bool:
        bot = penguinBot
    elif panda_bool:
        bot = pandaBot
    else:
        bot = catBot # default, when i use None there is an error
    return str(bot.get_response(userText))
if __name__ == "__main__":
    app.run(port=7000)