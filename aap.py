from flask import Flask, app
from flask_restful import Api
from flask_jwt import JWT
from db import db

    
from secure import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,Item_List
from resources.store import Store,StoreList

aap= Flask(__name__)

db.init_app(aap)    

aap.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
aap.config["SQLALCHMEY_TRACK_MODIFICATIONS"]= False
aap.secret_key = 'pgpg'
api= Api(aap)

@aap.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(aap,authenticate,identity)

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Item_List,'/items')
api.add_resource(StoreList,"/stores")

api.add_resource(UserRegister, "/Register")

aap.run(port=4500,debug=True)