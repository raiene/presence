from flask import Flask
import mongoengine
from flask_bootstrap import Bootstrap
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)
db = mongoengine
db.connect(**Config.MONGODB_SETTINGS) # connects to database named microblog


from app import views, model

if __name__ == '__main__':
    app.run()