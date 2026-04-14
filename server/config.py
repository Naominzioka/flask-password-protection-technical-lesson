from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

#create bycrypt instance from app
bcrypt = Bcrypt(app)

api = Api(app)


"""
Note on Configuration
Take note of the new config.py file in the server/ directory. As our app is getting more and more complex,
setting up a config file can help clean up our code a bit.

In each of our applications so far, app.py needed to import from models.py 
in order to initialize the database's connection to the app. 
That's still the case here, 
but we also find ourselves with the need to import an instantiated Bcrypt from app.py into models.py! 
This creates a circular import, 
where objects in two separate files are dependent upon one another to function.

To avoid this, you can often refactor your objects to avoid unnecessary dependencies (we're all guilty of this!),
you can refactor your code into one large file, or you can move some of your imports and configurations into a third file. 
That's what we did here - check out config.py and you'll notice a lot of familiar code. 
We took the imports and configurations from app.py and models.py and put them together to avoid circular imports. 
These are then imported by app.py and models.py when they're ready to be used.
"""
