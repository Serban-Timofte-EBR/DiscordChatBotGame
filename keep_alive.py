
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
