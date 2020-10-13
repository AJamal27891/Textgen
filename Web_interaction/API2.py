from flask import Flask, jsonify, request, render_template , make_response
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import numpy
import tensorflow as tf
import requests
import subprocess
import json
from Model.src.interactive_conditional_samples import interact_model
import os
app = Flask(__name__)


api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.TextGenDB
users = db["Users"]
admin_pw = "@1234-dskafjl"

def UserExist(username):
    if users.find({"Username":username}).count() == 0:
        return False
    else:
        return True


class Register(Resource):
    # def get(self):
    #     headers = {'Content-Type':'text/html'}
    #     return make_response(render_template('register.html'),200,headers)

    def post(self):
        #Step 1 is to get posted data by the user
        postedData = request.get_json()
        #Get the data
        username = postedData["username"]
        password = postedData["password"] #"123xyz"
        email = postedData["email"]

        if UserExist(username):
            retJson = {
                'status':301,
                'msg': 'Invalid Username'
            }
            return jsonify(retJson)

        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        #Store username and pw into the database
        users.insert({
            "Username": username,
            "Password": hashed_pw,
            "email":email,
            "Tokens":10
            })


        retJson = {
            "status": 200,
            "msg": "You successfully signed up for the API"
        }
        return jsonify(retJson)




def verifyPw(username, password):
    if not UserExist(username):
        return False

    hashed_pw = users.find({
        "Username":username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def generateReturnDictionary(status, msg):
    retJson = {
        "status": status,
        "msg": msg
    }
    return retJson

def verifyCredentials(username, password):
    if not UserExist(username):
        return generateReturnDictionary(301, "Invalid Username"), True

    correct_pw = verifyPw(username, password)

    if not correct_pw:
        return generateReturnDictionary(302, "Incorrect Password"), True

    return None, False


class TextGen(Resource):
    # def get(self):
    #     headers = {'Content-Type':'text/html'}
    #     return make_response(render_template('textgen.html'),200,headers)

    def post(self):
        postedData = request.get_json()
        nsamples = 1
        model_name = '117M'
        length=None
        top_k = 0
        temperature = 1

        username = postedData["username"]
        InText = postedData["in_text"]
        password = postedData["password"]
        nsamples = postedData["nsamples"]
        model_name = postedData['model_name']
        length = postedData['length']
        temperature =   postedData['temperature']
        top_k= postedData['top_k']

        tokens = users.find({
            "Username":username
        })[0]["Tokens"]

        retJson, error = verifyCredentials(username, password)
        if error:
            return jsonify(retJson)


        elif tokens<=0:
            return jsonify(generateReturnDictionary(303, "Not Enough Tokens"))

        # InText = requests.get(InText)
        # nsamples= request.get(nsamples)
        # model_name = request.get(model_name)
        #retJson = {}
        # the generator
        else:
            text = interact_model(model_name= model_name,nsamples=nsamples,texting=InText,length=length,temperature=temperature,top_k=top_k)
            retJson = {"output":text}
            users.insert({'InputText':InText,'OutputText':text})
            '''
            with open('temp.jpg', 'wb') as f:
                f.write(r.content)
                proc = subprocess.Popen('python classify_image.py --model_dir=. --image_file=./temp.jpg', stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                ret = proc.communicate()[0]
                proc.wait()
                with open("text.txt") as f:
                    retJson = json.load(f) '''


            users.update({
                "Username": username
            },{
                "$set":{
                    "Tokens": tokens-1
                }
            })

            return jsonify(generateReturnDictionary(200, text))


class Refill(Resource):
    # def get(self):
    #     headers = {'Content-Type':'text/html'}
    #     return make_response(render_template('refill.html'),200,headers)

    def post(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["admin_pw"]
        amount = postedData["amount"]

        if not UserExist(username):
            return jsonify(generateReturnDictionary(301, "Invalid Username"))


        if password != admin_pw:
            return jsonify(generateReturnDictionary(302, "Incorrect Password"))
        else:
            users.update({
                "Username": username
            },{
                "$set":{
                    "Tokens": amount
                }
            })
            return jsonify(generateReturnDictionary(200, "Refilled"))


class Del(Resource):
    def delete(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"] #"123xyz"
        retJson, error = verifyCredentials(username, password)
        if error:
            return jsonify(retJson)
        else:
            users.delete_one({"Username":username})
            return jsonify(generateReturnDictionary(200, "User %s was deleted"%username))

class AdDel(Resource):
    def delete(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["admin_pw"]
        if password != admin_pw:
            return jsonify(generateReturnDictionary(302, "Incorrect Password"))
        else:
            users.delete_one({"Username":username})
            return jsonify(generateReturnDictionary(200, "User %s was deleted by admin"%username))


class AllUsers(Resource):
    def get(self ):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["admin_pw"]
        if password != admin_pw:
            return jsonify(generateReturnDictionary(302, "Incorrect Password"))
        else:
            data =  [doc for doc in users.find({},{"Username":1,"_id": 0})]
            return jsonify(data)


class welcome(Resource):
     def get(self):
        return render_template('welcome.html')
#
#
#     def get(request):
#         headers = {'Content-Type':'text/html'}
#         return make_response(render_template('home.html'),200,headers)
#api.add_resource(interface,"/interface")
api.add_resource(welcome, '/')
api.add_resource(Register, '/register')
api.add_resource(TextGen, '/TextGen')
api.add_resource(Refill, '/refill')
api.add_resource(Del,'/deleteuser')
api.add_resource(AdDel,'/admindeleteuser')
api.add_resource(AllUsers,'/allusers')



if __name__=="__main__":
    app.run(debug=False,host='0.0.0.0')
