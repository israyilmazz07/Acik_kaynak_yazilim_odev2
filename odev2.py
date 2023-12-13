from flask import Flask, request

from flask_restful import Api, Resource

import pandas as pd

import requests




app = Flask(__name__)

api = Api(app)



class Even(Resource):

   def get(self, number):

       url = f"https://api.isevenapi.xyz/api/iseven/{number}/"



       response = requests.get(url)

       data = response.json()

       return {'data' : data}, 200





api.add_resource(Even, "/iseven/<int:number>/")




if __name__ == '__main__':

   app.run(host="0.0.0.0", port=6767)

   app.run()
