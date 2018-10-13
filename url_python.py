from flask import  Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

# db_connect = create_engine('sqllite:///url.db')
urlApp = Flask(__name__)
urlApi = Api(urlApp)
