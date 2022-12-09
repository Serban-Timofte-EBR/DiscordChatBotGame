''The discord server which will host our chatbot! This server will stop running after one hour! I saw this code on GitHub here: https://gist.github.com/beaucarnes/51ec37412ab181a2e3fd320ee474b671 . I update it using uptimerobot.com where I created a monitor directly on the website which will pink the server every 5 minutes to keep it running!'''

from flask import Flask        # use it like an webserver 
from threading import Thread   # the server will run on other server of the bot so they will be able so run in the same time



app = Flask('')



@app.route('/')
def home():
 return "Hello. I am alive!" #return message for everyone who visit the server



def run():
 app.run(host='0.0.0.0',port=8080)



def keep_alive():
 t = Thread(target=run)
 t.start()
