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

bots = [catBot, bunnyBot, dogBot, slothBot, penguinBot, pandaBot]
for c in bots :
    trainer = ChatterBotCorpusTrainer(c)
    trainer.train("chatterbot.corpus.english")


training_data = open('training/data.txt').read().splitlines()

cat_data = open("training/cat.txt").read().splitlines()
catTrainer = ListTrainer(catBot)
catTrainer.train(cat_data)

bunny_data = open("training/bunny.txt").read().splitlines()
bunnyTrainer = ListTrainer(bunnyBot)
bunnyTrainer.train(bunny_data)

dog_data = open("training/dog.txt").read().splitlines()
dogTrainer = ListTrainer(dogBot)
dogTrainer.train(dog_data)

sloth_data = open("training/sloth.txt").read().splitlines()
slothTrainer = ListTrainer(slothBot)
slothTrainer.train(sloth_data)

penguin_data = open("training/penguin.txt").read().splitlines()
penguinTrainer = ListTrainer(penguinBot)
penguinTrainer.train(penguin_data)

panda_data = open("training/panda.txt").read().splitlines()
pandaTrainer = ListTrainer(pandaBot)
pandaTrainer.train(panda_data)

bot_dict = {"cat":catBot, "dog": dogBot, "panda": pandaBot, "penguin":penguinBot, \
    "bunny":bunnyBot, "sloth":slothBot}
bot_name = ""

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cat", methods=['POST'])
def cat():
    bot_name = "cat"
    return render_template("cat.html")

@app.route("/dog", methods=['POST'])
def dog():
    bot_name = "dog"
    return render_template("dog.html")

@app.route("/sloth", methods=['POST'])
def sloth():
    bot_name = "sloth"
    return render_template("sloth.html")

@app.route("/penguin", methods=['POST'])
def penguin():
    bot_name = "penguin"
    return render_template("penguin.html")

@app.route("/panda", methods = ['POST'])
def panda():
    bot_name = 'panda'
    return render_template("panda.html")

@app.route("/bunny", methods=['POST'])
def bunny():
    bot_name = 'bunny'
    return render_template("bunny.html")


@app.route("/get")

#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    bot = bot_dict.get(bot_name)
    return str(bot.get_response(userText))


@app.route('/send_message', methods=['POST'])
def send_message():
    bot = bot_dict.get(bot_name)
    input_json = request.get_json(force = True)
    if input_json['type'] =='panda':
        return str(bot.get_response(input_json['msg']))

if __name__ == "__main__":
    app.debug = True
    app.run(port=7000)